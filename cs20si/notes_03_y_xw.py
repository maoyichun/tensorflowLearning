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

w = tf.Variable(0.0, name="weights")
b = tf.Variable(0.0, name="bias")

Y_predicted = X * w + b

loss = tf.square(Y - Y_predicted, name="loss")

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        total_loss = 0
        for x, y in data:
            _, loss_value = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += loss_value
        print('Epoch: {0}, loss: {1}'.format(i, total_loss/n_samples))

    w_value, b_value = sess.run([w, b])
    print('w: {0}, b: {1}'.format(w_value, b_value))

X, Y = data.T[0], data.T[1]
plt.plot(X, Y, 'bo', label='Real data')
plt.plot(X, X * w_value + b_value, 'r', label='Predicted data')
plt.legend()
plt.show()
