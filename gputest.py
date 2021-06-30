# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:37:40 2021

@author: robert
"""

import tensorflow as tf
print(tf.version.VERSION)

from tensorflow.python.client import device_lib
tf.config.list_physical_devices('GPU')

device_lib.list_local_devices()

tf.test.is_built_with_cuda()

tf.test.is_gpu_available()

