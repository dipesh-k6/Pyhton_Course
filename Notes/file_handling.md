# File modes:
    "w"write — creates file, overwrites if exists
    "r"read — file must exist
    "a"append — adds to end, never overwrites

---------------------------------------------------------------------------------------------------

# creating  a file
    Way 1 — basic open/close:
        file = open("receipt.txt", "w")
        file.write("Hello!")
        file.close() 
                                                   - must always close!
    Way 2 — with statement (recommended):
        with open("receipt.txt", "w") as file:
        file.write("Hello!")                        - file closes automatically here!

----------------------------------------------------------------------------------------------------

# reading a file
    way 1 - read entire file as one string
        with open("test.txt", "r") as file:
        content = file.read()
        print(content)

    way 2 - read line by line into a list
        with open("test.txt", "r") as file:
        lines = file.readlines()
        print(lines)

    way 3 - iterate line by line (memory efficient - generator style!)
        with open("test.txt", "r") as file:
        for line in file:
        print(line)

------------------------------------------------------------------------------------------------------

