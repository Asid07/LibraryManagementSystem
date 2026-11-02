from tkinter import *
import sqlite3

def member_screen():

    win=Toplevel()

    win.title("Members")
    win.geometry("700x500")

    Label(win,text="Member ID").grid(row=0,column=0)
    Label(win,text="Name").grid(row=1,column=0)
    Label(win,text="Email").grid(row=2,column=0)

    id_entry=Entry(win)
    name_entry=Entry(win)
    email_entry=Entry(win)

    id_entry.grid(row=0,column=1)
    name_entry.grid(row=1,column=1)
    email_entry.grid(row=2,column=1)

    def insert():

        conn=sqlite3.connect("library.db")
        cur=conn.cursor()

        cur.execute("""
        INSERT INTO MEMBER
        VALUES(?,?,?, '', '', '')
        """,(id_entry.get(),
             name_entry.get(),
             email_entry.get()))

        conn.commit()
        conn.close()

        show()

    def show():

        listbox.delete(0,END)

        conn=sqlite3.connect("library.db")
        cur=conn.cursor()

        cur.execute("SELECT * FROM MEMBER")

        rows=cur.fetchall()

        for row in rows:
            listbox.insert(END,row)

        conn.close()

    def delete():

        conn=sqlite3.connect("library.db")
        cur=conn.cursor()

        cur.execute(
        "DELETE FROM MEMBER WHERE Member_ID=?",
        (id_entry.get(),))

        conn.commit()
        conn.close()

        show()

    def update():

        conn=sqlite3.connect("library.db")
        cur=conn.cursor()

        cur.execute("""
        UPDATE MEMBER
        SET Member_Name=?, Email=?
        WHERE Member_ID=?
        """,
        (
        name_entry.get(),
        email_entry.get(),
        id_entry.get()
        ))

        conn.commit()
        conn.close()

        show()

    def search():

        listbox.delete(0,END)

        conn=sqlite3.connect("library.db")
        cur=conn.cursor()

        cur.execute("""
        SELECT * FROM MEMBER
        WHERE Member_Name LIKE ?
        """,('%'+name_entry.get()+'%',))

        rows=cur.fetchall()

        for row in rows:
            listbox.insert(END,row)

        conn.close()

    Button(win,text="Insert",
           command=insert).grid(row=3,column=0)

    Button(win,text="Update",
           command=update).grid(row=3,column=1)

    Button(win,text="Delete",
           command=delete).grid(row=3,column=2)

    Button(win,text="Search",
           command=search).grid(row=3,column=3)

    Button(win,text="View All",
           command=show).grid(row=3,column=4)

    listbox=Listbox(win,width=80)
    listbox.grid(row=5,column=0,columnspan=5)

    show()