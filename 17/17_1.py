def spinlock(spins, times):
    buffer = [0]
    i = 0
    n = 1
    for v in range(1, times+1):
        i = ((i+(spins%n))%n)+1
        buffer.insert(i, v)
        n += 1
        # print(buffer[0], buffer[1])
    return buffer

if __name__ == '__main__':
    #times = 50000000
    times = 2017
    buffer = spinlock(376, times)
    print(buffer[buffer.index(0)+1])