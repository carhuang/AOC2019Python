import reader

def get_fuel_req(mass):
    return mass // 3 - 2

def get_fuel_req_sum(modules):
    sum_ = 0
    for module in modules:
        sum_ += get_fuel_req(module)
    return sum_

modules = reader.get_int_input_line_by_line("./input/01.txt")
print(get_fuel_req_sum(modules))
