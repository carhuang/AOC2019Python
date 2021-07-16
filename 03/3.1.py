import sys
sys.path.append("..")
import reader

map = reader.get_string_input_line_by_line("../input/03.txt")

def update_x_location(x):
  return (x + 3) % len(map[0])

def count_trees_in_path():
  x = 0  # x coordinate
  num_trees = 0
  for y in range(len(map)):   # walk 1 step down each round
    if map[y][x] == '#':
      num_trees += 1
    x = update_x_location(x)  # walk 3 steps right
  return num_trees

print(count_trees_in_path())