#! /usr/bin/env python

from math import sqrt


def one():
    for i in range(10000):
        sqrt(16)

def two():
    for i in range(10000):
        16**0.5       

def three():
    for i in range(10000):    
        pow(16,.5)

one()
two()
three()