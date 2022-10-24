# You Will Create a Quiz Creator/Taking App

# Your App Will connect to https://cae-bootstore.herokuapp.com/
# (Like We Did In class Yesterday)


# There are new endpoints available.  See the Documentation on github to understand how they work:  https://github.com/CrtlAltElite/BookStoreAPI

# Your Application should:
# Login a user in with Basic Auth
# Allow Users to Register an account

# If the user is anyone but you (doesn't has your google-classroom email address) then
# You should create a quiz with 10 random questions from the API from all users questions [Note the API isn't starting with 10 questions]
# After the question is completed you need to Award the user a score based on there correct or incorrect response

# If the User is you (has your google-classroom email address) The user should be prompted with extra prompts that each work properly:
# NOTE: They should also be able to take the quiz like a normal user
# Create Question
# Edit Question
# Delete Question
# View My Questions

# As ALWAYS: add a README.md explaining your app and how to use it.


# Make this as cool as you can!  If you want to make it harder try and make 'fuzzy' answers work (aka answer that should be right but don't match the answer string in the game perfectly)

from getpass import getpass
import json
import requests
import time
import base64

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"
endpoint_question = "/question"
url = "https://cae-bootstore.herokuapp.com/"

def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text
    
    
def login_user(user_name, password):
    auth_string=user_name+':'+password
    headers = {
        'Authorization': "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    user_data=requests.get(
        url + endpoint_login,
        headers = headers
    )
    return user_data.json()


def new_question():
    question = input("Enter question: ")
    answer = input("Enter answer: ")
    quest_dict = {
        "question": question,
        "answer": answer 
    }
    question_json_create = json.dumps(quest_dict)
    response = requests.post(url + endpoint_question, 
    data=question_json_create)
    if response.ok:
        print("Success!")
    else:
        print("No, No! Donkey brain!")

def delete_question():
    del()
def view_question():
    print (question_json_create)
    



print(login_user('scroogducke@gmail.com','1a2b3c45'))

def login(email):
    password=getpass("Password: ")
    user=login_user(email, password)
    return user
def register():
    print("Registration:")
    email=input("Email: ")
    f_name=input("First Name: ")
    l_name=input("Last Name: ")
    password=getpass("Password: ")
    user_dict={
        "email":email,
        "f_name":f_name,
        "l_name":l_name,
        "password":password,
        "status": "user"
    }
    if email == "kevinr4839@gmail.com":
        user_dict["status"] = "admin"
    return register_user(user_dict)





def main():
    while True:
        print("Welcome to the Bookstore")
        email = input("Enter your email to Login. Register by tpying 'register' ")
        if email == 'register':
            registeredOK = register()
            if registeredOK:
                print("You have successfully registered")
                continue
            else:
                print("Error, please try again")
                continue
        elif email.lower() == "quit":
            print("Don't come back.")
            break
        else:
            try:
                login(email)
            except:
                print("Invalid Username/Password")
                continue
        if email == "kevinr4839@gmail.com":
            print ("Admin")
            print ("""
Admin Options:
1. Create Question
2. Delete Question
3. View My Questions
            """)
       

            option = input("What would you like to do?")
            if option == "1":
                new_question()
            if option == "2":
                delete_question()
            if option == "3": 
                view_question()
        
        else:
            print ("User")
            return