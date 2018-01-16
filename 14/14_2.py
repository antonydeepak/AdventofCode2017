from knothash import knot_hash

def convert_to_bool(n):
    bits = []
    for _ in range(128):
        bits.append(bool(n & 1))
        n >>= 1
    return list(reversed(bits))

def mark(grid, x, y, directions):
    grid[x][y] = False
    for direction in directions:
        pos_x = x+direction[0]
        pos_y = y+direction[1]
        if pos_x>=0 and pos_x<128 and pos_y>=0 and pos_y<128 and grid[pos_x][pos_y]:
            mark(grid, pos_x, pos_y, directions)

if __name__ == '__main__':
    key_string = 'oundnydw'
    #key_string = 'flqrgnkx'
    count = 0
    grid = []

    for i in range(128):
        key = f'{key_string}-{i}'
        row = int(knot_hash(key), 16)
        grid.append(convert_to_bool(row))
    assert(len(grid[31])==128)

    directions = [(-1,0), (0,-1), (0,1), (1,0)]
    for i in range(128):
        for j in range(128):
            if grid[i][j]:
                mark(grid, i, j, directions)
                count += 1

    print(count)