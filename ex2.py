"""wczytuje wszystkie hasła, i sprawdza je obydwiema regułami"""

passwords = []

with open("ex2input.txt") as file:
    for line in file.readlines():
        passwords.append(line.split(' '))

counter1 = 0
counter2 = 0
for p in passwords:
    numbers = p[0].split('-')
    minn = int(numbers[0])
    maxx = int(numbers[1])
    char = p[1][0]
    password = p[2][:-1]
    count = password.count(char)
    if minn <= count <= maxx:
        counter1 += 1

    if password[minn - 1] == char and password[maxx - 1] != char:
        counter2 += 1
    elif password[minn - 1] != char and password[maxx - 1] == char:
        counter2 += 1

print(f"part 1: {counter1}")
print(f"part 2: {counter2}")
