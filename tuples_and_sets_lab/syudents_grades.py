number_students = int(input())
student_book = {}

for i in range(number_students):
    name, grade = input().split()
    if name not in student_book:
        student_book[name] = []
    student_book[name].append(float(grade))

for student in student_book.items():
    avg = sum(student[1]) / len(student[1])

    print(f"{student[0]} -> {' '.join([f'{el:.2f}' for el in student[1]])} (avg: {avg:.2f})")
