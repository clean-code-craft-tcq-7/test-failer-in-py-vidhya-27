def get_pair_number(major_index, minor_index):
    return major_index * 5 + minor_index + 1


def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{get_pair_number(i, j)} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(get_pair_number(0,0) == 1)
assert(get_pair_number(4,4) == 25)
assert(get_pair_number(3,4) == 20)
assert(get_pair_number(4,3) == 24)
assert(result <= get_pair_number(4,4))
assert(result == 25)
print("All is well (maybe!)")
