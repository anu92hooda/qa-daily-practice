import getpass

# list of dict
users=  [{"username":"anu", "password": "hello123"},
         {"username":"user1", "password": "user123"},
         {"username":"user2", "password": "admin123"}

         ]

# Function to validate login
def login(username,password):
    for user in users:
        if user["username"]==username and user["password"]==password:
            return f"welcome {username}"

    return"Invalid username or password , Please try again"

#Function to take user input
def userinput():
    print("QA Login System page")
    username= input("Please Enter the username ").strip()
    password = getpass.getpass("Please Enter the password ")

    result= login(username,password)
    print(result)


userinput()

