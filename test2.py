#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 0025 17:47
# @Author  : Julianna
# @Site    : 
# @File    : test2.py
# @Software: PyCharm




def find(C, T):
    res = []
    for i in range(len(C)):
        for j in range(i+1, len(C)-1):
            data1 = []
            if C[i]==T:
                data1.append(C[i])
                break
            elif C[i]<T:
                if T-C[i] in C[i+1:]:
                    data1.append(C[i])
                    data1.append(T-C[i])
                    break
            elif C[i]+C[j]<T
        res.append(data1)
