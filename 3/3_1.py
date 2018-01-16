# Tricky implementation. Try to simulate the traversal layer by layer

from sys import stdin
import math

def spiral(num):
    layer = math.ceil(math.sqrt(num))
    layer = layer if layer%2 else layer+1
    layer_start = ((layer-2)**2)
    corner_step = layer-1
    middles = []

    for i in range(1, 5):
        corner = layer_start+(i*corner_step)
        middle = corner-((corner_step)//2)
        middles.append(middle)

    return layer//2 + min((abs(num-middle) for middle in middles))

if __name__ == '__main__':
    for line in stdin:
        print(spiral(int(line.strip())))