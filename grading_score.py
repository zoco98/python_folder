student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
print(student_scores)
student_grades = student_scores
for key in student_scores:
    if student_scores[key]>91 and student_scores[key]<100:
        student_grades[key] = "Outstanding"
    elif student_scores[key]>81 and student_scores[key]<90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key]>71 and student_scores[key]<80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)
student_grades["sriparna"] = "Not bad"
student_grades[2] = "Not bad"
print(student_grades)