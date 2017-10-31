# coding: utf-8

import tensorflow as tf

# val1 = tf.zeros([2, 5], tf.int32)
# input_tensor = [[1, 2], [3, 4], [5, 6]]
# val2 = tf.zeros_like(input_tensor)
# val3 = tf.ones([2, 3], tf.int32)
# val4 = tf.ones_like(input_tensor)
# val5 = tf.fill([2, 3], 8)
#
# linspace1 = tf.linspace(10.1, 20, 4, name='linspace')
# range1 = tf.range(10, 20, 2, name='range1')
#
# a = tf.constant([3, 6])
# b = tf.constant([3, 2])
# c = tf.div(a, b)
#
# t_0 = 19
# t_0Zero = tf.zeros_like(t_0)
# t_0Ones = tf.ones_like(t_0)
#
# t_1 = ['apple', 'peach', 'grape']
# t_1Zeros = tf.zeros_like(t_1)
# # t_1Ones = tf.ones_like(t_1)
#
# with tf.Session() as sess:
#     # print(sess.run(val1))
#     # print(sess.run(val2))
#     # print(sess.run(val3))
#     # print(sess.run(val4))
#     # print(sess.run(val5))
#     # print(sess.run(linspace1))
#     # print(sess.run(range1))
#     # print(sess.run(c))
#     print(sess.run(t_1Zeros))
#
# my_const = tf.constant([1.0, 2.0], name="my_const")
# # print(tf.get_default_graph().as_graph_def())
# #
# # a = tf.Variable(2, name="scalar")
# # print(type(a))
# # print(type(my_const))
# W = tf.Variable(tf.truncated_normal([7, 10]))
# # const = 1
# W2 = tf.Variable(10)
# assign_op = W2.assign(100)
#
# a = tf.Variable(2, name="scalar")
# a_times_two = a.assign(a.initialized_value() * 2)
#
# W3 = tf.Variable(10)
# U = tf.Variable(W.initialized_value() * 2)
#
# with tf.Session() as sess:
#     # init = tf.global_variables_initializer()
#     # print(type(init))
#     # tf.global_variables_initializer().run()
#     # initW = tf.variables_initializer([W])
#     # sess.run(initW)
#     sess.run(tf.global_variables_initializer())
#     # print(type(initW))
#     print(type(W))
#     print(type(my_const))
#     print(W.eval())
#     sess.run(assign_op)
#     print(W2.eval())
#
#     sess.run(a_times_two)
#     print(a.eval())
#     sess.run(a_times_two)
#     print(a.eval())
#     sess.run(a_times_two)
#     print(a.eval())
#
#     print(W3.assign_add(112))
#     print(W3.assign_sub(20))
#
#     print(U.eval())
#
# sess1 = tf.Session()
# sess2 = tf.Session()
#
# sess1.run(W3.initializer)
# sess2.run(W3.initializer)
#
# print(sess1.run(W3.assign_add(1)))
# print(sess1.run(W3.assign_sub(2)))
#
# print(sess2.run(W3.assign_add(3)))
# print(sess2.run(W3.assign_sub(14)))
#
# sess1.close()
# sess2.close()
#
# sess3 = tf.InteractiveSession()
#
#
# print(tf.get_default_session())

a = tf.placeholder(tf.float32, shape=[3])
b = tf.constant([5, 5, 5], tf.float32)
c = a + b
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./my_graph', sess.graph)
    print(sess.run(c, feed_dict={a: [1, 2, 3]}))