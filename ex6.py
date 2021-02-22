import string


def part1(all_group_answers):
    sum_counts = 0

    for group_answers in all_group_answers:
        group_questions = []
        for person_answers in group_answers:
            for answer in person_answers:
                if answer not in group_questions:
                    group_questions.append(answer)
        sum_counts += len(group_questions)

    return sum_counts


def part2(all_group_answers):
    sum_counts = 0

    for group_answers in all_group_answers:
        group_questions = list(string.ascii_lowercase)
        for person_answers in group_answers:
            questions_to_remove = []
            for question in group_questions:
                if question not in list(person_answers):
                    questions_to_remove.append(question)
            for question in questions_to_remove:
                group_questions.remove(question)
        sum_counts += len(group_questions)

    return sum_counts


def main():
    all_group_answers = []

    with open("ex6input.txt") as file:
        person_answers = []
        for line in file.readlines():
            if line != "\n":
                person_answers.append(line[:-1])
            else:
                all_group_answers.append(person_answers)
                person_answers = []
        all_group_answers.append(person_answers)

    print(f"part 1: {part1(all_group_answers)}")
    print(f"part 2: {part2(all_group_answers)}")


if __name__ == '__main__':
    main()
