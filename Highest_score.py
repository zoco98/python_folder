# Input a list of student scores
student_scores = input("Enter students score: ").split()
highest_score = int(student_scores[0])

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if highest_score < student_scores[n]:
    highest_score = student_scores[n]

print(f"The highest score in the class is: {highest_score}")