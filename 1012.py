# -*- coding: utf-8 -*-
def A1(a):
    result=[i for i in a if i%5==0 and i%2==0]
    if len(result)==0:
        print('N',end=' ')
    else:
        print(sum(result),end=' ')
    

def A2(a):
    result=[i for i in a if i%5==1]
    a=0
    if len(result)==0:
        print('N',end=' ')
    else:
        for i in range(0,len(result)):
            if i%2==0:
                a+=result[i]
            else:
                a-=result[i]
        print(a,end=' ')

def A3(a):
    result=[i for i in a if i%5==2]
    if len(result)==0:
        print('N',end=' ')
    else:
        print(len(result),end=' ')
    
def A4(a):
    result=[i for i in a if i%5==3]
    if len(result)==0:
        print('N',end=' ')
    else:
        print(sum(result)/len(result),end=' ')

def A5(a):
    result=[i for i in a if i%5==4]
    if len(result)==0:
        print('N',end=' ')
    else:
        print(sorted(result)[len(result)-1],end='') #sorted默认从小到大

if __name__ == '__main__':
    a = [int(a) for a in input().split()]
    A1(a)
    A2(a)
    A3(a)
    A4(a)
    A5(a)