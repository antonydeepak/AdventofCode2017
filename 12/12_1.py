from sys import stdin

class Color:
    White, Black = range(2)

def connected_components(G, vertex):
    cc = []
    c = {}
    for v in G:
        c[v] = Color.White

    dfs_visit(G, vertex, c, cc)

    return cc

def dfs_visit(G, root, c, cc):
    c[root] = Color.Black
    cc.append(root)

    for child in G[root]:
        if c[child] == Color.White:
            dfs_visit(G, child, c, cc)

def get_node(G, node):
    if node not in G:
        G[node] = []
    return G[node]

if __name__ == '__main__':
    G = {}
    for line in stdin:
        node,children = line.split(' <-> ')
        node = int(node)
        children = [int(v.strip()) for v in children.split(',')]

        adjacents = get_node(G, node)
        adjacents.extend(children)

        for child in children:
            adjacents = get_node(G, child)
            adjacents.append(node)

    print(len(connected_components(G, 0)))