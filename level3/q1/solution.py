#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def solution(x, y):
    x = long(x)
    y = long(y)
    fib = [1, 2]
    mx = max(x, y)
    fibonacci(mx, fib)
    print(fib)
    idx = next(index for index, value in enumerate(fib) if value >= mx)
    # print(fib, idx)
    cmbs = [(1, 1)]
    create_tree((1, 1), 0, idx, cmbs)
    if (x, y) in cmbs:
        return str(idx)
    else:
        return 'impossible'


def create_tree((m, f), h, idx, cmbs):
    if h == idx:
        return
    first, second = reproduce(m, f)
    cmbs.append(first)
    cmbs.append(second)
    create_tree(first, h + 1, idx, cmbs)
    create_tree(second, h + 1, idx, cmbs)


def reproduce(m, f):
    return (m + f, f), (m, m + f)


def fibonacci(h, fib):
    if len(fib) == h:
        return
    fib.append(fib[-2] + fib[-1])
    fibonacci(h, fib)
    return
