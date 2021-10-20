from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Label
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entry
entry_website = Entry(width=45)
entry_website.grid(row=1, column=1, columnspan=2)
entry_email = Entry(width=45)
entry_email.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=28)
entry_password.grid(row=3, column=1)

# Button
button_password = Button(text="Generate Password", highlightthickness=0)
button_password.grid(row=3, column=2)
button_add = Button(text="Add",width=45)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()