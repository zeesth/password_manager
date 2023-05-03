from tkinter import *
from tkinter import messagebox
import modules

#   Calling the function to generate a random password
def call_generator():
    password_result = modules.generator()
    #   Clears the password field and enters the new one
    password_entry.delete(0, END)
    password_entry.insert(0, password_result)

#   Calling the function to save the user data
def call_save():
    modules.save(website_entry, user_entry, password_entry)

#   Seting up the app window
screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=15)
screen.geometry("580x400")

#   Creating the image to the window
canvas = Canvas(width=200, height=214, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 107, image=img)
canvas.place(x=180, y=20)

#   Creating the website entry space and its label
website_label = Label(text="Website:")
website_label.place(x=20, y=250)

website_entry = Entry(width=53)
website_entry.place(x=125, y= 250)
website_entry.focus()

#   Creating the email/username entry space and its label
user_label = Label(text="Email/Username:")
user_label.place(x=20, y=270)

user_entry = Entry(width=53)
user_entry.place(x=125, y=270)
user_entry.insert(0, "vitor.gracindo@hotmail.com")

#   Creating the password entry space and its label
password_label = Label(text="Password:")
password_label.place(x=20, y=290)

password_entry = Entry(width=34)
password_entry.place(x=125, y=290)

#   Creating the generate password button
gen_pas = Button(text="Generate Password", highlightthickness=0, command=call_generator)
gen_pas.place(x=373, y=287)

#   Creating the add button
add_button = Button(text="Add", width=50, command=call_save)
add_button.place(x=125, y=313)

screen.mainloop()
