#! /bin/env python
# -*- coding: utf-8 -*-
import itertools
def pi(N):
    sum = 0
    pn = itertools.cycle([4,-4])
    odd = itertools.count(1,2)
    for n in range(N):
        sum = sum + next(pn)/next(odd)
    return sum
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

        

   
 



