#Making Subjects Dictionary
subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}
#Creating Students Dictionary and using for loop to put each students test scores
students = {}
for subject, scores in subjects.items():
    for student, score in scores.items():
        if student not in students:
            students[student] = {}
        students[student][subject] = score
#prints out students and their respected subject grades
print(students)
