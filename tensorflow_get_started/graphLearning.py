# coding: utf-8

import tensorflow as tf
import numpy as np

c = tf.constant(1)
print(c.graph)
print(tf.get_default_graph())

with tf.Graph().as_default():
    d = tf.constant(2)
    print(d.graph)
print(c.graph)

g2 = tf.Graph()
print("g2:", g2)
g2.as_default()
e = tf.constant(11)
print(e.graph)

# sess = tf.Session()
x = tf.constant(1)
with tf.Session() as sess:
    value = x.eval()

print(value)
