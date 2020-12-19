#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from Alchemy_of_LA.Matrix import Matrix
from Alchemy_of_LA.Vector import Vector
import math


if __name__ == "__main__":

    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)

    #  x 扩大2倍， y扩大1.5倍
    # T = Matrix([[2, 0], [0, 1.5]])
    # 实现对x轴反转
    # T = Matrix([[1, 0], [0, -1]])
    # 实现y轴翻转
    # T = Matrix([[-1, 0], [0, 1]])
    # 实现 针对x轴和y轴的翻转
    # T = Matrix([[-1, 0], [0, -1]])
    # 沿着x轴进行错切，相当于斜体字
    # T = Matrix([[1, 0.5], [0, 1]])
    # 沿着y轴进行错切，相当于斜体字
    # T = Matrix([[1, 0], [0.5, 1]])


    #实现旋转操作
    theta = math.pi / 3
    T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    P2 = T.dot(P.T())
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.show()