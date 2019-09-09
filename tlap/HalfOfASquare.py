#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:33:55 2019

@author: x1
PROBLEM: HALF OF A SQUARE
Write a program that uses only two output statements,
cout << "#" and cout << "\n", to produce a pattern of hash symbols
shaped like half of a perfect 5 x 5 square (or a right triangle)
"""
import numpy as np

for i in range(5):
    print('\n', end='')
    for j in range(i):
        print('#', end='')
              
