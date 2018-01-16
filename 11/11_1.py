from sys import stdin

def steps(path, directions):
    pos = [0, 0]
    for step in path:
        pos[0] += directions[step][0]
        pos[1] += directions[step][1]
    
    x = abs(pos[0])
    y = abs(pos[1])
    dxy = min(x, (y//1.5))
    dy = abs(y-dxy*1.5)//1.5
    dx = abs(x-dxy)//2
    return int(dx+dy+dxy)

if __name__ == '__main__':
    directions = {
        'n': (-2, 0),
        'ne': (-1, 1.5),
        'se': (1, 1.5),
        's': (2, 0),
        'sw': (1, -1.5),
        'nw': (-1, -1.5)
    }

    for line in stdin:
        path = line.strip().split(',')
        print(steps(path, directions))