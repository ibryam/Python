from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Helvetica"
FONT_SIZE = 10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for l in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(2,4))]
    password_numbers = [choice(numbers) for n in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_box.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_box.get()
    email = email_box.get()
    password = password_box.get()
    new_data = {
        website:{
        "email": email,
        "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please make sure to fill in all the empty fields!")
    else:
        try:
            with open("data.json", "r") as d:
                 #reading old data
                 data = json.load(d)
        except FileNotFoundError:
            with open("data.json", "w") as d:
                json.dump(new_data, d, indent = 4)
        else:
             #update old data with new data
             data.update(new_data)

             with open("data.json", "w") as d:
                 #saving updated data
                 json.dump(data, d, indent = 4)
        finally:
             website_box.delete(0,END)
             password_box.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website= website_box.get()
    try:
        with open("data.json") as d:
            data = json.load(d)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No records found for {website}.")





# ---------------------------- UI SETUP ------------------------------- #

# creating the Password manager config
window = Tk()
window.title("Password Manager")
window.config(padx=50,
              pady= 50)
canvas = Canvas(width=200,
                height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100,
                    image=photo)
canvas.grid(column= 1, row = 0)


# creating "Website" label
website_label = Label(text = "Website: ",
                      font = (FONT_NAME, FONT_SIZE, "normal"))
website_label.grid(column = 0,
                   row = 1)
# creating "Website" box
website_box = Entry(width= 17)

website_box.grid(column = 1, row = 1, columnspan = 1)
website_box.focus()


# creating "Email/Username" label
email_label = Label(text = "Email/Username: ",
                      font = (FONT_NAME, FONT_SIZE, "normal"))
email_label.grid(column = 0,
                   row = 3)
# creating "Email/Username" box
email_box = Entry(width= 35)
email_box.insert(0,"ibryamfibryam@gmail.com")

email_box.grid(column = 1, row = 3, columnspan = 2)


# creating "Password" label
password_label = Label(text = "Password: ",
                      font = (FONT_NAME, FONT_SIZE, "normal"))
password_label.grid(column = 0,
                   row = 4)
# creating "Password" box
password_box = Entry(width= 17)

password_box.grid(column = 1, row = 4)

#creating "Generate password" button

generate_password = Button(text = "Generate Password", command=generate_password)
generate_password.grid(column = 2, row = 4)


#creating "Add" button
add = Button(text = "Add", width=30, command=save)
add.grid(column = 1, row = 5, columnspan = 2)

#creating "Search" button
search= Button(text = "Search", width= 14, command = find_password)
search.grid(column = 2, row = 1)



window.mainloop()