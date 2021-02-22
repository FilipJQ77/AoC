terrain = []

with open("ex3input.txt") as file:
    for line in file.readlines():
        terrain.append(line[:-1])

len_terrain = len(terrain) - 1
terrain_width = len(terrain[0])


def traverse(x, y):
    level_y = 0
    level_x = 0
    counter = 0

    while level_y < len_terrain:
        level_x += x
        level_x %= terrain_width
        level_y += y
        if terrain[level_y][level_x] == '#':
            counter += 1

    return counter


print(f"part 1: {traverse(3, 1)}")
print(f"part 2: {traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)}")
