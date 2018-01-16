from sys import stdin

def checksum(matrix):
    sum = 0

    for _ in matrix:
        row = list(sorted(map(int, _.split())))
        n = len(row)
        for i in range(n):
            for j in range(i+1, n):
                if (row[j]%row[i] == 0):
                    sum += row[j]//row[i]
                    break
            else:
                continue
            break

    return sum

if __name__ == '__main__':
    matrix = []
    for line in stdin:
        matrix.append(line)
    print(checksum(matrix))