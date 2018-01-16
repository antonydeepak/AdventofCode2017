# Implement the requirements from problem statement

from sys import stdin

def find_next(i, shift, n):
    return (i+shift)%n

def captcha(sequence):
    n = len(sequence)

    sum = 0
    for i in range(n):
        if (sequence[i] == sequence[find_next(i, 1, n)]):
            sum += int(sequence[i])
    return sum


for line in stdin:
    print(captcha(line.strip()))