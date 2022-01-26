#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.01.22
@author: felix
"""
from typing import List

from override.class_tools import override


class Example:
    @override
    def other_func(self):
        return 0

    @override
    def other_func(self, a: int, b: int):
        return (a + b) * (a + b)

    @override
    def my_func(self):
        return 0

    @override
    def my_func(self, a: int, b: str):
        return b * a

    @override
    def my_func(self, a: int, b: int):
        return a * b

    @override
    def my_func(self, a: int, b: int, c: int):
        return a * b * c

    @override
    def my_func(self, *, val: int, other_val: int):
        return val, other_val

    @override
    def my_func(self, val: List[int], other_val, /):
        return [other_val * v for v in val]

    @override
    def my_func(self, val: List[str], other_val, /):
        return val, other_val


def test_with_simple_args():
    example = Example()
    assert example.my_func(2, 3) == 6
    assert example.my_func(2, "3") == "33"
    assert example.my_func() == 0
    assert example.my_func(2, 3, 4) == 24


def test_with_kwargs():
    pass
