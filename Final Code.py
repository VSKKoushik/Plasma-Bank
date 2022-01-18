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


def home():
    root = Toplevel()
    root.geometry('1180x680+90+5')
    root.configure(background="#bab6d0")
    root.resizable(False, False)
    root.title("HOMEPAGE")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file="C:\\Users\\gs858\\Downloads\\Home.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    def site():
        webbrowser.open("https://www.redcrossblood.org/donate-blood/dlp/plasma-information.html")
    Button(root, text='DONATE PLASMA', width=20, font=('Kristen ITC', 15), bg="black", fg="white", borderwidth=0,command=lambda: [root.destroy(),donor()]).place(
        x=650, y=32)
    Button(root, text='PLASMA REQUIRED', width=20, font=('Kristen ITC', 15), bg="black", fg="white",
           borderwidth=0,command=lambda: [root.destroy(),reciever()]).place(x=920, y=32)
    Button(root, text='WANT TO KNOW ABOUT PLASMA?', width=30, font=('Kristen ITC', 15), bg="black", fg="white",
           borderwidth=0, command=lambda: [site()]).place(x=0, y=32)
    root.mainloop()


def donor():
    root = Toplevel()
    root.geometry('1200x680+90+5')
    root.configure(background = "#bab6d0")
    root.resizable(False,False)
    root.title("DONOR PAGE")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "C:\\Users\\gs858\\Downloads\\Donor.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    Fullname = StringVar()
    Age = StringVar()
    State = StringVar()
    Mobilenumber = StringVar()
    Email = StringVar()
    blgr = StringVar()
    def database2():
        name1 = Fullname.get()
        aj=Age.get()
        Sta = State.get()
        mbno = Mobilenumber.get()
        email = Email.get()
        blood= blgr.get()
        conn = sqlite3.connect('DONOR.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS donordet(Fullname TEXT,Age TEXT,State TEXT,bloodgroup TEXT,Mobilenumber TEXT,Email TEXT)')
        cursor.execute('INSERT INTO donordet(FullName,Age,State,bloodgroup,Mobilenumber,Email) VALUES(?,?,?,?,?,?)',(name1,aj,Sta,blood,mbno,email))
        conn.commit()
    entry_1 = Entry(root, textvar=Fullname,width=30,font=50)
    entry_1.place(x=550, y=150)
    entry_2 = Entry(root, textvar=Age,width=30,font=50)
    entry_2.place(x=550, y=222)
    list2 = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
             'Chhattisgarh', 'Dadra and Nagar Haveli and Daman&Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana',
             'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
             'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
             'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh',
             'West Bengal'];
    droplist = OptionMenu(root, State, *list2)
    droplist.config(width=33, font=('Comic Sans MS', 8), borderwidth=0)
    State.set('Select state')
    droplist.place(x=550, y=287)
    list1 = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-', 'OTHERS'];
    droplist = OptionMenu(root, blgr, *list1)
    droplist.config(width=33,font=('Comic Sans MS',8),borderwidth=0)
    blgr.set('Select bloodgroup')
    droplist.place(x=550, y=356)
    entry_5 = Entry(root, textvar=Email,width=30,font=50)
    entry_5.place(x=550, y=424)
    entry_6 = Entry(root, textvar=Mobilenumber,width=30,font=50)
    entry_6.place(x=550, y=495)
    Button(root, text='Submit', width=15, font=('Comic Sans MS',15),borderwidth=0,bg='#13ece6', command=lambda: [database2(),root.destroy(),home()]).place(x=500, y=560)
    Button(root, text='HOME', width=15, font=('Kristen ITC',15),borderwidth=0,bg='black',fg='white', command=lambda: [root.destroy(),home()]).place(x=0, y=0)
    root.mainloop()


def reciever():
    root = Toplevel()
    root.geometry('1156x672+90+5')
    root.title("RECIEVER PAGE")
    root.resizable(False, False)
    root.configure(background="#bab6d0")
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = PhotoImage(file="C:\\Users\\gs858\\Downloads\\Request.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    Rmail = StringVar()
    Rpswrd = StringVar()
    Rsender = StringVar()
    Rsubject = StringVar()
    emailE = Entry(root, width=28, textvariable=Rmail, font=30)
    emailE.place(x=580, y=173)
    passwordE = Entry(root, width=28, show="*", textvariable=Rpswrd, font=30)
    passwordE.place(x=580, y=223)
    senderE = Entry(root, width=28, textvariable=Rsender, font=30)
    senderE.place(x=580, y=273)
    subjectE = Entry(root, width=28, textvariable=Rsubject, font=30)
    subjectE.place(x=580, y=330)
    msgbodyE = Text(root, width=31, height=10)
    msgbodyE.place(x=580, y=380)

    def sendemail():
        try:
            mymsg = MIMEMultipart()
            mymsg['From'] = str(Rmail.get())
            mymsg['To'] = str(Rsender.get())
            mymsg['Subject'] = str(Rsubject.get())
            mymsg.attach(MIMEText(msgbodyE.get(1.0, 'end'), 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(str(Rmail.get()), str(Rpswrd.get()))
            text = mymsg.as_string()
            server.sendmail(str(Rmail.get()), str(Rsender.get()), text)
            Label_6 = Label(root, text="Mail Sent", width=20, fg='green', font=("bold", 15), bg='black')
            Label_6.place(x=470, y=645)
            server.quit()
        except:
            Label_6 = Label(root, text="Unable to send", width=20, fg='red', font=("bold", 15), bg='black')
            Label_6.place(x=470, y=645)
    Button(root, text="Send", font=('Comic Sans MS', 15), width=15, bg='#32dcf4', command=lambda: [sendemail()]).place(x=485, y=570)
    def list():
        my_conn = sqlite3.connect('DONOR.db')
        my_w = Tk()
        my_w.geometry('744x695+300+5')
        my_w.resizable(False, False)
        my_w.configure(background="black")
        r_set = my_conn.execute('''SELECT * from donordet ORDER BY state''');
        i = 0  # row value inside the loop
        for plasmaban in r_set:
            for j in range(len(plasmaban)):
                e = Entry(my_w, width=20, bg="#fdff4c")
                e.grid(row=i, column=j)
                e.insert(END, plasmaban[j])
            i = i + 1
    Button(root, text='VIEW LIST OF DONORS', width=27, borderwidth=0, bg='#fff168', font=("Comic Sans MS", 15),
           command=list).place(x=410, y=90)
    Button(root, text='HOME', width=15, font=('Kristen ITC',15),borderwidth=0,bg='black',fg='white', command=lambda: [root.destroy(),home()]).place(x=0, y=0)
    root.mainloop()

empty()
