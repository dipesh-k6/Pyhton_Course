# from the given data find which student got the highest marks with his/her name.

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

students = {sum(student.get("marks").values()):student.get("name") for student in student_info}
marks, name = sorted(students.items())[-1]

print(f"Student with highest marks {marks} is {name}")