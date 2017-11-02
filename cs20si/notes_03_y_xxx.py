# coding: utf-8
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

DATA_FILE = "../stanford-tensorflow-tutorials/data/fire_theft.xls"

book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

w1 = tf.Variable(0.0, name="weights_1")
w2 = tf.Variable(0.0, name="weights_2")
w3 = tf.Variable(0.0, name="weights_3")
b = tf.Variable(0.0, name="bias")

Y_predicted = X * X * X * w1 + X * X * w2 + X * w3 + b

loss = tf.square(Y - Y_predicted, name="loss") / 1e5

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-4).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        total_loss = 0
        for x, y in data:
            _, loss_value = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += loss_value
        print('Epoch: {0}, loss: {1}'.format(i, total_loss/n_samples))

    w1_value, w2_value, w3_value, b_value = sess.run([w1, w2, w3, b])
    print('w1: {0}, w2: {1}, w3: {2}, b: {3}'.format(w1_value, w2_value, w3_value, b_value))

X, Y = data.T[0], data.T[1]
plt.plot(X, Y, 'bo', label='Real data')
plt.plot(X, X * X * X * w1_value + X * X * w2_value + X * w3_value + b_value, 'ro', label='Predicted data')
plt.legend()
plt.show()
