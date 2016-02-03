#!/usr/bin/python3
import sys


def fibonacci(x):
    a = 1
    b = 1
    next = a + b
    for i in range(x):
        yield a
        a = b
        b = next
        next = a + b

def factors(n):
    for k in range(1,n+1):
        if n%k==0:
            yield k

def rangeiter(inputsize):
    newlist = []
    for i in range(inputsize):
        var = int(input("Enter another value:---- "))
        newlist.append(var)
    print(newlist)

def main():
    store = []
    #inputsize = int(sys.argv[1])
    #rangeiter(inputsize)
    #for i in factors(50):
    #    store.append(i)
    #print(store)
    for i in fibonacci(40):
        store.append(i)
    print(store)

if __name__=='__main__':
    main()
