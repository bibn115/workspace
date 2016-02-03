#!/usr/bin/python3
import sys
from CreditCard import CreditCard

def classtest(val):
    cc = CreditCard('John','1st bank','345 333 5566',1000)
    cc.charge(345)
    val = cc.get_balance()
    print(val)

def main():
    func = int(sys.argv[1])
    n = int(sys.argv[2])

    options = {
            0: classtest,
            }

    options[func](n)

if __name__=='__main__':
    main()

