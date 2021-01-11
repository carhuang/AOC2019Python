import sys
sys.path.append("..")
import reader

def get_fuel_req(mass):
    current_fuel = mass // 3 - 2
    if current_fuel <= 0:
        return 0
    return current_fuel + get_fuel_req(current_fuel)

def get_fuel_req_sum(modules):
    sum_ = 0
    for module in modules:
        sum_ += get_fuel_req(module)
    return sum_

modules = reader.get_int_input_line_by_line("../input/01.txt")
print(get_fuel_req_sum(modules))
