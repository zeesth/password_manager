from random import choice, sample, randint
from tkinter import messagebox, END
import json

def generator():
    #   Creates a list of characters to choose from
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ''

    #   Chooses the quantity of each character, limiting the password lenght to 16
    letters_n = randint(4,8)
    numbers_n = randint(4,(15 - letters_n))
    symbols_n = 16-letters_n - numbers_n

    #   Chooses each type of character randomly from the lists
    letters = [choice(letters_list) for i in range(letters_n)]
    numbers = [choice(numbers_list) for i in range(numbers_n)]
    symbols = [choice(symbols_list) for i in range(symbols_n)]

    password = letters + numbers + symbols

    #   Reorganizes the choosen characteres and returns
    password = sample(password, len(password))
    password_result = ''.join(password)
    
    return password_result
    
def generator():
    #   Creates a list of characters to choose from
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_n = randint(4,8)
    numbers_n = randint(4,(15 - letters_n))
    symbols_n = 16-letters_n - numbers_n

    #   Chooses each type of character randomly from the lists
    letters = [choice(letters_list) for i in range(letters_n)]

    numbers = [choice(numbers_list) for i in range(numbers_n)]
        
    symbols = [choice(symbols_list) for i in range(symbols_n)]

    password = letters + numbers + symbols
    #   Reorganizes the choosen characteres and returns
    password = sample(password, len(password))
    password_result = ''.join(password)
    
    return password_result
    
    
def save(website_entry, login_entry, password_entry):
    #   Saves each value given by the user in a variable
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    
    new_account = {
        website: {
            "login": login,
            "password": password,
        }
    }
    
    #   Checks if all values were filled
    if website == "" or login == "" or password == "":
        messagebox.showinfo(title="Error", message="Please fill all fields.")
    else:
        try:
            #   Loads the data, updates and then writes it again
            with open("Python/100 Days of Code/Intermediate/Projects/Password Manager/data.json", "r") as data_json:
                data = json.load(data_json)
                data.update(new_account)
            with open("Python/100 Days of Code/Intermediate/Projects/Password Manager/data.json", "w") as data_json:
                json.dump(data, data_json, indent=4)
            
        except:
            #   If the file doesn't exist or is empty, creates and fill it
            with open("Python/100 Days of Code/Intermediate/Projects/Password Manager/data.json", "w") as data_json:
                json.dump(new_account, data_json, indent=4)
                
        finally:
            #   Clears all fields after the function is done
            website_entry.delete(0, END)
            login_entry.delete(0, END)
            login_entry.insert(0, "vitor.gracindo@hotmail.com")
            password_entry.delete(0, END)

def search(website_entry):
    website = website_entry.get()
    
    #   Retrieves the stored data
    with open("Python/100 Days of Code/Intermediate/Projects/Password Manager/data.json", "r") as data_json:
        data_stored = json.load(data_json)
        
    #   Searches for the credentials for the specified website
    login = data_stored[website]["login"]
    password = data_stored[website]["password"]
    messagebox.showinfo(title=f"{website} account", message=f"Login: {login}\nPassword: {password}")
    
