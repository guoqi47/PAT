# -*- coding: utf-8 -*-

if __name__ =='__main__':
    a = input()
    a = [int(i) for i in a]
    
    if len(a)==3:
        for i in range(0,a[0]):
            print('B',end='')
        for i in range(0,a[1]):
            print('S',end='')
        for i in range(0,a[2]):
            print(i+1,end='')
    elif len(a)==2:
        for i in range(0,a[0]):
            print('S',end='')
        for i in range(0,a[1]):
            print(i+1,end='')
    elif len(a)==1:
        for i in range(0,a[1]):
            print(i+1,end='')