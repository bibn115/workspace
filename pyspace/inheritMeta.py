"""Implementing the abstract class"""

from metaimpl import Sequence

class submeta(Sequence):

    def __init__(self,value=0):
        self._value = value
        
    def checkbase(self):
        print('Calling from the inherited class')

    def __getitem__(self,j):
        self._value += 1
        return self._value

    def __len__(self):
        return len(self._value)


