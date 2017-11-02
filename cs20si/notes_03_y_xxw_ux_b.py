# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = "../stanford-tensorflow-tutorials/data/fire_theft.xls"

book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

w = tf.Variable(0.0, name="weights_1")
u = tf.Variable(0.0, name="weights_2")
b = tf.Variable(0.0, name="bias")

Y_predicted = X * X * w + X * u + b

# 除以1e5防止loss过大溢出 输出nan
loss = tf.square(Y - Y_predicted, name="loss") / 1e3

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        total_loss = 0
        for x, y in data:
            # sess.run(optimizer, feed_dict={X: x, Y: y})
            # w_value, u_value, b_value = sess.run([w, u, b], feed_dict={X: x, Y: y})
            # loss1 = sess.run(loss, feed_dict={X: x, Y: y})
            _, loss_value = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += loss_value
        print('epoch: {0}, loss: {1}'.format(i, total_loss * 1e3/n_samples))

    w_value, u_value, b_value = sess.run([w, u, b])
    print('w: {0}, u: {1}, b: {2}'.format(w_value, u_value, b_value))

X_data, Y_data = data.T[0], data.T[1]
plt.plot(X_data, Y_data, 'bo', label='Real data')
plt.plot(X_data, X_data * X_data * w_value + X_data * u_value + b_value, 'ro', label='Predicted data')
plt.legend()
plt.show()
