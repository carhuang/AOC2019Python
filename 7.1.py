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

    def jump_if_true(self):
        modes = self.program[self.pc] // 100
        p1 = self.get_value(self.program[self.pc + 1], self.get_digit(modes, 0))
        if p1:
            self.pc = self.get_value(self.program[self.pc + 2], self.get_digit(modes, 1))
        else:
            self.pc += 3

    def jump_if_false(self):
        modes = self.program[self.pc] // 100
        p1 = self.get_value(self.program[self.pc + 1], self.get_digit(modes, 0))
        if p1:
            self.pc += 3
        else:
            self.pc = self.get_value(self.program[self.pc + 2], self.get_digit(modes, 1))

    def less_than(self):
        modes = self.program[self.pc] // 100
        p1 = self.get_value(self.program[self.pc + 1], self.get_digit(modes, 0))
        p2 = self.get_value(self.program[self.pc + 2], self.get_digit(modes, 1))
        pos = self.program[self.pc + 3]
        if p1 < p2:
            self.write_value(1, pos)
        else:
            self.write_value(0, pos)
        self.pc += 4

    def equals(self):
        modes = self.program[self.pc] // 100
        p1 = self.get_value(self.program[self.pc + 1], self.get_digit(modes, 0))
        p2 = self.get_value(self.program[self.pc + 2], self.get_digit(modes, 1))
        pos = self.program[self.pc + 3]
        if p1 == p2:
            self.write_value(1, pos)
        else:
            self.write_value(0, pos)
        self.pc += 4

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
                5: self.jump_if_true,
                6: self.jump_if_false,
                7: self.less_than,
                8: self.equals,
                99: self.halt
            }
            switcher[instruction]()

phase_setting_sequences = []
def generate_phase_setting_sequences(setting_choices, phase_setting_seq):
    if len(setting_choices) == 1:
        phase_setting_seq.append(setting_choices[0])
        phase_setting_sequences.append(phase_setting_seq)
        return
    else:
        for phase_setting in setting_choices:
            generate_phase_setting_sequences(setting_choices.remove(phase_setting), phase_setting_seq.append(phase_setting))

generate_phase_setting_sequences(set())



program = reader.get_intcode_program('../input/07.txt')
computer = IntcodeComputer(program)