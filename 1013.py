# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:29:25 2017

@author: dell
"""

def a():
    for i in range(3,10000,2):
        yield i

def b(n):
    return lambda x : x%n!=0

def c():
    yield 2
    it = a()
    while True:
         i = next(it)
         yield i
         it = filter(b(i),it)
    

if __name__ == '__main__':
    count = map(int,input().split())
    count=list(count)
    it = c()
    num = []
    for i in range(0,count[0]-1):
        i = next(it)
    for i in range(count[0],count[1]+1):
        i = next(it)
        num.append(i)
    for i in range(0,count[1]-count[0]+1):
        if i == count[1]-count[0]:
            print(num[i],end='')
        elif (i+1) %10 !=0:
            print(num[i],end=' ')
        else:
            print(num[i])
        
    