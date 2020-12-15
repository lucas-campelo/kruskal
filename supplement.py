class Node:
    def __init__(self, key):
        self.root = self
        self.key = key

class Edge:
    def __init__(self, endpointA, endpointB, weight):
        self.endpointA = endpointA
        self.endpointB = endpointB
        self.weight = weight

def union(A, B):
    if A is B:
        return
    find_root(A).root = find_root(B)

def find_root(A):
    if A.root is A:
        return A
    return find_root(A.root)
