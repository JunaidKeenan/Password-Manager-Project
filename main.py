from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website_details = website_entry.get()
    email_details = email_entry.get()
    password_details = password_entry.get()

    if len(website_details) == 0 or len(password_details) == 0:
        messagebox.showwarning(title='Oops!', message='You did not fill in everything')
    else:
        is_ok = messagebox.askokcancel(title=website_details, message=f'These are the details: \n{email_details}'
                                                                      f'\n{password_details}\nIs it ok to save?')

        if is_ok:
            with open('data.txt', mode = 'a') as file:
                file.write(f'{website_details} | {email_details} | {password_details}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#Logo
canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
email_entry.insert(END, '@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w')

#Buttons
password_button = Button(text='Generate Password')
password_button.grid(column=2, row=3, sticky='w')

add_button = Button(text='Add', width=36, command=save_info)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()