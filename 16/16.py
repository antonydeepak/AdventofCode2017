from collections import deque

def spin(P, x):
    n = len(P)
    rotations = x%n
    for _ in range(rotations):
        v = P.pop()
        P.appendleft(v)

def Ex(P, si, ei):
    P[si],P[ei] = P[ei],P[si]

def swap(P, s, e):
    si = P.index(ord(s)-97)
    ei = P.index(ord(e)-97)
    Ex(P, si, ei)

def pretty_print(P):
    print([chr(i+97) for i in P])

def pretty_inverted_print(Pi):
    for i,v in enumerate(Pi):
        print(chr(i+97), v)

if __name__ == '__main__':
    P = deque(range(0,16))

    ops = [
        's1',
        'x3/4',
        'pe/b'
    ]

    # accidently combined 1 & 2 but should be pretty simple to figure out
    ops = input().split(',')
    reps = 1000000000
    # for problem 2simulation shows that patterns repeat after every 60 iterations.
    required = reps%60
    for i in range(required):
        for op in ops:
            if op.startswith('s'):
                spin(P, int(op[1:]))
            elif op.startswith('x'):
                si,ei = list(map(int, op[1:].split('/')))
                Ex(P, si, ei)
            else:
                s,e = op[1:].split('/')
                swap(P, s, e)

        ans = ''.join([chr(i+97) for i in P])

    print(ans)