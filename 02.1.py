import reader

class IntcodeComputer:
    def __init__(self, program):
        self.program = program
        self.pc = 0
    
    def get_value(self, pos):
        return self.program[pos]

    def write_value(self, val, pos):
        self.program[pos] = val

    def add(self):
        val = self.get_value(program[self.pc + 1]) + self.get_value(program[self.pc + 2])
        self.write_value(val, self.program[self.pc + 3])
        self.pc += 4

    def multiply(self):
        val = self.get_value(program[self.pc + 1]) * self.get_value(program[self.pc + 2])
        self.write_value(val, self.program[self.pc + 3])
        self.pc += 4

    def halt(self):
        self.pc = -1

    def run(self):
        switcher = {
            1: self.add,
            2: self.multiply,
            99: self.halt
        }
        while self.pc < len(program) and self.pc >= 0:
            opcode = self.program[self.pc]
            switcher[opcode]()


program = reader.get_intcode_program("./input/02.txt")
program[1] = 12
program[2] = 2
computer = IntcodeComputer(program)
computer.run()
print(computer.program[0])