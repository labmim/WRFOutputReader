#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:15:54 2017

@author: eowfenth
"""

def CorrectNumberInFileName(index):
    if (index < 10):
        return "00" + str(index)
    elif (index >= 10 and index <= 99):
        return "0" + str(index)
    return str(index)