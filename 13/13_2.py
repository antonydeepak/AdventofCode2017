from sys import stdin

def delay(firewall):
    delay = 0
    while (True):
        for i in range(len(firewall)):
            level,depth = firewall[i]
            if intersects(delay+level, depth):
                break
        else:
            return delay
        delay += 1 

#Pray
def intersects(level, depth):
    assert(depth>0)

    return (level%(2*(depth-1)) == 0)

if __name__ == '__main__':
    firewall = []
    for line in stdin:
        level,depth = list(map(int, line.split(': ')))
        firewall.append((level, depth))

    print(delay(firewall))

