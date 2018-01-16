from sys import stdin

def solve(road, pos):
    directions = [
        (1,0),#down
        (0,-1),#left
        (-1,0),#up
        (0,1)#right
    ]

    direction = (1,0)
    path = []

    while pos in road:
        if road[pos] == '+':
            for d in directions:
                if d != mul_tuple(direction, -1):
                    if (add_tuple(pos,d) in road):
                        direction = d
                        break
        if road[pos].isalpha():
            path.append(road[pos])
        pos = add_tuple(pos,direction)

    return ''.join(path)

def mul_tuple(a,factor):
    return tuple(factor*v for v in a)

def add_tuple(a, b):
    return tuple(sum(v) for v in zip(a,b))

if __name__ == '__main__':
    road = {}
    for i,line in enumerate(stdin):
        for j,cell in enumerate(line):
            v = cell.strip()
            if v:
                road[(i,j)] = v
    pos = min(road.keys())
    print(solve(road, pos))
