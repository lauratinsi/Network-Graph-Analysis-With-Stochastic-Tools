# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:48:33 2016

@author: lauratinsi
"""

import numpy as np 
import math as mt

A=[[1/2, 0, 0, 0, 0, 0, 0, 0, 0, 1/2],[0, 1/12, 1/3, 0, 1/4, 1/3, 0, 0, 0, 0],
   [0, 1/3, 1/12, 1/3, 1/4, 0, 0, 0, 0, 0],[0, 0, 1/3, 1/12, 1/4, 0, 0, 1/3, 0, 0],
[0, 1/4, 1/4, 1/4, 0, 1/4, 0, 0, 0, 0],[0, 1/3, 0, 0, 1/4, 1/12, 1/3, 0, 0, 0],
[0, 0, 0, 0, 0, 1/3, 2/3, 0, 0, 0],[0, 0, 0, 1/3, 0, 0, 0, 1/6, 1/2, 0],
[0, 0, 0, 0, 0, 0, 0, 1/2, 0, 1/2],[1/2, 0, 0, 0, 0, 0, 0, 0, 1/2, 0]];


def cal_theo(A):
    L=[]
    for j in range(0,len(A)):
           Q= np.array([[A[l][m] for l in range(0,len(A))] for m in range(0,len(A))])
           for l in range (0, len(A)):
               for m in range (0, len(A)):
                   Q[l][m]=A[l][m]
           for i in range(0, len(A)):
                   Q[i][j]= 0
           M =np.linalg.inv(np.eye(len(A))+np.dot(-1*np.eye(len(A)),Q))
           M_j=np.dot(M, np.transpose(np.ones(len(A))))
           sig_j=mt.sqrt(2*sum(M_j)-len(A)*(len(A)+1))
           L.append(sig_j)
    return L
       
print(cal_theo(A))

            
            
        
    