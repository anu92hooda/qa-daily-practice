
# function to validate name
def name_validate(name):

    if not name.split():
        raise ValueError("Name cannot be empty")

    if "@" in name or "." in name:
        raise ValueError("Name cannot have special chars")

    return name


# function to validate age
def age_validate(age):

    if not age.isdigit():
        raise ValueError("Age must be a number ")

    if int(age)<0:
        raise ValueError("Age should be greater then 0")

    return age


#function to validate email
def email_validate(email):

    if not email:
        raise ValueError("email cannot be empty")

    if "@" not in email or "." not in email:
        raise ValueError("email must contain'@' and '.' ")

    if email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."):
        raise ValueError("email cannot start or end with '@' or '.'")

    return email


