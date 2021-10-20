from tkinter import *
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=2)

# Label
label_website = Label(text="Website:", font=(FONT_NAME, 12))
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:", font=(FONT_NAME, 12))
label_email.grid(row=2, column=0)
label_password = Label(text="Password:", font=(FONT_NAME, 12))
label_password.grid(row=3, column=0)


window.mainloop()