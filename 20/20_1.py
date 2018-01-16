from sys import stdin
import re

def add_tuple(a, b):
    return tuple(sum(v) for v in zip(a,b))

def mul_tuple(a, factor):
    return tuple(factor*v for v in a)

def closest(particles):
    return particles.index(min(particles, key=lambda x: sum([abs(v) for v in x[0]])))

# Runs longer
if __name__ == '__main__':
    pattern = re.compile('p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>')

    particles = []
    for line in stdin:
        xp,yp,zp,xv,yv,zv,xa,ya,za = list(map(int, pattern.match(line).groups()))
        particles.append([(xp,yp,zp),(xv,yv,zv),(xa,ya,za)])
    
    best = closest(particles)
    best_count = 1
    step = 1
    best_until = 20000
    while best_count<best_until:
        for i,particle in enumerate(particles):
            position = particle[0]
            velocity = particle[1]
            acceleration = particle[2]

            new_velocity = add_tuple(velocity, mul_tuple(acceleration, step))
            particle[1] = new_velocity
            velocity = new_velocity

            new_position = add_tuple(position, mul_tuple(velocity, step))
            particle[0] = new_position

            # print(f'i:{i} p:{new_position}')
        
        new_best = closest(particles)
        if best != new_best:
            best = new_best
            best_count = 0 
        best_count += 1 if (new_best == best) else 0
    
    print(best)