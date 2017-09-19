# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:31:59 2017

@author: dell
"""

if __name__ == '__main__':
    a = input().split()
    for i in range(len(a)-1,-1,-1):
        if i != 0:
            print(a[i],end=" ")
        else:
            print(a[0],end="")
        
    