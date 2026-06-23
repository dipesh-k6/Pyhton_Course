# Use zip() to pair students with their grades and print each pair like: Ali got A
# Use enumerate() to print a numbered list starting from 1 not 0 (hint: enumerate has a second parameter) 


students = ["Ali", "Sara", "John", "Emma"]
grades = ["A", "B+", "A-", "B"]

print(list(zip(map(lambda student: f"{student} got", students), grades)))

for student, grade in zip(students, grades):
    print(f"{student} got {grade}")
                                                   
for index,student in enumerate(students, 1):         
                                                     
    print(f"{index} : {student}")

#Need a new list → use map()/filter() + list()
#Just printing/iterating → use a for loop, cleaner and more Pythonic