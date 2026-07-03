# calculate which subject has total highest marks

student_info = [
    {
        "name": "Ram",
        "marks": {
            "math": 90,
            "social": 20,
            "english": 40,
        }
    },
    {
        "name": "Hari",
        "marks": {
            "math": 85,
            "social": 45,
            "english": 35,
        }
    },
    {
        "name": "Geeta",
        "marks": {
            "math": 55,
            "social": 58,
            "english": 29,
        }
    },
    {
        "name": "Sita",
        "marks": {
            "math": 56,
            "social": 86,
            "english": 49,
        }
    },
]

sub_marks = [student.get("marks") for student in student_info]
sub_total_marks = {}

for items in sub_marks:
    for subject, marks in items.items():
        sub_total_marks[subject] = sub_total_marks.get(subject, 0) + marks

marks_sub = {value:key for key,value in sub_total_marks.items()}
marks, subject = sorted(marks_sub.items())[-1]  

print(f"highest marks is {marks} for subject {subject}")