def part1(adapters):
    adapters.sort()
    adapters.insert(0, 0)
    jolt1 = 0
    jolt3 = 0
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            jolt1 += 1
        elif adapters[i + 1] - adapters[i] == 3:
            jolt3 += 1
    jolt3 += 1
    return jolt1 * jolt3


def part2(adapters):
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    possibilites = 1
    print(adapters)
    len_adapters = len(adapters)
    for i in range(len_adapters - 1):
        if adapters[i + 1] - adapters[i] == 1:
            if i + 2 < len_adapters and adapters[i + 2] - adapters[i] <= 3:
                # possibilites += 1
                if i + 3 < len_adapters and adapters[i + 3] - adapters[i] <= 3:
                    possibilites += 1
                possibilites *= 2  # nah
    return possibilites


def main():
    adapters = []
    with open("input/ex10.txt") as file:
        for line in file.readlines():
            adapters.append(int(line))
    print(f"part 1: {part1(adapters.copy())}")
    print(f"part 2: {part2(adapters.copy())}")  # todo 47514379541324 too high


if __name__ == '__main__':
    main()
