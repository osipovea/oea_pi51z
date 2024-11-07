n = int(input("Введите кол-во учеников"))
students = []
for i in range(n):
  student = input().split()
  students.append((student[0], int(student[1])))
for student in students:
  print(student[0], student[1])
print()
for student in students:
  if student[1] >= 4:
    print(student[0], student[1])
