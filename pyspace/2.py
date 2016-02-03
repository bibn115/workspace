#!/usr/bin/python3
import sys
import math
import utility


def generator(va):
    k = 1
    while k*k < va:
        if(va%k == 0):
            yield(k*k)
        k += 1
    if(k*k == va):
        yield(k*k)

def dummy(n):
    print('dummy')
    utility.utilitytest(4)

def listcomp(n):
    factors = [k for k in range(1,n+1) if n%k==0]
    print(factors)

def setcomp(n):
    factors = {k*k for k in range(1,n+1) if n%k==0}
    print(factors)

def gencomp(n):
    total = sum(k*k for k in range(1,n+1))
    print(total)

def tuplepairs(n):
    total = []
    for i in range(n,n+50):
        total.append(divmod(i,3) )
    print(total)

def main():
    func = int(sys.argv[1])
    n = int(sys.argv[2])
    
    options = { 
            0: listcomp,
            1: dummy,
            2: setcomp,
            3: gencomp,
            4:tuplepairs,
            5:generator}

    options[func](n)
    print(list(generator(n)))

if __name__=='__main__':
    main()
