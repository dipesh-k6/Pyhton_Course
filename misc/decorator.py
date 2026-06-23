user = input("enter your name = ")

def product_decorator(add_product):
    def wrapper(user):
        if user.lower() == "admin":
            add_product(user)
        else:
            print("you are not admin")
    return wrapper

@product_decorator
def add_product(user):
    print("product added successfully", user)