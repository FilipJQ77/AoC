class BinarySpace:
    def __init__(self, minn, number):
        self.minn = minn
        self.maxx = number
        self.size = number - minn + 1

    def lower_half(self):
        self.size //= 2
        self.maxx -= self.size

    def upper_half(self):
        self.size //= 2
        self.minn += self.size


def main():
    passes = []
    passes_id = []
    max_id = -1
    with open("input/ex5.txt") as file:
        for line in file:
            passes.append(line[:-1])
    for p in passes:
        binary_space_row = BinarySpace(0, 127)
        for char in p[:7]:
            if char == 'F':
                binary_space_row.lower_half()
            else:
                binary_space_row.upper_half()
        binary_space_column = BinarySpace(0, 7)
        for char in p[7:]:
            if char == 'L':
                binary_space_column.lower_half()
            else:
                binary_space_column.upper_half()
        row = binary_space_row.minn
        column = binary_space_column.minn
        pass_id = row * 8 + column
        passes_id.append(pass_id)
        if pass_id > max_id:
            max_id = pass_id

    print(f"part 1: {max_id}")

    passes_id.sort()
    for i in range(len(passes_id) - 1):
        if passes_id[i] + 2 == passes_id[i + 1]:
            print(f"part 2: {passes_id[i] + 1}")


if __name__ == '__main__':
    main()
