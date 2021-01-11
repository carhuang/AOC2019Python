import sys
sys.path.append("..")
import reader

class IntcodeComputer:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.input = 0
        self.output_ = 0

    def enter_input(self, val):
        self.input = val

    def print_output(self):
        print("output", self.output)
    
    def get_value(self, pos, mode):
        if mode == 1:
            return pos
        return self.program[pos]

    def write_value(self, val, pos):
        self.program[pos] = val

    def get_digit(self, number, n):
        return number // 10**n % 10   

    def add(self):
        modes = self.program[self.pc] // 100
        val = self.get_value(program[self.pc + 1], self.get_digit(modes, 0)) + self.get_value(program[self.pc + 2], self.get_digit(modes, 1))
        self.write_value(val, self.program[self.pc + 3])
        self.pc += 4

    def multiply(self):
        modes = self.program[self.pc] // 100
        val = self.get_value(program[self.pc + 1], self.get_digit(modes, 0)) * self.get_value(program[self.pc + 2], self.get_digit(modes, 1))
        self.write_value(val, self.program[self.pc + 3])
        self.pc += 4

    def halt(self):
        self.pc = -1

    def load(self):
        self.write_value(self.input, self.program[self.pc + 1])
        self.pc += 2

    def output(self):
        mode = self.program[self.pc] // 100
        self.output_ = self.get_value(self.program[self.pc + 1], mode)
        print("output", self.output_)
        self.pc += 2

    def run(self):
        while self.pc < len(program) and self.pc >= 0:
            opcode = self.program[self.pc]
            instruction = opcode % 100
            # print(opcode, instruction)
            switcher = {
                1: self.add,
                2: self.multiply,
                3: self.load,
                4: self.output,
                99: self.halt
            }
            switcher[instruction]()


program = reader.get_intcode_program('../input/05.txt')
computer = IntcodeComputer(program)
computer.enter_input(1)
computer.run()
