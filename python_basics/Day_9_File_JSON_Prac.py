import json

# Create and write to a text file , w will write and create file if its not there
def filehandling():
    with open('firstnote.txt', 'w') as file:
        file.write("Hello QA \n ")
        file.write("Learning file Handling today \n")

# read from firstnote.txt and print

    with open('firstnote.txt','r') as file:
         for line in file:
              print(line.strip())

#filehandling()


def appendToFile():
    with open('firstnote.txt','a') as file:
        file.write("Appended new line\n")

    with open('firstnote.txt','r') as file:
        text=file.read()
        print(text)

appendToFile()



def fileHandlingJson():
    data={
        "name":"Anu",
        "title":"QA",
        "skills":["Python","Postman","Selenium"],
        "experience":6

    }

    with open('data.json','w') as file:
        json.dump(data, file, indent=4)


    with open('data.json','r') as file:
        data=json.load(file)
        print(data["name"],data["skills"])

fileHandlingJson()

