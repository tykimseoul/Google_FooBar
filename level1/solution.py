#!/usr/local/bin/python
# -*- coding: utf-8 -*-


def solution(x):
    return ''.join([chr(122 - (d - 97)) if 97 <= d <= 122 else chr(d) for d in [ord(c) for c in x]])
