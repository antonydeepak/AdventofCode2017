from sys import stdin

pc = 0
registers = [0]*26
last_played = -1

def register_index(register):
    return ord(register)-97

def is_register(value):
    try:
        return int(value)
    except:
        return isinstance(value, str)

def get_value(obj):
    try:
        return int(obj)
    except:
        return registers[register_index(obj)]

def snd(register, dummy):
    global last_played
    last_played = registers[register_index(register)]
    return True

def set(register, value):
    value = get_value(value)
    registers[register_index(register)] = value
    return True

def add(register, value):
    value = get_value(value)
    registers[register_index(register)] += value
    return True

def mul(register, value):
    value = get_value(value)
    registers[register_index(register)] *= value
    return True

def mod(register, value):
    value = get_value(value)
    registers[register_index(register)] %= value
    return True

def rcv(value, dummy):
    value = get_value(value)
    if value!=0:
        print(last_played)
        return False
    return True

def jgz(obj, offset):
    global pc
    value = get_value(obj)
    offset = get_value(offset)
    if value>0:
        pc += offset
        pc -= 1 #so that the pc+1 in the main loop will be come back to the proper pc
    return True

commands = {
    'snd': snd,
    'set': set,
    'add': add,
    'mul': mul,
    'mod': mod,
    'rcv': rcv,
    'jgz': jgz
}

def execute(statement):
    global last_command
    command = statement[0].strip()
    register = statement[1].strip()
    value = None
    if len(statement)>2:
        value = statement[2].strip()
    last_command = command
    
    return commands[command](register, value)

if __name__ == '__main__':
    statements = []
    for line in stdin:
        statement = line.split(' ')
        statements.append(statement) 

    last_command = None
    n = len(statements)
    while pc>=0 and pc<n and (execute(statements[pc])):
        pc += 1