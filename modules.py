from random import choice, sample, randint
from tkinter import messagebox, END

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
    
    
def save(website_entry, user_entry, password_entry):
    #   Saves each value given by the user in a variable
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    
    #   Checks if all values were filled
    if website == "" or user == "" or password == "":
        messagebox.showinfo(title="Error", message="Please fill all fields.")
    #   Confirms if the user filled the right values
    else:
        sure = messagebox.askokcancel(title=website, message=f"Are you sure you want to save these details? \nEmail: {user} \nPassword: {password} \n")
        #   Writes the account information and clears all fields
        if sure:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {user} | {password}\n")
            
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            user_entry.insert(0, "vitor.gracindo@hotmail.com")
            password_entry.delete(0, END)
        else:
            pass
