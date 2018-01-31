# coding: utf-8

import tensorflow as tf
import numpy as np
import sys

features = {'SepalLength': np.array([6.4, 5.0]),
            'SepalWidth':  np.array([2.8, 2.3]),
            'PetalLength': np.array([5.6, 3.3]),
            'PetalWidth':  np.array([2.2, 1.0])}
labels = np.array([2, 1])
dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

# dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# dataset = tf.data.Dataset.from_tensor_slices((
#     np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
#     np.random.uniform(size=(5, 2))
# ))

# dataset = tf.data.Dataset.from_tensor_slices(
#     {
#         "a": np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
#         "b": np.random.uniform(size=(5, 2))
#     }
# )

# dataset = dataset.batch(2)
iterator = dataset.make_one_shot_iterator()
one_element = iterator.get_next()
with tf.Session() as sess:
    try:
        while True:
            print(sess.run(one_element))
    except tf.errors.OutOfRangeError:
        print("end!")

print(sys.path)
