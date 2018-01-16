from sys import stdin

def scan(firewall):
    sev = 0
    for i in range(1, len(firewall)):
        level,depth = firewall[i]
        if intersects(level, depth):
            sev += level*depth
    return sev

def intersects2(level, depth):
    assert(depth>0)
    if depth == 1:
        return True

    collision_at = 0
    i = 1
    while collision_at<=level:
        if collision_at==level:
            return True
        collision_at = i*2*(depth-1)
        i += 1
    return False

def intersects(level, depth):
    assert(depth>0)

    return (level%(2*(depth-1)) == 0)

if __name__ == '__main__':
    firewall = []
    for line in stdin:
        level,depth = list(map(int, line.split(': ')))
        firewall.append((level, depth))

    print(scan(firewall))

