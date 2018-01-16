from sys import stdin

def is_clean(grid, cur):
    if (cur in grid and grid[cur]!='.'):
        return False
    return True

def is_weak(grid, cur):
    if (cur in grid and grid[cur]=='w'):
        return True
    return False

def is_infected(grid, cur):
    if (cur in grid and grid[cur]=='#'):
        return True
    return False

def is_flagged(grid, cur):
    if (cur in grid and grid[cur]=='f'):
        return True
    return False

def change_state(grid, cur):
    if is_clean(grid, cur):
        grid[cur] = 'w'
    elif is_weak(grid, cur):
        grid[cur] = '#'
    elif is_infected(grid, cur):
        grid[cur] = 'f'
    elif is_flagged(grid, cur):
        grid[cur] = '.'
    else:
        assert(True==False)

    return True if (grid[cur] == '#') else False

def rotate_right(orientation):
    return (orientation[1],-1*orientation[0])

def rotate_left(orientation):
    return (-1*orientation[1],orientation[0])

def reverse(orientation):
    return (-1*orientation[0],-1*orientation[1])

def move(grid, cur, orientation):
    x,y = cur
    xo,yo = orientation
    return (x+xo,y+yo)

def pretty_print(grid, m, n):
    for i in range(m):
        for j in range(n):
            print(grid[(i,j)], end=' ')
        print()

def get_orientation(grid, cur, orientation):
    if is_clean(grid, cur):
        return rotate_left(orientation)
    elif is_weak(grid, cur):
        return orientation
    elif is_infected(grid, cur):
        return rotate_right(orientation)
    elif is_flagged(grid, cur):
        return reverse(orientation)
    else:
        assert(True==False)

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
    iterations = 10000000
    # iterations = 100
    infected = 0
    for _ in range(iterations):
        orientation = get_orientation(grid, cur, orientation)
        infected += int(change_state(grid, cur))
        cur = move(grid, cur, orientation)

    print(infected)