def get_int_input_line_by_line(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(int(line.strip()))
    return data

def get_string_input_line_by_line(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip())
    return data

def get_intcode_program(filename):
    program = open(filename, 'r').read().split(',')
    return [int(num) for num in program]


