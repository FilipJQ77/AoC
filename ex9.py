def check_number(numbers, index):
    number = numbers[index]
    for i in range(index - 25, index):
        for j in range(i + 1, index):
            summ = numbers[i] + numbers[j]
            if summ == number:
                return True
    return False


def part1(numbers):
    for i in range(25, len(numbers)):
        if not check_number(numbers, i):
            return numbers[i]


def find_contiguous_set(numbers, index):
    number = numbers[index]
    for i in range(index):
        summ = numbers[i]
        if summ > number:
            continue
        for j in range(i + 1, index):
            summ += numbers[j]
            if summ == number:
                return numbers[i:j]
            elif summ > number:
                continue


def part2(numbers):
    not_valid_index = 0
    for i in range(25, len(numbers)):
        if not check_number(numbers, i):
            not_valid_index = i
            break
    cont_set = find_contiguous_set(numbers, not_valid_index)
    return min(cont_set) + max(cont_set)


def main():
    numbers = []
    with open("ex9input.txt") as file:
        for line in file.readlines():
            numbers.append(int(line))
    print(f"part 1: {part1(numbers)}")
    print(f"part 2: {part2(numbers)}")


if __name__ == '__main__':
    main()
