def get_int_input_line_by_line(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(int(line.strip()))
    return data