student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
"""
This is the scoring criteria:
  Scores 91 - 100: Grade = "Outstanding"
  Scores 81 - 90: Grade = "Exceeds Expectations"
  Scores 71 - 80: Grade = "Acceptable"
  Scores 70 or lower: Grade = "Fail"
"""
for k, v in student_scores.items():
    if v > 90:
         student_grades[k] = "Outstanding"
    elif v > 80:
         student_grades[k] = "Exceeds Expectations"
    elif v > 70:
        student_grades[k] = "Acceptable"
    else:
        student_grades[k] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)