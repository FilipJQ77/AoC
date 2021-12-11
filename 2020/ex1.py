"""wczytuje z pliku zestaw liczb, sprawdza wszystkie kombinacje 2 i 3"""

numbers = []
with open("input/ex1.txt") as file:
    for number in file.readlines():
        numbers.append(int(number))

len_numbers = len(numbers)
for i in range(len_numbers):
    for j in range(i, len_numbers):
        summ = numbers[i] + numbers[j]
        if summ == 2020:
            print(f"part 1: {numbers[i] * numbers[j]}")

for i in range(len_numbers):
    for j in range(i + 1, len_numbers):
        for k in range(j + 1, len_numbers):
            summ = numbers[i] + numbers[j] + numbers[k]
            if summ == 2020:
                print(f"part 2: {numbers[i] * numbers[j] * numbers[k]}")
