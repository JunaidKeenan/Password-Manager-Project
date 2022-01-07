from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


#Logo
canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


#Labels
website_label = Label(text='Website:',font=('Arial',12))
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:', font=('Arial',12))
email_label.grid(column=0,row=2)

password_label = Label(text='Password:',font=('Arial',12))
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry(width=35, justify=LEFT)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w')

#Buttons
password_button = Button(text='Generate Password')
password_button.grid(column=2, row=3)

add_button = Button(width=36, text='Add')
add_button.grid(column=1, row=4, columnspan=2)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()