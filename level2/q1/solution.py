#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def solution(h, q):
    size = get_tree_size(h)
    tree = {k: 0 for k in range(1, size + 1)}
    tree[size] = -1
    tree = draw_tree(size, h, tree)
    return [tree[x] for x in q]


def draw_tree(root, level, tree):
    if level == 1:
        return tree
    tree[root - 1] = root
    tree[root - get_tree_size(level) // 2 - 1] = root
    tree = draw_tree(root - 1, level - 1, tree)
    tree = draw_tree(root - get_tree_size(level) // 2 - 1, level - 1, tree)
    return tree


def get_tree_size(h):
    return sum([2 ** x for x in range(h)])

