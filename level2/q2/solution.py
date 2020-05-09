#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def solution(n, b):
    graph = [n]
    while True:
        x, y, z = get_xyz(n, b)
        if z in graph:
            break
        graph.append(z)
        print(graph)
        n = z

    return len(graph) - graph.index(z)


def get_xyz(n, b):
    k = len(n)
    x = ''.join(sorted(n, reverse=True))
    y = ''.join(sorted(n))
    z = base_b(int(x, b) - int(y, b), b).zfill(k)
    return x, y, z


def base_b(n, b):
    e = n // b
    q = n % b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return base_b(e, b) + str(q)
