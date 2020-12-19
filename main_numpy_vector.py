#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":

    print(np.__version__)

    # np.array 基础
    lst = [1, 2, 3]
    lst[0] = "Linear Algebra"
    print(lst)

    vec = np.array([1, 2, 3])
    print(vec)
    # vec[0] = "Linear Algebra"
    # vec[0] = 666
    # print(vec)

    # np.array的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))

    # np.array的基本属性
    print(vec)
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0: 2])
    print(type(vec[0: 2]))

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))


    # 计算模
    print(np.linalg.norm(vec))
    #计算单位向量
    print(vec / np.linalg.norm(vec))
    #计算单位向量的模
    print(np.linalg.norm(vec / np.linalg.norm(vec)))

    # zero3 = np.zeros(3)
    # print(zero3 / np.linalg.norm(zero3))


    a = np.array([[1,2],[3,4]])
    b= np.array([10, 100])
    print(b)
    print(a.shape)
    print(b.shape)
    print(a.dot(b))