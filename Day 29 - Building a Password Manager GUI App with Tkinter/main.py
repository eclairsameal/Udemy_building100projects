from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """將資料寫入檔，寫入時會確認是否為空跟再次確認"""
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                string = website + " | " + email + " | " + password + "\n"
                # print(string)
                file.write(string)
                entry_website.focus()
                entry_website.delete(0, END)  # 刪除文字(範圍), END = 字尾
                entry_email.delete(0, END)
                entry_email.insert(0, "@gmail.com")
                entry_password.delete(0, END)


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
entry_website.focus()
entry_email = Entry(width=45)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "@gmail.com")  # 插入文字
entry_password = Entry(width=28)
entry_password.grid(row=3, column=1)

# Button
button_password = Button(text="Generate Password", highlightthickness=0)
button_password.grid(row=3, column=2)
button_add = Button(text="Add", width=45, command=save)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()