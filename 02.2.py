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

def get_target_pair(program, target):
    for noun in range(100):
        for verb in range(100):
            new_program = program.copy()
            new_program[1] = noun
            new_program[2] = verb
            computer = IntcodeComputer(new_program)
            computer.run()
            if computer.program[0] == target:
                return 100 * noun + verb
    return 0

program = reader.get_intcode_program("./input/02.txt")
print(get_target_pair(program, 19690720))