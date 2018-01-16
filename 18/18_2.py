from sys import stdin
from multiprocessing import Process, Pipe
from threading import Timer
import os

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
    def __init__(self, statements, memory, conn):
        self._memory = memory
        self._pc = 0
        self._statements = statements
        self._conn = conn

    def run(self):
        commands = {
            'set': self._set,
            'add': self._add,
            'mul': self._mul,
            'mod': self._mod,
            'jgz': self._handle_jgz,
            'snd': self._handle_snd,
            'rcv': self._rcv}
        n = len(self._statements)
        snd_ops = 0

        while self._pc>=0 and self._pc<n:
            command, register, value = self._statements[self._pc]
            if self._is_register(value):
                value = self._memory.get(value)
            else:
                value = int(value)
            commands[command](register, value)

            if (command == 'snd'):
                snd_ops += 1
            # print('b:{0} c:{1} a:{2}'.format(self._memory.get('b'), self._memory.get('c'), self._memory.get('a')))
            self._pc += 1

        print(f"{os.getpid()}(pid): {snd_ops}")

    def _is_register(self, value):
        try:
            _ = int(value)
            return False
        except ValueError:
            return True

    def _set(self, register, value):
        self._memory.set(register, value)

    def _add(self, register, value):
        old_value = self._memory.get(register)
        self._memory.set(register, old_value+value)

    def _mul(self, register, value):
        old_value = self._memory.get(register)
        self._memory.set(register, old_value*value)

    def _mod(self, register, value):
        cur_value = self._memory.get(register)
        self._memory.set(register, cur_value%value)

    def _handle_jgz(self, register, offset):
        if self._is_register(register):
            register_value = self._memory.get(register)
        else:
            register_value = int(register)

        self._jgz(register_value, offset)

    def _jgz(self, value, offset):
        if value>0:
            self._pc += (offset-1)#so that the pc+1 in the main loop will be come back to the proper pc 

    def _handle_snd(self, register, dummy):
        register_value = register
        if self._is_register(register):
            register_value = self._memory.get(register)

        self._snd(register_value)

    def _snd(self, value):
        self._conn.send(value)

    def _deadlock(self):
        self._conn.close()

    def _rcv(self, register, dummy):
        deadlock_timer = Timer(1*5, self._deadlock) #30 sec timeout for deadlock
        deadlock_timer.start()

        try:
            value = self._conn.recv()
            deadlock_timer.cancel()
            # print(f"{os.getpid()}-rcv {value}")
        except EOFError:
            self._pc = len(self._statements)
            return

        self._memory.set(register, value)

def join_all(processes):
    for p in processes:
        p.join()

if __name__ == '__main__':
    statements = []
    for line in stdin:
        statement = line.split(' ')
        if len(statement) == 2: #hack to always deflate to 3 values
            statement.append('0') 
        statements.append([s.strip() for s in statement]) 

    pipe = Pipe()

    processes = []
    for i in range(2):

        memory = MemoryBank(total=26, default=0)
        memory.set('p', i)
        program = Program(statements, memory, pipe[i])
        process = Process(target=program.run)
        process.start()

        pipe[i].close()

        processes.append((process, i))

    for i in range(2):
        print(f"{processes[i][0].pid}-{processes[i][1]}")

    join_all((process for process,_ in processes))