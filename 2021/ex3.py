def part1(diagnostic):
    number_length = len(diagnostic[0])
    zeros_count = [0] * number_length
    ones_count = [0] * number_length
    for number in diagnostic:
        for i in range(number_length):
            if number[i] == '0':
                zeros_count[i] += 1
            else:
                ones_count[i] += 1

    gamma = 0
    epsilon = 0

    for i in range(number_length):
        pow2 = 2 ** (number_length - i - 1)
        if ones_count[i] > zeros_count[i]:
            gamma += pow2
        else:
            epsilon += pow2

    return gamma * epsilon


def part2(diagnostic):
    number_length = len(diagnostic[0])

    oxygen_list = [*diagnostic]
    co2_list = [*diagnostic]

    for i in range(number_length):
        zeros_oxygen = 0
        ones_oxygen = 0
        zeros_co2 = 0
        ones_co2 = 0

        for number in oxygen_list:
            if number[i] == '0':
                zeros_oxygen += 1
            else:
                ones_oxygen += 1
        for number in co2_list:
            if number[i] == '0':
                zeros_co2 += 1
            else:
                ones_co2 += 1

        if len(oxygen_list) > 1:
            if ones_oxygen >= zeros_oxygen:
                oxygen_list = [x for x in oxygen_list if x[i] == '1']
            else:
                oxygen_list = [x for x in oxygen_list if x[i] == '0']

        if len(co2_list) > 1:
            if ones_co2 >= zeros_co2:
                co2_list = [x for x in co2_list if x[i] == '0']
            else:
                co2_list = [x for x in co2_list if x[i] == '1']

    oxygen = int(oxygen_list[0], 2)
    co2 = int(co2_list[0], 2)

    return oxygen * co2


def main():
    with open("input/ex3.txt") as file:
        diagnostic = [x.strip() for x in file.readlines()]

    print(f"part 1: {part1(diagnostic)}")
    print(f"part 2: {part2(diagnostic)}")


if __name__ == '__main__':
    main()
