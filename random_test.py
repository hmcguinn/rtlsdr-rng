#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rng import rtlRandom 


r = rtlRandom() 

for i in range(10000): 
    print(r.random())
