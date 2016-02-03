#!/usr/bin/python3
import sys


def rangecalc(data,size):
    x = {}
    for i in range(size):
        print(data[i])
        x[i]=data[i]
    print(x)

def expmod(a,b,c):
    x=1
    while(b>0):
        if (b&1==1):
            x = (x*a)%c
        a = (a*a)%c
        b =b>>1
    return x

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    print(expmod(a,b,c))
    a = [1,2,3,4,45,5]
    rangecalc(a,6)

if __name__=='__main__':
    main()
