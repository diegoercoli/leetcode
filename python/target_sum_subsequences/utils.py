from symtable import Class

import numpy as np
def take_solution(matrix, i, j):
    n, m = np.shape(matrix)
    if 0 <= i < n and 0 <= j < m:
        return matrix[i, j]
    else:
        return set()

class Subsolution:
    def __init__(self, v=None):
        if v is None:
            self.items = []
        else:
            self.items = list(v)

    #def union(self, other):
     #   self.items.union(other.items)

    def add(self, item):
        self.items.append(item)
        self.items.sort() #modify list in place

    def __eq__(self, other):
        if not isinstance(other, Subsolution):
            return False
        if len(self.items) != len(other.items):
            return False
        for i in range(len(self.items)):
            if self.items[i] != other.items[i]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.items))


    def __str__(self):
        return str(self.items)

    def copy(self):
        return Subsolution(self.items)
