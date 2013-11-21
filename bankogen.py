#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Genererer bankoplader som din mor lavede dem.

Kald programmet uden argumenter i samme mappe som filen "skabelon.svg" og gem
i en svg-fil.
"""

import itertools
import random


# Slam begynder her.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0"

banko_poss = list(itertools.product(range(9), range(3)))

def alphatobanko():
    a = {}
    i = 0
    for y in range(3):
        for x in range(9):
            a[(x, y)] = alphabet[i]
            i += 1
    return a

def generate_bankoplade():
    poss = []
    yxs = {}
    for y in range(3):
        yxs[y] = []
    for x in range(9):
        ys = []
        for i in range(3):
            if len(yxs[i]) < 5:
                ys.append(i)
        random.shuffle(ys)
        y = ys[0]
        poss.append((x, y))
        yxs[y].append(x)
    for y in range(3):
        xs = range(9)
        ts = yxs[y]
        for t in ts:
            xs.remove(t)
        random.shuffle(xs)
        xs = xs[:5 - len(ts)]
        for x in xs:
            poss.append((x, y))

    banko = [None for _ in range(9)]
    xs = range(9)
    random.shuffle(xs)
    for x in xs:
        col = []
        banko[x] = col
        nns = 0
        for y in range(3):
            if (x, y) in poss:
                col.append(True)
                nns += 1
            else:
                col.append(None)
        ns = range(10)
        random.shuffle(ns)
        ns = ns[:nns]
        ns.sort()
        j = 0
        for i in range(3):
            if col[i]:
                col[i] = ns[j] + 10 * x
                j += 1
    return banko

def make_banko_svg():
    atb = alphatobanko()
    with open('skabelon.svg') as f:
        bt = f.read()

    for _ in range(4):
        banko = generate_bankoplade()
        for x in range(9):
            for y in range(3):
                v = banko[x][y]
                a = 'X' + atb[(x, y)]
                if v is None:
                    bt = bt.replace(a, '', 1)
                else:
                    bt = bt.replace(a, '%02d' % v, 1)
    return bt
    
if __name__ == '__main__':
    print make_banko_svg()
