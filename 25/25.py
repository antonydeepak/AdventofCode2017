import re
from sys import stdin
from functools import partial

class CircularBuffer(object):
    def __init__(self, capacity=10):
        self._capacity = capacity

        self._buffer = [0]*self._capacity
        self._head = 0
        self._tail = 0
        self._current = 0

        self._buffer[self._current] = 0

    def write(self, value):
        self._buffer[self._current] = value

    def read(self):
        return self._buffer[self._current]

    def seek_right(self):
        if self._is_full():
            self._resize()

        i = self._increment(self._current)
        if self._current == self._tail:
            self._tail = i
        self._current = i

    def seek_left(self):
        if self._is_full():
            self._resize()

        i = self._decrement(self._current)
        if self._current == self._head:
            self._head = i
        self._current = i

    def _resize(self):
        buffer = CircularBuffer(self._capacity*2)

        offset = [0, False]
        i = self._head
        while i!=self._tail:
            buffer.write(self._buffer[i])
            buffer.seek_right()
            if i == self._current:
                offset[1] = True
            if offset[1]:
                offset[0] += 1
            i = self._increment(i)
        buffer.write(self._buffer[self._tail])
        
        while offset[0]>0:
            buffer.seek_left()
            offset[0] -= 1

        self._capacity = buffer._capacity
        self._buffer = buffer._buffer
        self._head = buffer._head
        self._tail = buffer._tail
        self._current = buffer._current

    def _is_full(self):
        return self._increment(self._tail) == self._head
    
    def _increment(self, i):
        return (i+1)%self._capacity

    def _decrement(self, i):
        return (i-1)%self._capacity

def process(write, move, next_state, buffer):
    assert(move == 'right' or move == 'left')

    buffer.write(write)
    if move == 'right':
        buffer.seek_right()
    elif move:
        buffer.seek_left()
    
    return next_state

def parse_start_state(line):
    return re.match('Begin in state (\w+).', line).groups()[0]

def parse_checksum(line):
    return int(re.match('Perform a diagnostic checksum after (\d+) steps.', line).groups()[0])

def parse_states(states, stdin, buffer):
    line = stdin.readline()
    while (line):
        line = stdin.readline().strip()
        state_id = re.match('In state (\w+):', line).groups()[0]

        states[state_id] = [None]*2
        state = states[state_id]
        for _ in range(2):
            line = stdin.readline().strip()
            value = int(re.match('If the current value is (\d+):', line).groups()[0])
            line = stdin.readline().strip()
            write_value = int(re.match('- Write the value (\d+).', line).groups()[0])
            line = stdin.readline().strip()
            move_value = re.match('- Move one slot to the (\w+).', line).groups()[0]
            line = stdin.readline().strip()
            next_state = re.match('- Continue with state (\w+).', line).groups()[0]

            state[value] = partial(process, write_value, move_value, next_state, buffer)

        line = stdin.readline()

def print_buffer(buffer):
        i = buffer._head
        while i!=buffer._tail:
            print(buffer._buffer[i], end=' ')
            i = buffer._increment(i)
        print(buffer._buffer[buffer._tail])
        print(f'head:{buffer._head} tail:{buffer._tail} cur: {buffer._current}')

if __name__ == '__main__':
    buffer = CircularBuffer()
    states = {}

    active_state = parse_start_state(stdin.readline().strip())
    steps = parse_checksum(stdin.readline().strip())

    parse_states(states, stdin, buffer)
    # print(states)

    for _ in range(steps):
        active_state = states[active_state][buffer.read()]()

    print(sum(buffer._buffer))