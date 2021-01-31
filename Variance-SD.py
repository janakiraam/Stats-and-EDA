# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:15:51 2021

@author: I340968
"""

#Range

# The numpy.ptp() function returns the range (maximum-minimum) of values along an axis.

import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5], [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
print(A)
B=A.T
print("\n \n")
print("################# Transpose ###########################")
print("\n \n")
print(B)
a= np.ptp(B,axis=0)
print("\n \n",a)
a1=np.ptp(B)
print(a1)


#Quartile
#Ref: https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5], [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
B=A.T

print(B)
print("\n\n")
a=np.percentile(B,27,axis=0, interpolation='lower')
b=np.percentile(B,25,axis=1, interpolation='lower')
c=np.percentile(B,75,axis=0, interpolation='lower')
d=np.percentile(B,50,axis=0, interpolation='lower')
print(a)

print(b)

print(c)

print(d)


#Variance
import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5],
  [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
B=A.T
a = np.var(B,axis=0)
b = np.var(B,axis=1)
print(a)

print(b)

#Standard deviation
import numpy as np
A=np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5],
  [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
B=A.T
a = np.std(B,axis=0)
b = np.std(B,axis=1)
print(a)

print(b)