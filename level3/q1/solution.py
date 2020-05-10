#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def solution(x, y):
    x = long(x)
    y = long(y)
    gen = 0
    while min(x, y) != 1:
        if x > y:
            gen += x // y
            x %= y
        elif x < y:
            gen += y // x
            y %= x
        else:
            return 'impossible'
    gen += max(x, y) - min(x, y)
    return str(gen)


print(solution(4, 7))
