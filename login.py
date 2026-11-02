from tkinter import *
from dashboard import dashboard

def check():

    if user.get()=="admin" and password.get()=="123":

        root.destroy()
        dashboard()

def login_screen():

    global root,user,password

    root=Tk()
    root.title("Library Login")
    root.geometry("300x200")

    Label(root,text="Username").pack()

    user=Entry(root)
    user.pack()

    Label(root,text="Password").pack()

    password=Entry(root,show="*")
    password.pack()

    Button(root,text="Login",command=check).pack(pady=10)

    root.mainloop()