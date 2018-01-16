def spinlock(spins, times):
    i = 0
    n = 1
    ans = -1

    for v in range(1, times+1):
        i = ((i+(spins%n))%n)+1
        if i==1:
            ans = v
        n += 1

    assert(ans != -1)
    return ans

if __name__ == '__main__':
    times = 50000000
    #times = 2017
    print(spinlock(376, times))