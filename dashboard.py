from tkinter import *
from members import member_screen

def dashboard():

    root=Tk()

    root.title("Dashboard")
    root.geometry("400x300")

    Label(root,text="Library Management System",
          font=("Arial",16)).pack(pady=20)

    Button(root,text="Manage Members",
           command=member_screen,
           width=20).pack()

    root.mainloop()