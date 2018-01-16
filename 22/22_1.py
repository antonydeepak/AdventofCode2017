from sys import stdin

def is_infected(grid, cur):
    return True if (cur in grid and grid[cur]=='#') else False

def flip_infection(grid, cur):
    grid[cur] = ('.' if (cur in grid and grid[cur]=='#') else '#')
    return True if (grid[cur] == '#') else False

def move(grid, cur, orientation):
    x,y = cur
    xo,yo = orientation
    return (x+xo,y+yo)

def rotate_right(cur):
    return (cur[1],-1*cur[0])

def rotate_left(cur):
    return (-1*cur[1],cur[0])

def pretty_print(grid, m, n):
    for i in range(m):
        for j in range(n):
            print(grid[(i,j)], end=' ')
        print()

if __name__ == '__main__':
    grid = {}

    i = 0
    for line in stdin:
        for j,v in enumerate(line.strip()):
            grid[(i,j)] = v
        i += 1

    m = i
    n = (j+1)
    cur = (m//2,n//2)
    orientation = (-1,0)
    iterations = 10000
    # iterations = 70
    infected = 0
    for _ in range(iterations):
        orientation = rotate_right(orientation) if is_infected(grid, cur) else rotate_left(orientation)
        infected += int(flip_infection(grid, cur))
        cur = move(grid, cur, orientation)

    print(infected)