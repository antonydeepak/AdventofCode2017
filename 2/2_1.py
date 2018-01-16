# Implement the requirements from problem statement

from sys import stdin

def checksum(matrix):
    sum = 0
    for row in matrix:
        e = list(map(int, row.split()))
        sum += max(e)-min(e)
    return sum

if __name__ == '__main__':
    matrix = []
    for line in stdin:
        matrix.append(line)
    print(checksum(matrix))