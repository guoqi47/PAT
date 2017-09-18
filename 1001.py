# -*- coding: utf-8 -*-

#给两个数字加千分位符
#1最简单

#if __name__ =='__main__':
#    a =[int(i) for i in input().split()]
#    b=sum(a)
#    print(format(b,','))


#2倒置遍历
def formatNum(num):
    num = str(num)
    count=0
    result=''
    for i in num[::-1]:
        result+=i
        count+=1
        if count%3==0 and count!=len(num):
            result+=','
    result=result[::-1]
    if result[0]=='-' and result[1]==',': #删去-后的，
        result=result[0]+result[2::]
                
            
    return result
    
if __name__ =='__main__':
    a =[int(i) for i in input().split()]
    b=sum(a)
    print(formatNum(b))
    