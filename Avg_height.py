student_heights = input("enter height: ").split()
print(student_heights)
total_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_height +=student_heights[n]

print(f"total height = {total_height}")
print(f"number of students = {len(student_heights)}")
avg_height = total_height/len(student_heights)
print(f"average height = {round(avg_height)}")