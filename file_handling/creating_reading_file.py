with open("test.txt", 'w') as file:
    file.write("Parking System \n")
    file.write("Welcome! \n")

with open("test.txt", 'r') as file:
    content = file.read()
    print(content)

with open("test.txt", 'r') as file:                        #readlines() keeps \n at end of each line. To clean it:
    lines = file.readlines()                               #lines = [line.strip() for line in file.readlines()]
    print(lines)

with open("test.txt", 'r') as file:
    for line in file:
        print(line)