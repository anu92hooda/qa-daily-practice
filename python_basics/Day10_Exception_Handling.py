from traceback import print_exc

# Function take user input for name and Age
def validate_user_input(name, age):

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if not age.isdigit():
        raise ValueError("Age must be number.")

    if int(age)<= 0:
        raise ValueError("Age cannot be 0 or negative")

    return name , int(age)

# Main block
try:
    name_input= input("Enter your Full Name eg 'Anu Hooda' ")
    age_input= input("Enter your age in number")

    name, age= validate_user_input(name_input, age_input)
    print(f"welcome {name} , your age is{age}")

except ValueError as ve:
    print("Input error:" , ve)

finally:
    print("Program ended")






