# -*- coding: utf-8 -*-




if __name__ =='__main__':
    a = [float(i) for i in input().split()]
    b = [float(i) for i in input().split()]
    c = a + b[1::]
    c[0] += b[0]
    num = len(c)
    for i in range(1,num-2,2):
        n = 1
        while (i+2*n)<num-1:
            if c[i] == c[i+2*n]:
                c[i+1] += c[i+2*n+1]
                del c[i+2*n]
                del c[i+2*n]
                num-=2
                c[0]-=1
            n+=1
    
    for i in range(0,len(c)):
        if i!=len(c)-1:
            print([str(c[i]),int(c[i])][int(c[i])==c[i]],end=' ')
        else:
            print([str(c[i]),int(c[i])][int(c[i])==c[i]],end='')
        
    