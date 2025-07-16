from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("SignUp")
window.geometry("900x480")
window.configure(bg="lightblue")
window.resizable(False, False)

img = PhotoImage(file="Python/digitalWhiteBoard/image.png")
Label(window, image=img, border=0, bg="white").place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="Sign up", fg="black", bg="white", font=("Microsoft YaHei UI Light", 30, "bold"))
heading.place(x=100, y=5)

# Username input
def on_username_enter(e):
    if username_entry.get() == "Username":
        username_entry.delete(0, 'end')
        username_entry.config(fg="black")

def on_username_leave(e):
    if username_entry.get() == "":
        username_entry.insert(0, "Username")
        username_entry.config(fg="grey")

username_label = Label(frame, text="Username", bg="white", fg="black", font=("Microsoft YaHei UI Light", 12, "bold"))
username_label.place(x=30, y=60)
username_entry = Entry(frame, width=25, fg="grey", borderwidth=0, highlightthickness=0, bg="white", font=("Microsoft YaHei UI Light", 11))
username_entry.place(x=30, y=90)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", on_username_enter)
username_entry.bind("<FocusOut>", on_username_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=120)

# Password input
def on_password_enter(e):
    if password_entry.get() == "Password":
        password_entry.delete(0, 'end')
        password_entry.config(show="*", fg="black")

def on_password_leave(e):
    if password_entry.get() == "":
        password_entry.insert(0, "Password")
        password_entry.config(show="", fg="grey")

password_label = Label(frame, text="Password", bg="white", fg="black", font=("Microsoft YaHei UI Light", 12, "bold"))
password_label.place(x=30, y=140)
password_entry = Entry(frame, width=25, fg="grey", borderwidth=0, highlightthickness=0, bg="white", font=("Microsoft YaHei UI Light", 11))
password_entry.place(x=30, y=170)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", on_password_enter)
password_entry.bind("<FocusOut>", on_password_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=200)



window.mainloop()