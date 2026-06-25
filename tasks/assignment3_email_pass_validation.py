valid_domains = ["com", "org", "gov", "np", "io"]
valid_specialcharacters = "!@#$%^&*(),.?\":{}|<>"

def validate_email(email):
    if(email.find("@") == -1 or email.find(".") == -1):
        return False, "invalid email format"
    
    email_prefix = email.strip().split("@")
    email_suffix = email.strip().lower().split(".")

    if(not email_prefix[0]):
        return False, "invalid email"
    if(not email_suffix[-1] in valid_domains):
        return False, "invalid email domain"
    
    return True, " email validated"

check_mail = False

while(not check_mail):
    email = input("\n enter your email : ")
    check_mail, message = validate_email(email)
    print(message)


# email = "example@mail.ab"

# while (email.split(".")[-1].lower() not in valid_domains):
#     print(f"valid domains = {", ".join(valid_domains)}")
#     email = input("enter your email : ")

def validate_password(password):
    errors = []
    
    if (not len(password) >= 8):
        errors.append("\n*minimum password length is 8")
    if (not any(char in valid_specialcharacters for char in password)):
        errors.append("include at least one special character")
    if (not any(char.isupper() for char in password)):
        errors.append("include at least one uppercase character")
    if(not any(char.islower() for char in password)):
        errors.append("include at least one lowercase character")
    if(not any(char.isnumeric() for char in password)):
        errors.append("include at least one number")

    if(errors):
        message = "\n*".join(errors)
        return False, message
    else:
        return True, " password validated"
    
check_pass = False
while(not check_pass):
    password = input("\nenter your password : ")
    check_pass, message = validate_password(password)
    print(message)
      
# password = input("enter your password : ")
# print(validate_password(password))

print(f"""\nyour email and password are = 
 Email : {email}
 Password : {password}""")