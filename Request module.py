#RECEIVER PAGE
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
