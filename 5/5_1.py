from sys import stdin

def jumps(l):
    n = len(l)
    ci = 0 # current index
    jumps = 0

    while ci>=0 and ci<n:
        j = l[ci]
        ni = ci+j
        l[ci] += 1
        ci = ni
        jumps += 1

    return jumps

if __name__ == '__main__':
    l = []
    for line in stdin:
        l.append(int(line.strip()))
    print(jumps(l))