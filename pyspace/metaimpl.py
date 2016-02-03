"""Sequence metaclass implementaiton trial"""
#!/usr/bin/python3

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Own collection of collections. Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Returns the element at index j of the sequence"""

    def __contains__(self, val):
        """Return true if the value is found in the sequence, false otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def index(self, val):
        """Returns the leftmost index in sequence for given value"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in the sequence")

    def count(self, val):
        """Returns number of elements which are equal to given value"""
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
        return k



