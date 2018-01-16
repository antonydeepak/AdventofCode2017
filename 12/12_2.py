from sys import stdin

class Color:
    White, Black = range(2)

def connected_components(G):
    c = {}
    for v in G:
        c[v] = Color.White

    count = 0
    for v in G:
        if c[v] == Color.White:
            dfs_visit(G, v, c)
            count += 1

    return count

def dfs_visit(G, root, c):
    c[root] = Color.Black

    for child in G[root]:
        if c[child] == Color.White:
            dfs_visit(G, child, c)

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

    print(connected_components(G))