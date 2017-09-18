# -*- coding: utf-8 -*-



if __name__ =='__main__':
    grade=[]
    count = int(input())
    for i in range(0,count):
        grade.append(input().split())
    grade.sort(key=lambda d:int(d[2]))
    
    print(grade[len(grade)-1][0]+' '+ grade[len(grade)-1][1])
    print(grade[0][0]+' '+ grade[0][1])