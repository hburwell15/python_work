#Code to get the average of students heights that are inputed

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_students = 0
total_height = 0

for height in student_heights:
    total_height += height

for students in student_heights:
  total_students += 1

print(round((total_height / total_students)))


