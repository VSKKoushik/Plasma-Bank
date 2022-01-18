from tkinter import *
import sqlite3
import webbrowser
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def empty():
    root = Tk()
    root.geometry('0x0+0+0')
    root.resizable(False,False)
    login()
    root.mainloop()

#LOGIN PAGE
def login():
    root = Toplevel()
    root.geometry('1280x680+42+5')
    root.configure(background = "#bab6d0")
    root.resizable(False,False)
    root.title("LOGIN PAGE")
    C = Canvas(root, bg="blue", height=200, width=300)
    filename = PhotoImage(file = "C:\\Users\\gs858\\Downloads\\Login.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    Username = StringVar()
    Passwords = StringVar()
    def database():
        name111 = Username.get()
        psswd111 = Passwords.get()
        conn = sqlite3.connect('LOGIN.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS plasmalogin (Username TEXT,Passwords TEXT)')
        cursor.execute('INSERT INTO plasmalogin (Username,Passwords) VALUES(?,?)', (name111, psswd111))
        conn.commit()
    label_1 = Label(root, text="LOGIN", width=15,font=('Comic Sans MS',15),bg="#000000",fg="#49ff00")
    label_1.place(x=650, y=220)
    entry_2 = Entry(root, textvar=Username,width=20,font=60)
    entry_2.place(x=750, y=301.5)
    entry_3= Entry(root, textvar=Passwords,show="*",width=20,font=60)
    entry_3.place(x=750, y=433)
    Button(root,text='Submit',font=('Comic Sans MS',15), width=20,bg='#90e3dd', command=lambda: [database(),root.destroy(),home()]).place(x=630, y=557)
    Button(root,text='Not Registered?Sign-up',font=('Comic Sans MS',12),borderwidth=0, width=20, command=lambda:[root.destroy(),reg()],bg='#ffffff',fg='#1501a5').place(x=210, y=566)
    root.mainloop()

#REGISTRATION PAGE
def reg():
    root = Toplevel()
    root.geometry('1180x680+90+5')
    root.configure(background="#bab6d0")
    root.resizable(False, False)
    root.title("REGISTRATION PAGE")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file="C:\\Users\\gs858\\Downloads\\Register.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    Fullname = StringVar()
    Password = StringVar()
    Retype = StringVar()
    Mobilenumber = StringVar()
    Email = StringVar()
    var = IntVar()
    def database1():
        name1 = Fullname.get()
        psswd = Password.get()
        repsswd = Retype.get()
        mbno = Mobilenumber.get()
        email = Email.get()
        gender = var.get()
        conn = sqlite3.connect('REGISTRATION.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS plasmaban(Fullname TEXT,Password TEXT,Retype TEXT,Mobilenumber TEXT,Email TEXT,Gender TEXT)')
        cursor.execute('INSERT INTO plasmaban(FullName,Password,Retype,Mobilenumber,Email,Gender) VALUES(?,?,?,?,?,?)',
                       (name1, psswd, repsswd, mbno, email, gender))
        conn.commit()
    entry_1 = Entry(root, textvar=Fullname, width=30, font=50)
    entry_1.place(x=550, y=150)
    entry_2 = Entry(root, textvar=Password, show="*", width=30, font=50)
    entry_2.place(x=550, y=214)
    entry_3 = Entry(root, textvar=Retype, show="*", width=30, font=50)
    entry_3.place(x=550, y=305)
    entry_3 = Entry(root, textvar=Mobilenumber, width=30, font=50)
    entry_3.place(x=550, y=386)
    entry_4 = Entry(root, textvar=Email, width=30, font=50)
    entry_4.place(x=550, y=465)
    Radiobutton(root, text="Male", padx=5, variable=var, value=1, font=("Comic Sans MS", 20), bg="black",
                fg="#fb9f12").place(x=550, y=523)
    Radiobutton(root, text="Female", padx=20, variable=var, value=2, font=("Comic Sans MS", 20), bg="black",
                fg="#fb9f12").place(x=650, y=523)
    Button(root, text='Submit', width=15, font=('Comic Sans MS', 15), borderwidth=0, bg='#13ece6',command=lambda: [database1(),root.destroy(),login()]).place(x=500, y=580)
    root.mainloop()
