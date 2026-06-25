# Question:
# students = [
#     {"name": "Ali", "grade": 85, "city": "Kathmandu"},
#     {"name": "Sara", "grade": 92, "city": "Pokhara"},
#     {"name": "John", "grade": 45, "city": "Kathmandu"},
#     {"name": "Emma", "grade": 78, "city": "Pokhara"},
#     {"name": "Ray", "grade": 55, "city": "Kathmandu"},
# ]

# Using comprehensions only:
# 1. List of names who passed (grade >= 60)
# 2. Dictionary of {name: grade} for failed students
# 3. Set of unique cities
# 4. List of names from Kathmandu who passed

students = [
    {"name": "Ali", "grade": 85, "city": "Kathmandu"},
    {"name": "Sara", "grade": 92, "city": "Pokhara"},
    {"name": "John", "grade": 45, "city": "Kathmandu"},
    {"name": "Emma", "grade": 78, "city": "Pokhara"},
    {"name": "Ray", "grade": 55, "city": "Kathmandu"},
]

passed_list = [student["name"] for student in students if student["grade"] >= 60]
print(passed_list)

failed_dictionary = {
    student["name"]: student["grade"] for student in students if student["grade"] < 60
}
print(failed_dictionary)

unique_cities = {student["city"] for student in students}
print(unique_cities)

passed_list_kathmandu = [
    student["name"]
    for student in students
    if student["grade"] >= 60 and student["city"].lower() == "kathmandu"
]
print(passed_list_kathmandu)
