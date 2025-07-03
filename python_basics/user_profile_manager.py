import os
import json
from textwrap import indent

from python_basics.validators import name_validate, age_validate, email_validate
from datetime import datetime


FILENAME="profiles.json"
current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    # User input
    name_input= input("Please enter your full name")
    age_input= input("Please enter your age")
    email_input =input("Please enter your email address")

    #Validation
    name=name_validate(name_input)
    age=age_validate(age_input)
    email=email_validate(email_input)

    user_profile={
        "name": name,
        "age": age,
        "email": email,
        "timestamp": current_time
    }

    # Load or create file
    if os.path.exists(FILENAME):
        with open(FILENAME,'r') as file:
            data=json.load(file)

        data.append(user_profile)

    else:
        # File doest not exist
        data= [user_profile]

    # Save updated data
    with open(FILENAME,'w') as file:
        json.dump (data, file , indent=4)

    #Show profiles?
    show= input("Do you want to see all saved user y/n")

    if show.lower()=="y":
       with open(FILENAME,'r') as file:
           userinfo= json.load(file)
           print(json.dumps(userinfo , indent=4))

except ValueError as ve:
    print("Input error " , ve)

finally :
    print(" Program completed.")



