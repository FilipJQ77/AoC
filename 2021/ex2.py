def part1(moves):
    horizontal = 0
    depth = 0
    for command, number in moves:
        if command == "forward":
            horizontal += number
        elif command == "down":
            depth += number
        elif command == "up":
            depth -= number
    return horizontal * depth


def part2(moves):
    horizontal = 0
    depth = 0
    aim = 0
    for command, number in moves:
        if command == "forward":
            horizontal += number
            depth += aim * number
        elif command == "down":
            aim += number
        elif command == "up":
            aim -= number
    return horizontal * depth


def main():
    moves = []
    with open("input/ex2.txt") as file:
        for line in file.readlines():
            command = line.strip().split()
            moves.append((command[0], int(command[1])))

    print(f"part 1: {part1(moves)}")
    print(f"part 2: {part2(moves)}")


if __name__ == '__main__':
    main()
