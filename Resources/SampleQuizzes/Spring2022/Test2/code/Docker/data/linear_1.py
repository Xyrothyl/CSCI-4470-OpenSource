# MIT License
#
# Copyright (c) 2017 François Chollet
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# NOTE: This has minor changes for program control that does 
# not impact the overall concepts used in class.

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

def make_noisy_data(m=0.1, b=0.3, n=100):
  x = tf.random.uniform(shape=(n,1,1))
  noise = tf.random.normal(shape=(len(x),1,1), stddev=0.01)
  y = m * x + b + noise
  return x, y

def predict(m, b, x):
  y = m * x + b
  return y

def squared_error(y_pred, y_true):
  return tf.reduce_mean(tf.square(y_pred - y_true))

# Loading data
m = 0.1
b = 0.3
(train_images, train_labels) = make_noisy_data(m=m, b=b, n=60000)
(test_images, test_labels) = make_noisy_data(m=m, b=b, n=10000)


