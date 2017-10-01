# -*- coding: utf-8 -*-

def a(i):
    week = ord(num[0][i])-ord('A')
    if week == 0:
        print('MON',end=' ')
    elif week == 1:
        print('TUE',end=' ')
    elif week == 2:
        print('WED',end=' ')
    elif week == 3:
        print('THU',end=' ')
    elif week == 4:
        print('FRI',end=' ')
    elif week == 5:
        print('SAT',end=' ')
    else:
        print('SUN',end=' ')

def b(i):
    hour = num[0][i]
    if hour in list(range(1,10)):
        print(repr(i).zfill(2)+':',end='')
    else:
        print(repr(ord(num[0][i])-ord('A')+10 )+ ':',end='')
    
def c(i):
    print(str(i).zfill(2))

if __name__ =='__main__':
    num = []
    index=[]
    for i in range(0,4):
        num.append(input())
    for i in range(0,min(len(num[0]),len(num[1]))):
        if num[0][i]==num[1][i] and num[1][i].isalpha():
            index.append(i)
    for i in range(0,min(len(num[2]),len(num[3]))):
        if num[2][i]==num[3][i] and num[3][i].isalpha():
            index.append(i)
    a(index[0])
    b(index[1])
    c(index[2])
        