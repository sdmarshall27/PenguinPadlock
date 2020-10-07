from tkinter import *


def login():
    login_screen = Toplevel(app)
    login_screen.title("Login")
    login_screen.geometry("620x300")

    username = StringVar()
    password = StringVar()

    Label(login_screen, text="Please enter your login credentials below").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username: ").pack()
    Entry(login_screen, textvariable=username)
    Label(login_screen, text="Password: ").pack()
    Entry(login_screen, textvariable=password)


def register():
    register_screen = Toplevel(app)
    register_screen.title("Login")
    register_screen.geometry("620x300")


def main_account_screen():
    global app
    app = Tk()
    app.title("Penguin Padlock")
    app.geometry("1240x720")

    Label(text="Welcome to Penguin Padlock!", height="2", width="720",
          bg="red", font=("Calibri", 32)).pack()
    Label(text="", height=10).pack()

    Button(text="Login", font=("Calibri", 24), height=2, width=25,
           command=login).pack()
    Label(text="", height=2).pack()
    Button(text="Register", font=("Calibri", 24), height=2, width=25,
           command=register).pack()

    app.mainloop()


main_account_screen()
