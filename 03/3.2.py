import sys
sys.path.append("..")
import reader

map = reader.get_string_input_line_by_line("../input/03.txt")

def update_x_location(x, step):
  return (x + step) % len(map[0])

# count the number of trees in the path with the specified slope
def count_trees_in_path(x_step, y_step):
  x = 0
  num_trees = 0
  for y in range(0, len(map), y_step):
    if map[y][x] == '#':
      num_trees += 1
    x = update_x_location(x, x_step)
  return num_trees

a = count_trees_in_path(1, 1)  # slope right 1, down 1
b = count_trees_in_path(3, 1)  # slope right 3, down 1
c = count_trees_in_path(5, 1)  # slope right 5, down 1
d = count_trees_in_path(7, 1)  # slope right 7, down 1
e = count_trees_in_path(1, 2)  # slope right 1, down 2
print(a * b * c * d * e)