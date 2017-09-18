# -*- coding: utf-8 -*-

def a(n):
    for i in range(3,n+1,2):
        yield i
        
def b(i): #筛选函数
    return lambda x:x%i!=0

def c(it):
    yield 2
    while True:
        i = next(it)
        yield i
        it = filter(b(i),it)
    
if __name__ =='__main__':
    n=int(input())
    
    l = list(c(a(n)))
    count=0
    for i in range(0,len(l)-1):
        if l[i+1]-l[i]==2:
            count+=1
    print(count)