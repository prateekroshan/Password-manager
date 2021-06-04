# saving data in json format

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# password generating mechanism
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# save password


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    website_data = {
        website: {
            "Email": email,
            "Password": password,

        }

    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="WARNING", message="YOU HAVE EMPTY FIELD")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(website_data, file, indent=4)
            # then update it using new data
        else:
            data.update(website_data)

            # write into the data.json
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message=f"NO DATA FILE FOUND !!")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=f"{website}", message=f"Your Details \n Email : {email} \n Password :{[password]} ")
        else:
            messagebox.showinfo(title="ERROR", message=f"{website} NOT FOUND!!")

# UI SETUP


window = Tk()
window.title("PASSWORD MANAGER🚀🚀🚀")
window.maxsize(width=700, height=400)
window.config(padx=50, pady=50, bg="skyblue")

canvas = Canvas(height=200, width=200, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", highlightthickness=0)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", highlightthickness=0)
email_label.grid(row=2, column=0)

# not needed ->
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
website_entry.focus()
email_entry = Entry(width=30)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "prateekmahapatra1@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password ->", command=generate_password)
generate_password_button.grid(row=3, column=0)
add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()
