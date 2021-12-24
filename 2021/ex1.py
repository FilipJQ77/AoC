def part1(depths):
    increased = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increased += 1
    return increased


def part2(depths):
    increased = 0
    for i in range(3, len(depths)):
        sum1 = depths[i - 3] + depths[i - 2] + depths[i - 1]
        sum2 = depths[i - 2] + depths[i - 1] + depths[i]
        if sum2 > sum1:
            increased += 1
    return increased


def main():
    with open("input/ex1.txt") as file:
        depths = [int(x) for x in file.readlines()]

    print(f"part 1: {part1(depths)}")
    print(f"part 2: {part2(depths)}")


if __name__ == '__main__':
    main()
