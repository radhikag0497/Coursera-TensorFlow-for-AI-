# -*- coding: utf-8 -*-
"""Fashion MNIST Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o0Zul9VeeS-jh59sY-GAH9HcXzfk7sm3
"""

import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs = {}):
        if(logs.get('loss')<0.4):
            print('\nReached 60% accuracy to cancelling training!')
            self.model.stop_training = True

callbacks = myCallback()
fashion_mnist = keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = fashion_mnist.load_data()

np.set_printoptions(linewidth=200)

plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape = (28,28)), # becoz our input images are 28X28
                          tf.keras.layers.Dense(128, activation = tf.nn.relu),
                          tf.keras.layers.Dense(10, activation= tf.nn.softmax) # becoz we have 10 classes of clothing in dataset
])

model.compile(optimizer = tf.optimizers.Adam(), loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5, callbacks = [callbacks])

model.evaluate(test_images, test_labels)