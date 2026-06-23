# Get unique students who attended Monday
# Find students who attended both days
# Find students who attended only Monday (not Tuesday)
# Find students who attended at least one day
# Find students who attended only one day (not both) — this one's tricky, look up

students_monday = ["Ali", "Sara", "John", "Emma", "Ali"]
students_tuesday = ["Sara", "Ray", "John", "Mike", "Emma"]

print(f"unique students who attended Monday : {list(set(students_monday))}")
print(f"students who attended both days : {list(set(students_monday).intersection(students_tuesday))}")
print(f"students who attended only Monday (not Tuesday) : {list(set(students_monday).difference(students_tuesday))}")
print(f"students who attended at least one day : {list(set(students_monday).union(students_tuesday))}")
print(f"""students who attended only one day (not both) :{list(set(students_monday).difference(students_tuesday)
.union(set(students_tuesday).difference(students_monday)))} """)