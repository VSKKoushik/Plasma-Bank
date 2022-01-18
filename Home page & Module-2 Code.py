#HOME PAGE
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

#DONOR PAGE
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
