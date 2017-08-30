import os
# import logging
# logging.basicConfig(level=logging.INFO)
# from functools import reduce
#
#
# def triangles(rows):
#     l = [1]
#     while len(l) <= rows:
#         yield l
#         l = [1] + [l[x] + l[x + 1] for x in range(len(l) - 1)] + [1]
#
#
# def str2float(s):
#     def char2num(c):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}[c]
#
#     def fn(x, y):
#         return x * 10 + y
#
#     cl = list(map(char2num, s))
#     n = s.index('.')
#     cl1 = cl[:n]
#     cl2 = cl[n+1:]
#     return reduce(fn, cl1) + (reduce(fn, cl2)) / (10 ** len(cl2))
#
#
# print(str2float('178768756.235645434'))


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally..')
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# # print(10 / n)

pwd = os.path.abspath('.')
