import csv
import random

students = []

with open("students.csv", "r", encoding="utf-8") as file:
    read_lines = csv.reader(file)

    for line in read_lines:
        students.append(line[0])

number_students = 3 

if(number_students <= len(students)):
    chosen_students = random.sample(students,number_students)

    print("Studentii alesi sunt : ")

    for student in chosen_students:
        print(student)
else:
    print("Nu exista suficienti studenti in lista")
