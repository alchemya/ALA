#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vector:

    def __init__(self, lst):
        self._values = lst

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        """对系统自己而言"""
        return "Vector({})".format(self._values)

    def __str__(self):
        """对于使用者而言"""
        return "({})".format(", ".join(str(e) for e in self._values))
