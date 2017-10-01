# -*- coding: utf-8 -*-


if __name__ =='__main__':
    b=0
    c=0
    a = [int(i) for i in input().split()]
#    print(a[0])
#    a[0] = str(a[0])
#    print(a[0][0])
    a[0] = str(a[0])
    a[2] = str(a[2])
    for i in range(0,len(a[0])):
        if int(a[0][i])==a[1]:
            b=b*10+a[1]
    for i in range(0,len(a[2])):
        if int(a[2][i])==a[3]:
            c=c*10+a[3]
    print(b+c)
    