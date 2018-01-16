if __name__ == '__main__':
    seedA = 516
    seedB = 190
    mulA = 16807
    mulB = 48271
    cap = 2147483647

    curA = seedA
    curB = seedB
    count = 0
    for _ in range(40000000):
        curA = (curA*mulA)%cap
        curB = (curB*mulB)%cap
        count += int((curA&65535) == (curB&65535))
    print(count)