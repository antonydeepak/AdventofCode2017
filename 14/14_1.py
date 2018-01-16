from knothash import knot_hash #from 10th day

def count_setbits(n):
    count = 0
    while (n):
        n &= (n-1)
        count += 1
    return count

if __name__ == '__main__':
    key_string = 'oundnydw'
    #key_string = 'flqrgnkx'
    count = 0
    for i in range(128):
        key = f'{key_string}-{i}'
        row = int(knot_hash(key), 16)
        count += count_setbits(row)
    print(count)