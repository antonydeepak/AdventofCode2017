from sys import stdin
import re

def parent(node, P):
    if node not in P:
        return node

    p = node
    while P[p] != p:
        p = P[p]
    return p

# Use a union find approach
if __name__ == '__main__':
    P = {}

    for line in stdin:
        groups = line.split('->')
        node,weight = groups[0].split()
        weight =  re.match('\((\d+)\)', weight).groups()[0]
        if node not in P:
            P[node] = node
        if len(groups)>1:
            group = groups[1]
            children = [token.strip() for token in group.split(', ')]
            for child in children:
                P[child] = node

    print(parent(list(P.values())[0], P))