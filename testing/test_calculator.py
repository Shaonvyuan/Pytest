#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./data/calc.yml") as f:
        datas = yaml.safe_load(f)
    # return (datas['add']['datas'], datas['add']['ids'])
    return datas


# yaml json excel csv xml
# 测试类
class TestCalc:
    datas: list = get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, expected", get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
    def test_add(self, a, b, expected):
        result = self.calc.add(a, b)
        assert expected == result

    @pytest.mark.parametrize("a, b, expected", get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
    def test_div(self, a, b, expected):
        if b == 0:
            try:
                self.calc.div(a, b)
            except ZeroDivisionError as e:
                print("Divisor should not be zero")
        else:
            result = self.calc.div(a, b)
            assert expected == result

    # def test_add1(self):
    #     datas = [[1, 1, 2], [100, 400, 500], [1, 0, 1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])

    # def test_div(self):
    #     datas = [[1, 1, 1], [100, 400, 500], [1, 0, 1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.div(data[0], data[1])
