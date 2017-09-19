# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:47:33 2017

@author: dell
"""

if __name__ == '__main__':
    result = []
    a = [int(i) for i in input().split()]
    
    for i in range(0,len(a),2):
        if a[i]==0 :
            result.append(0)
            result.append(0)
        elif a[i+1]!=0:
            result.append(a[i]*a[i+1])
            result.append(a[i+1]-1)
            
    for i in range(0,len(result)):
        if i != len(result)-1:
            print(result[i],end=" ")
        else:
            print(result[i],end="")
        
        