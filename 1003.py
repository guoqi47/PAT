# -*- coding: utf-8 -*-
#题意不好理解

def a(str):
    f1=False
    f2=False
    f3=False
    for i in str:
        if not(i=='P' or i=='A' or i=='T'):
            return False
        elif i=='P':
            f1=True
        elif i=='A':
            f2=True
        elif i=='T':
            f3=True
        if (f1 and f2 and f3):
            return True


if __name__ =='__main__':
    count = int(input())
    for i in range(0,count):
        if a(input()):
            print('YES')
        else:
            print('NO')
    
    
    
    