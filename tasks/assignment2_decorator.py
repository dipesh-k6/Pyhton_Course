# task:
# Make a simple calculator
# but use decorator so that only username == "admin" and password == "admin@123" can use the function of calculator
# Note: username and password must be argument of decorator


def calculator_decorator(username, password):
    def outer_function(func):
        def wrapper(n1, n2, choice="None"):

            if username == "admin" and password == "admin@123":
                print("\n Simple Calculator \n")
                valid_choices = ["add", "sub", "mul", "div", "rem", "pow"]
                while choice not in valid_choices:
                    choice = input(f"enter your choice from {valid_choices} : ")
                func(n1, n2, choice)

            else:
                print("incorrect username or password")

        return wrapper

    return outer_function

username = input("enter your username : ")
password = input("enter your password : ")
n1 = int(input("enter a number : "))
n2 = int(input("enter another number : "))


@calculator_decorator(username, password)
def calculate(n1, n2, choice):
    if choice == "add":
        print(f"addition = {n1+n2}")
    elif choice == "sub":
        print(f"substraction = {n1-n2}")
    elif choice == "mul":
        print(f"multiplication = {n1*n2}")
    elif choice == "div":
        print(f"division = {n1/n2}")
    elif choice == "rem":
        print(f"remiander = {n1%n2}")
    elif choice == "pow":
        print(f"power = {n1**n2}")
    else:
        print("something went wrong")
    
calculate(n1,n2)