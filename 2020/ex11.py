def is_seat_neighbour(current_seat_lines, x, y):
    if current_seat_lines[x][y] == "#":
        return 1
    else:
        return 0


def new_seat_occupation(current_seat_lines, x, y):
    seat = current_seat_lines[x][y]
    seat_lines_number = len(current_seat_lines)
    seat_line_length = len(current_seat_lines[0])

    if seat == ".":
        return "."
    else:
        neighbours = 0
        if x - 1 >= 0:
            if y - 1 >= 0:
                neighbours += is_seat_neighbour(current_seat_lines, x - 1, y - 1)
            neighbours += is_seat_neighbour(current_seat_lines, x - 1, y)
            if y + 1 < seat_line_length:
                neighbours += is_seat_neighbour(current_seat_lines, x - 1, y + 1)

        if y - 1 >= 0:
            neighbours += is_seat_neighbour(current_seat_lines, x, y - 1)
        neighbours += is_seat_neighbour(current_seat_lines, x, y)
        if y + 1 < seat_line_length:
            neighbours += is_seat_neighbour(current_seat_lines, x, y + 1)

        if x + 1 < seat_lines_number:
            if y - 1 >= 0:
                neighbours += is_seat_neighbour(current_seat_lines, x + 1, y - 1)
            neighbours += is_seat_neighbour(current_seat_lines, x + 1, y)
            if y + 1 < seat_line_length:
                neighbours += is_seat_neighbour(current_seat_lines, x + 1, y + 1)
        if seat == "L" and neighbours == 0:
            return "#"
        elif seat == "#" and neighbours >= 4:
            return "L"
        else:
            return current_seat_lines[x][y]


def part1(seat_lines):
    seat_lines_number = len(seat_lines)
    seat_line_length = len(seat_lines[0])
    current_seat_lines = seat_lines.copy()
    stabilized = False
    while not stabilized:
        new_seat_lines = current_seat_lines.copy()
        # check every seat
        for i in range(seat_lines_number):
            new_seat_line = ""
            for j in range(seat_line_length):
                new_seat_line += new_seat_occupation(current_seat_lines, i, j)
            new_seat_lines[i] = new_seat_line

        # check if nothing changed
        stabilized = True  # assumption
        for i in range(seat_lines_number):
            if current_seat_lines[i] != new_seat_lines[i]:
                stabilized = False
                break
        current_seat_lines = new_seat_lines.copy()

    counter = 0
    for i in range(seat_lines_number):
        for j in range(seat_line_length):
            if current_seat_lines[i][j] == "#":
                counter += 1
    return counter


def part2(seat_lines):
    pass


def main():
    seat_lines = []
    with open("input/ex11.txt") as file:
        for line in file.readlines():
            seat_lines.append(line[:-1])
    print(f"part 1: {part1(seat_lines)}")
    print(f"part 2: {part2(seat_lines)}")


if __name__ == '__main__':
    main()
