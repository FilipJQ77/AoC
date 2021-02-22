import re


def part1(passports):
    counter = 0
    for passport in passports:
        if len(passport) == 8:
            counter += 1
        elif len(passport) == 7:
            cid = False
            for field in passport:
                f = field.split(':')
                if f[0] == "cid":
                    cid = True
                    break
            if not cid:
                counter += 1
    return counter


def part2(passports):
    counter = 0
    for passport in passports:
        field_counter = 0
        for field in passport:
            f = field.split(":")
            if f[0] == "byr":
                if 1920 <= int(f[1]) <= 2002:
                    field_counter += 1
            elif f[0] == "iyr":
                if 2010 <= int(f[1]) <= 2020:
                    field_counter += 1
            elif f[0] == "eyr":
                if 2020 <= int(f[1]) <= 2030:
                    field_counter += 1
            elif f[0] == "hgt":
                values = re.split(r"(\d+)", f[1])
                unit = values[2]
                height = int(values[1])
                if unit == "cm":
                    if 150 <= height <= 193:
                        field_counter += 1
                elif unit == "in":
                    if 59 <= height <= 76:
                        field_counter += 1
            elif f[0] == "hcl":
                match = re.match(r"#[0-9A-Fa-f]{6}", f[1])
                if match:
                    field_counter += 1
            elif f[0] == "ecl":
                if f[1] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    field_counter += 1
            elif f[0] == "pid":
                if len(f[1]) == 9:
                    if all('0' <= char <= '9' for char in f[1]):
                        field_counter += 1

        if field_counter == 7:
            counter += 1

    return counter


def main():
    passports = []

    with open("ex4input.txt") as file:
        passport = ""
        for line in file.readlines():
            if line != "\n":
                passport += (line[:-1] + " ")
            else:
                passport = passport[:-1]
                passports.append(passport)
                passport = ""
        passport = passport[:-1]
        passports.append(passport)

    passports = list(map(lambda x: x.split(" "), passports))

    print(f"part 1: {part1(passports)}")
    print(f"part 2: {part2(passports)}")


if __name__ == '__main__':
    main()
