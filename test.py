#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 0025 16:04
# @Author  : Julianna
# @Site    : 
# @File    : test.py
# @Software: PyCharm


'''无重复连续子串'''
# def strLength(s):
#     n = len(s)
#     final_len = []
#     for i in range(n):
#         data1 = s[i]
#         for j in range(i+1, n):
#             if s[j] not in data1:
#                 data1 = data1 + s[j]
#             else:
#                 break
#         final_len.append(len(data1))
#     if final_len==[]:
#         if s=='':
#             final_len.append(0)
#         else:
#             final_len.append(1)
#     return max(final_len)
#
#
# if __name__ == '__main__':
#     s = input()
#     print(list(s))
#     print(strLength(s))


'''解一元方程'''
# def solve(eq, var="X"):
#     eq1 = eq.replace("=","-(")+")"
#     c = eval(eq1, {var:1j})
#     if c.imag==0 and c.real==0:
#         return -1
#     else:
#         return int(-c.real/c.imag)
#
# if __name__ == '__main__':
#     eq = input()
#     print(solve(eq))
#

'''快手题：字符串排序'''

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    res = []
    for i in range(m):
        res.append(input())
    V = []
    P = []
    for i in range(m):
        if res[i][0] == 'V':
            V.append(res[i])
        else:
            P.append(res[i])
    M = []
    M.append(V[0])
    for i in range(1, m):
        if i < len(V):
            if i % n == 0:
                M.append(P.pop(0))
            M.append(V[i])
        else:
            break
    print(len(M))
    for i in range(len(M)):
        print(M[i])


