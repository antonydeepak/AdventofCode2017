from sys import stdin
import re

def add_tuple(a, b):
    return tuple(sum(v) for v in zip(a,b))

def mul_tuple(a, factor):
    return tuple(factor*v for v in a)

def closest(particles):
    return particles.index(min(particles, key=lambda x: sum([abs(v) for v in x[0]])))

def collisions(particles):
    particle_histogram = {}
    for i,particle in particles.items():
        position = particle[0]
        if not (position in particle_histogram):
            particle_histogram[position] = [0,[]]
        particle_histogram[position][0] += 1
        particle_histogram[position][1].append(i)
    
    colliding_partciles = []
    for particle in particle_histogram.values():
        if particle[0]>1:
            colliding_partciles.extend(particle[1])
    
    return colliding_partciles

# Runs longer
if __name__ == '__main__':
    pattern = re.compile('p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>')

    particles = {}
    for i,line in enumerate(stdin):
        xp,yp,zp,xv,yv,zv,xa,ya,za = list(map(int, pattern.match(line).groups()))
        particles[i] = [(xp,yp,zp),(xv,yv,zv),(xa,ya,za)]
    
    best = len(particles)
    best_count = 1
    step = 1
    best_until = 20000
    while best_count<best_until:
        for i,particle in particles.items():
            position = particle[0]
            velocity = particle[1]
            acceleration = particle[2]

            new_velocity = add_tuple(velocity, mul_tuple(acceleration, step))
            particle[1] = new_velocity
            velocity = new_velocity

            new_position = add_tuple(position, mul_tuple(velocity, step))
            particle[0] = new_position

            # print(f'i:{i} p:{new_position}')
        for i in collisions(particles):
            del particles[i]

        new_best = len(particles)
        if best != new_best:
            best = new_best
            best_count = 0
        best_count += 1 if (new_best == best) else 0
    
    print(best)