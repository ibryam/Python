from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Warning", message="Please make sure to fill in all the empty fields!")
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"Details entered:\n\nWebsite: {website},\nEmail: {email}, \nPassword: {password}\n\n Press 'OK' to save or 'Cancel' to restart! ")

        if is_ok:
            with open("data.txt", "a") as d:
                d.write(f"Website: {website},\nEmail: {email}, \nPassword: {password}\n\n")
                website_box.delete(0,END)
                password_box.delete(0, END)




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
website_box = Entry(width= 35)

website_box.grid(column = 1, row = 1, columnspan = 2)
website_box.focus()



# creating "Email/Username" label
email_label = Label(text = "Email/Username: ",
                      font = (FONT_NAME, FONT_SIZE, "normal"))
email_label.grid(column = 0,
                   row = 2)
# creating "Email/Username" box
email_box = Entry(width= 35)
email_box.insert(0,"ibryamfibryam@gmail.com")

email_box.grid(column = 1, row = 2, columnspan = 2)




# creating "Password" label
password_label = Label(text = "Password: ",
                      font = (FONT_NAME, FONT_SIZE, "normal"))
password_label.grid(column = 0,
                   row = 3)
# creating "Password" box
password_box = Entry(width= 17)

password_box.grid(column = 1, row = 3)






#creating "Generate password" button

generate_password = Button(text = "Generate Password", command=generate_password)
generate_password.grid(column = 2, row = 3)





#creating "Add" button
add = Button(text = "Add", width=30, command=save)
add.grid(column = 1, row = 4, columnspan = 2)





window.mainloop()