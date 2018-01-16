from sys import stdin

class MemoryBank(object):
    def __init__(self, total=26, default=0):
        self._registers = [default]*total
    
    def set(self, register, value):
        assert(register.isalpha())

        i = self._index(register)
        self._registers[i] = value
    
    def get(self, register):
        assert(register.isalpha())

        i = self._index(register)
        return self._registers[i]

    def _index(self, register):
        return ord(register)-97

class Program(object):
    def __init__(self, statements, memory):
        self._memory = memory
        self._pc = 0
        self._statements = statements

    def run(self):
        commands = {
            'set': self._set,
            'sub': self._sub,
            'mul': self._mul,
            'jnz': self._handle_jnz}
        n = len(self._statements)
        mul_ops = 0

        while self._pc>=0 and self._pc<n:
            command, register, value = self._statements[self._pc]
            if self._is_register(value):
                value = self._memory.get(value)
            else:
                value = int(value)
            commands[command](register, value)

            if (command == 'mul'):
                mul_ops += 1
            # print('b:{0} c:{1} a:{2}'.format(self._memory.get('b'), self._memory.get('c'), self._memory.get('a')))
            self._pc += 1

        return mul_ops

    def _is_register(self, value):
        try:
            _ = int(value)
            return False
        except ValueError:
            return True

    def _set(self, register, value):
        self._memory.set(register, value)

    def _sub(self, register, value):
        old_value = self._memory.get(register)
        self._memory.set(register, old_value-value)

    def _mul(self, register, value):
        old_value = self._memory.get(register)
        self._memory.set(register, old_value*value)
    
    def _handle_jnz(self, register, offset):
        register_value = register
        if self._is_register(register):
            register_value = self._memory.get(register)

        self._jnz(register_value, offset)

    def _jnz(self, value, offset):
        if value !=0:
            self._pc += (offset-1)#so that the pc+1 in the main loop will be come back to the proper pc 

if __name__ == '__main__':
    statements = []
    for line in stdin:
        statement = line.split(' ')
        statements.append([s.strip() for s in statement]) 
    memory = MemoryBank(total=8, default=0)
    program = Program(statements, memory)
    print(program.run())

