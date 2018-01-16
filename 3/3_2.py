from sys import stdin

def within_bounds(n, i):
    return (i>=0 and i<n)

# Spits out the matrix. Take the answer from it. There could be a better implementation too
def spiral(num):
    n = 1
    v = 1
    grid = [[1]]
    while v<num:
        n += 2

        # create new grid
        temp = []
        for _ in range(n):
            temp.append([0]*n)

        # copy value from previous grid
        pn = n-2
        a = 1
        for i in range(pn):
            b = 1
            for j in range(pn):
                temp[a][b] = grid[i][j]
                b += 1
            a += 1
        grid = temp

        # compute
        a = n-1
        b = n-1
        i = a-1
        j = b
        while i>=0:
            sum = 0
            for ii in range(-1, 2):
                for ji in range(-1, 2):
                    if (within_bounds(n, i+ii) and within_bounds(n, j+ji)):
                        sum += grid[i+ii][j+ji]
            grid[i][j] = sum
            i -= 1

        i = 0
        j = b-1
        while j>=0:
            sum = 0
            for ii in range(-1, 2):
                for ji in range(-1, 2):
                    if (within_bounds(n, i+ii) and within_bounds(n, j+ji)):
                        sum += grid[i+ii][j+ji]
            grid[i][j] = sum
            j -= 1

        i = 1
        j = 0
        while i<n:
            sum = 0
            for ii in range(-1, 2):
                for ji in range(-1, 2):
                    if (within_bounds(n, i+ii) and within_bounds(n, j+ji)):
                        sum += grid[i+ii][j+ji]
            grid[i][j] = sum
            i += 1

        i = a
        j = 1
        while j<n:
            sum = 0
            for ii in range(-1, 2):
                for ji in range(-1, 2):
                    if (within_bounds(n, i+ii) and within_bounds(n, j+ji)):
                        sum += grid[i+ii][j+ji]
            grid[i][j] = sum
            j += 1

        v = grid[a][b]

    return grid, n

if __name__ == '__main__':
    for line in stdin:
        g,n = spiral(int(line.strip()))
        for i in range(n):
            for j in range(n):
                print(g[i][j], end=' ')
            print()