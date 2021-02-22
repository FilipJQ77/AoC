def part1(instructions):
    acc = 0
    i = 0
    instructions_done = []
    len_instructions = len(instructions)
    while i < len_instructions:
        if i in instructions_done:
            return acc
        else:
            instructions_done.append(i)
        instruction = instructions[i].split(" ")
        if instruction[0] == "acc":
            acc += int(instruction[1])
            i += 1
        elif instruction[0] == "jmp":
            i += int(instruction[1])
        else:
            i += 1


def run_code(instructions):
    """for part 2"""
    acc = 0
    i = 0
    instructions_done = []
    len_instructions = len(instructions)
    while i < len_instructions:
        if i in instructions_done:
            return None
        else:
            instructions_done.append(i)
        instruction = instructions[i].split(" ")
        if instruction[0] == "acc":
            acc += int(instruction[1])
            i += 1
        elif instruction[0] == "jmp":
            i += int(instruction[1])
        else:
            i += 1
    return acc


def part2(instructions):
    for i in range(len(instructions)):
        instruction = instructions[i].split(" ")
        if instruction[0] == "nop":
            new_instructions = instructions.copy()
            new_instructions[i] = new_instructions[i].replace("nop", "jmp")
            result = run_code(new_instructions)
            if result is not None:
                return result
        elif instruction[0] == "jmp":
            new_instructions = instructions.copy()
            new_instructions[i] = new_instructions[i].replace("jmp", "nop")
            result = run_code(new_instructions)
            if result is not None:
                return result


def main():
    instructions = []
    with open("ex8input.txt") as file:
        for line in file.readlines():
            instructions.append(line[:-1])

    print(f"part 1:{part1(instructions)}")
    print(f"part 2:{part2(instructions)}")


if __name__ == '__main__':
    main()
