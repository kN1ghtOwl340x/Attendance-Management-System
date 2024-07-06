import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon

pw = ""
usernameList = []

#===============creating a basic admin table==========================
try:
    conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
    cur = conn.cursor()
    cur.execute("create table admin_data(username varchar(100) PRIMARY KEY, passwd varchar(100))")
    cur.execute("insert into admin_data(username, passwd) values('admin', '123')")
    conn.commit()
    conn.close()

except:
    pass

#================accessing the admin username====================
try:
    conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
    cur = conn.cursor()
    cur.execute("select * from admin_data")
    admindata = cur.fetchall()
    #print(admindata)
    for data in admindata:
        usernameList.append(data[0])
    #print(usernameList)
except Exception as error:
    print(error)

class Admin_Login_Student:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Admin Login")

#===============Variable for admin login============
        self.userVar = tk.StringVar()
        self.passVar = tk.StringVar()

        self.title = tk.Label(self.root, text="Admin Login", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        self.title.pack(side="top", fill="x")

        self.loginFrame = tk.Frame(self.root, bg="grey", bd=3, relief="raised", height=300, width=550)
        self.loginFrame.place(x=75, y=75)

        self.username = tk.Label(self.loginFrame, text="Username: ", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        self.usernameEntry = tk.Entry(self.loginFrame, fg="white", textvariable=self.userVar, bd=0, font=("Times new roman", 18, "bold"))
        self.password = tk.Label(self.loginFrame, text="Password", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        self.passwordEntry = tk.Entry(self.loginFrame, fg="white", textvariable=self.passVar, bd=0, show="*", font=("Times new roman", 18, "bold"))

        self.username.place(x=150, y=80)
        self.usernameEntry.place(x=260, y=80, width=146)
        self.password.place(x=150, y=120)
        self.passwordEntry.place(x=260, y=120, width=146)

        self.enterButton = tk.Button(self.loginFrame, text="Enter", fg="black", font=("times new roman", 18, "bold"), width=10, command=self.adminLogin)
        self.enterButton.place(x=220, y=220)

        self.root.mainloop()

    def adminLogin(self):
        username = self.usernameEntry.get()
        passwd = self.passwordEntry.get()
        if username in usernameList:
            #print("present")
            conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
            cur = conn.cursor()
            cur.execute("select * from admin_data")
            admindata = cur.fetchall()
            for i in admindata:
                if(i[0] == username):
                    realPasswd = i[1]
                    break
            if(realPasswd == passwd):
                print("correct")
            else:
                messagebox.showinfo("Error!!", "Invalid  Password")
        else:
            messagebox.showinfo("Error!!", "Please enter correct username and password")


m = Admin_Login_Student()