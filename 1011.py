# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:40:09 2017

@author: dell
"""


if __name__ == '__main__':
    a = int(input())
    num=[]
    for i in range(1,a+1):
        num.append(input().split())
    for n in range(1,len(num)+1):
        b =[int(i) for i in num[n-1]]
        s = 'Case #'+repr(n)+': '+repr(b[0]+b[1]>b[2]).lower() #注意变换成小写
        print(s)