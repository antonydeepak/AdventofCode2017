import re
from sys import stdin

def ne(registers, register, value):
    return registers[register] != value
def eq(registers, register, value):
    return registers[register] == value
def gt(registers, register, value):
    return registers[register] > value
def ge(registers, register, value):
    return registers[register] >= value
def lt(registers, register, value):
    return registers[register] < value
def le(registers, register, value):
    return registers[register] <= value
def inc(registers, register, value):
    registers[register] += value
def dec(registers, register, value):
    inc(registers, register, -1*value)

# Both the parts of the puzzle are in this file
if __name__ == '__main__':
    pattern = re.compile("(\w+) (inc|dec) (-?\d+) if (\w+) ([[><=!]+) (-?\d+)")
    registers = {}
    logic = {
        "!=": ne,
        "==": eq,
        ">": gt,
        ">=": ge,
        "<": lt,
        "<=": le
    }
    operation = {
        "inc": inc,
        "dec": dec
    }

    INF = -100000000
    m = INF

    for line in stdin:
        dr,op,v,sr,lo,cond = pattern.match(line).groups()
        v = int(v)
        cond = int(cond)

        if dr not in registers:
            registers[dr] = 0
        if sr not in registers:
            registers[sr] = 0
        if (logic[lo](registers, sr, cond)):
            operation[op](registers, dr, v)

        m = max(m, max(registers.values()))

    print(max(list(registers.values())))
    print(m)