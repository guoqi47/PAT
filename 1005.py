# -*- coding: utf-8 -*-
#将给出的数保存在数组a中，依次遍历求出他们所覆盖的数保存在b中，
#最后比较，如果存在a中有b中没有的数，即为关键数保存在数组c中，
#最后对c数组进行排序。

def de(s):
    return lambda x:not(x in s)


if __name__ =='__main__':
    count = int(input())
    b=[] #新list
    a = input().split()
    a=[int(i) for i in a]
    
    for i in a:
        while i!=1:
            if i % 2==0:
                i=i/2
            else :
                i= (3*i+1)/2
            b.append(i)
    c=list(filter(de(b),a))
    c=sorted(c,reverse=True) #去掉末尾空格
    
    for i in range(0,len(c)):
        if i !=len(c)-1:
            print(c[i],end=' ')
        else:
            print(c[i])
        
    
    
   