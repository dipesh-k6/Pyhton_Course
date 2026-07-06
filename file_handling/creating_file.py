# file = open("abc.txt",'w') 
# file.write("hello")
# file.close()

# with open("abc.txt", 'a') as file:
#   file.write(", hi")

with open("abc.txt", 'r') as file:
    content = file.read()
    print(content)

