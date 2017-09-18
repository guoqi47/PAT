# -*- coding: utf-8 -*-

if __name__ =='__main__':
    a = input()
    num=0
    result=''
    for i in a:
        num+=int(i)
    for i in str(num):
        if i=='1':
            result+='yi '
        elif i=='2':
            result+='er '
        elif i=='3':
            result+='san '
        elif i=='4':
            result+='si '
        elif i=='5':
            result+='wu '
        elif i=='6':
            result+='liu '
        elif i=='7':
            result+='qi '
        elif i=='8':
            result+='ba '
        elif i=='9':
            result+='jiu '
        else:
            result+='ling '
            
    for i in range(0,len(result.rsplit())):
        if i!= len(result.rsplit())-1:
            print(result.rsplit()[i],end=' ')
        else:
            for i in result.rsplit()[i].split():
                print(i)
    