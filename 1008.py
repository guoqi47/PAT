# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:46:32 2017

@author: dell
"""
#注意，m可能大于n，所以要进行求余
if __name__ == '__main__':
#    a = input()
    a = [int(i) for i in input().split()]
    n = a[0]
    m = a[1]%n
    b = input().split()
    for i in range(1,m+1):
        b.append(0)
    for i in range(1,n+1):
        b[n+m-i] = b[n-i]
    for i in range(1,m+1):
        b[i-1]=b[n+i-1]
    for i in range(1,n+1):
        if i != n:
            print(b[i-1],end=" ")
        else:
            print(b[n-1],end="")
        