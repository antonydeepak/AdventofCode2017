def toHash(banks):
   return ''.join(map(str, banks)) 

def redistribution(banks):
    n = len(banks)
    patterns = {}
    pattern = toHash(banks)
    j = 0

    while pattern not in patterns:
        patterns[pattern] = j
        max_bank = max(banks)
        m = banks.index(max_bank)
        banks[m] = 0
        inc = max_bank//n
        for i in range(n):
            banks[i] += inc
        inc = max_bank%n
        i = m+1
        while inc>0:
            banks[i%n] += 1
            i += 1
            inc -= 1
        pattern = toHash(banks)
        j += 1

    return (j - patterns[pattern])

if __name__ == '__main__':
    #input for in the question is pretty bad, hence made it into a list
    print(redistribution([0, 2, 7, 0]))
    print(redistribution([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]))