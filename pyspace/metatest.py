#!/usr/bin/python3
from inheritMeta import submeta 

def metaact():
    print('Call meta')
    a=submeta(12)
    a.checkbase()
    print(a.members)

def main():
    print('invoke metatest')
    metaact()

if __name__ == "__main__":
    main()
