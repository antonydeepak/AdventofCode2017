from sys import stdin

def dec(i, n):
    return (i-1) if (i-1>=0) else (n-1)

def inc(i, n):
    return (i+1) if (i+1<n) else 0

def reverse(l, n, si, step):
    operations = (step)//2
    ei = (si+step-1)%n
    for _ in range(operations):
        l[si],l[ei] = l[ei],l[si]
        si = inc(si, n)
        ei = dec(ei, n)
    
def knot_hash(l, n, steps):
    cur = 0
    skip = 0

    for step in steps:
        reverse(l, n, cur, step)
        cur = (cur+step+skip)%n
        skip += 1

if __name__ == '__main__':
    end = 256
    l = list(range(0, end))
    n = len(l)
    steps = [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]

    knot_hash(l, n, steps)

    print(l[0]*l[1])