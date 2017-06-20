# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:28:41 2016

@author: eowfenth
"""

import numpy as np

# Escalares são tratados como zero-dimensional
#x = np.array(42)
#print("x:", x)
#print("Type:", type(x), x.dtype)
#print("Dim:", np.ndim(x))
#
#y = np.array([1,2,3,4,5,6,7])
#z = np.array([1.4,5.3,5.2])
#print("y", y, "z", z)
#print("Type:", type(y), y.dtype, type(z), z.dtype)
#print("Dim:", np.ndim(y), np.ndim(z))
#
#p = np.array([[15.2, 12.3],[1,2]])
#print("x:", p)
#print(p1)
#print("Type:", type(p), p.dtype)
#print("Dim:", np.ndim(p))


B = np.array([ [[111, 112], [222, 223]],
               [[333, 334], [444, 445]],
               [[555, 556], [666, 667]] ])

#print("B", B[2, 1, 0])
#print(B.ndim)
#print(B.shape)
#B.shape = (3, 2, 2)

C = np.array([ [111, 112], [222, 223]])

D = np.array([[1, 2, 5], [2,4,5]])
E = np.array([ [[1,1,1], [1,1,2], 
               [1,2,3] ]])
F = np.array([[1,1,3,4],[1,2,5,5]])

#print(np.shape(C))
C.shape = (1,4)

mb = np.array([])

# 223, 445, 667
i = 0
for b in B[:3]:
    print(b)
    print("iteration:", i)
    i += 1
    
    

old = np.array([1, 2, 3, 4])
new = np.append(old, 5)
print(old)
# [1, 2, 3, 4]
print(new)
# [1, 2, 3, 4, 5]
new = np.append(new, [6, 7])
print(new)