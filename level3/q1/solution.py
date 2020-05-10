#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def solution(x, y):
    x = long(x)
    y = long(y)
    gen = 0
    while (x, y) != (1, 1):
        if x > y:
            x -= y
            gen += 1
        elif x < y:
            y -= x
            gen += 1
        else:
            break
    return str(gen)

print(solution(2,1))
