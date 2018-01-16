from sys import stdin
import re

def rotation_0(m, n):
    return m

def flip(m, n):
    matrix = [[c for c in m[i]] for i in range(n)]
    offset = n//2
    for k in range(offset):
        for i in range(n):
            t = matrix[i][k]
            matrix[i][k] = matrix[i][n-k-1]
            matrix[i][n-k-1] = t
    return matrix

def invert(m, n):
    matrix = [[c for c in m[i]] for i in range(n)]
    offset = n//2
    for k in range(offset):
        for i in range(n):
            t = matrix[k][i]
            matrix[k][i] = matrix[n-k-1][i]
            matrix[n-k-1][i] = t
    return matrix

def rotate_90(m, n):
    matrix = [[c for c in m[i]] for i in range(n)]
    offset = n//2
    for k in range(offset):
        for i in range(k, n-k-1):
            t1 = matrix[k][k+i]

            t2 = matrix[k+i][n-k-1]
            matrix[k+i][n-k-1] = t1
            t1 = t2

            t2 = matrix[n-k-1][n-k-i-1]
            matrix[n-k-1][n-k-i-1] = t1
            t1 = t2

            t2 = matrix[n-k-i-1][k]
            matrix[n-k-i-1][k] = t1
            t1 = t2

            matrix[k][k+i] = t1
    return matrix

def rotate_180(m, n):
    matrix = m
    for _ in range(2):
        matrix = rotate_90(matrix, n)
    return matrix

def rotate_270(m, n):
    matrix = m
    for _ in range(3):
        matrix = rotate_90(matrix, n)
    return matrix

def encode(matrix, n, startx=0, starty=0):
    h = 1 #sentry
    for i in range(startx, startx+n):
        for j in range(starty, starty+n):
            h <<= 1
            if matrix[i][j] == '#':
                h |= 1
    return h

def decode(pattern, n):
    matrix = []
    for i in range(n):
        row = ''
        for j in range(n):
            row = ('#' if (pattern & (1<<(i*n+j))) else '.') + row
        matrix.insert(0, row)
    return matrix

def preprocess(rules):
    patterns = {}

    for rule in rules:
        s,d = rule

        value = (encode(d, len(d)), len(d))
        normal = encode(s, len(s))
        patterns[normal] = value

        transforms = [flip, invert]
        rotations = [rotation_0, rotate_90, rotate_180, rotate_270]
        for rotation in rotations:
            key = encode(rotation(s, len(s)), len(s))
            assert((key not in patterns) or (value == patterns[key]))
            patterns[key] = value

            for transform in transforms:
                key = encode(transform(rotation(s, len(s)), len(s)), len(s))
                assert((key not in patterns) or (value == patterns[key]))
                patterns[key] = value

    return patterns

def process(matrix, n, startx, starty, patterns):
    key = encode(matrix, n, startx, starty) 
    assert(key in patterns)

    m,mn = patterns[key]
    return decode(m, mn)

def solve(matrix, patterns, iterations):
    m = matrix
    for _ in range(iterations):
        n = len(m)
        split = 2 if (n%2 == 0) else (3 if (n%3 == 0) else -1)
        assert(split != -1)

        size = (split+1)*(n//split)
        t = [[None]*(size) for __ in range(size)]
        tj = 0
        for j in range(0, n, split):
            ti = 0
            for i in range(0, n, split):
                startx = i
                starty = j
                #print(m, split, startx, starty)
                pm = process(m, split, startx, starty, patterns)
                for a in range(len(pm)):
                    ttj = tj
                    for b in range(len(pm)):
                        t[ti][ttj] = pm[a][b]
                        ttj += 1
                    ti += 1
                # print(t)
            tj += (split+1)
        m = t
        # print(m)

    count = 0
    for i in range(len(m)):
        count += sum([len([1 for e in row if e == '#']) for row in m[i]])
    return count

# Both the problems are here. Just the input varies
if __name__ == '__main__':
    matrix = ['.#.', '..#', '###']
    #iterations = 2
    #iterations = 5
    iterations = 18

    rules = []
    for line in stdin:
        s,d = list(map(lambda x: x.split('/'), line.rstrip().split(' => ')))
        rules.append((s,d))
    patterns = preprocess(rules)
    print(solve(matrix, patterns, iterations))