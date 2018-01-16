from sys import stdin
import re

# not a good implementation. You have to eyeball the answer from output
imbalance = 0
def find_weight(G, root):
    global imbalance
    weight = G[root][0]
    children = G[root][1]
    children_weights = []
    for child in children:
        children_weights.append(find_weight(G, child))
    n = len(children_weights)
    if imbalance==0 and n>0:
        pw = children_weights[0][1]
        for i in range(1, n):
            cw = children_weights[i][1]
            if pw != cw:
                imbalance = abs(pw-cw)
                break
            pw = cw
        if imbalance>0:
            print(children_weights)
            print([G[child[0]] for child in children_weights])


    weights = [child[1] for child in children_weights]
    return (root, weight+sum(weights))

if __name__ == '__main__':
    G = {}
    root = 'hmvwl' #from 7.py answer
    #root = 'tknk'
    for line in stdin:
        groups = line.split('->')
        node,weight = groups[0].split()
        weight =  int(re.match('\((\d+)\)', weight).groups()[0])
        G[node] = (weight, [])
        if len(groups)>1:
            group = groups[1]
            children = [token.strip() for token in group.split(', ')]
            for child in children:
                G[node][1].append(child)
    #print(P)
    find_weight(G, root)
    print(imbalance)