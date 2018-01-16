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

def to_dense(sparse):
    assert(len(sparse)==256)
    dense = [0]*16

    for i in range(16):
        for j in range(16):
            dense[i] ^= sparse[i*16+j]
    
    return dense

def _knot_hash(l, n, steps):
    steps.extend([17, 31, 73, 47, 23])
    cur = 0
    skip = 0
    for _ in range(64):
        for step in steps:
            reverse(l, n, cur, step)
            cur = (cur+step+skip)%n
            skip += 1
    sparse_hash = l
    dense_hash = to_dense(sparse_hash)

    return ''.join([f'{v:02x}' for v in dense_hash])


def to_ascii(s):
    ascii = []
    for c in s:
        ascii.append(ord(c))
    return ascii

def knot_hash(key):
    l = list(range(0, 256))
    n = len(l)
    return _knot_hash(l, n, to_ascii(key))