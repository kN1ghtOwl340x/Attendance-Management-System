import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon

#(pw = "<password>") -> entry your mysql root password 
pw = ""

#A list containing all the id of teacher
teacherIdList = []

#==================Accessing all the teacher id=================
try:
    conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
    cur = conn.cursor()
    cur.execute("select * from Teacher_data")
    teacherdata = cur.fetchall()
    #print(teacherdata)
    for data in teacherdata:
        teacherIdList.append(data[0])
    #print(teacherIdList)
except Exception as error:
    print(error)

class Teacher_Login:
    def __init__(self):
        self.root = tk.Tk()#tk.Toplevel()
        self.root.geometry("700x400+0+0")
        self.root.title("Teacher Login")

#===============Variable for admin login============
        self.teacherIdVar = tk.StringVar()
        self.teacherPassVar = tk.StringVar()

        self.title = tk.Label(self.root, text="Teacher Login", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        self.title.pack(side="top", fill="x")

        self.loginFrame = tk.Frame(self.root, bg="grey", bd=3, relief="raised", height=300, width=550)
        self.loginFrame.place(x=75, y=75)

        self.teacherId = tk.Label(self.loginFrame, text="Teacher Id: ", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        self.teacherIdEntry = tk.Entry(self.loginFrame, fg="white", textvariable=self.teacherIdVar, bd=0, font=("Times new roman", 18, "bold"))
        self.password = tk.Label(self.loginFrame, text="Password", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        self.passwordEntry = tk.Entry(self.loginFrame, fg="white", textvariable=self.teacherPassVar, bd=0, show="*", font=("Times new roman", 18, "bold"))

        self.teacherId.place(x=150, y=80)
        self.teacherIdEntry.place(x=260, y=80, width=146)
        self.password.place(x=150, y=120)
        self.passwordEntry.place(x=260, y=120, width=146)

        self.enterButton = tk.Button(self.loginFrame, text="Enter", fg="black", font=("times new roman", 18, "bold"), width=10, command=self.teacherLogin)
        self.enterButton.place(x=220, y=220)

        self.root.mainloop()

#===============checking teacher id and password============================
    def teacherLogin(self):
        id = self.teacherIdVar.get()
        passwd = self.teacherPassVar.get()
        if id in teacherIdList:
            #print("present")
            conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
            cur = conn.cursor()
            cur.execute("select * from Teacher_data")
            teacherdata = cur.fetchall()
            conn.commit()
            conn.close()
            for i in teacherdata:
                if(i[0] == id):
                    realpasswd = i[2]
                    break
            if(realpasswd == passwd):
                print("correct")

            else:
                messagebox.showinfo("Error!!", "Invalid  Password")
        else:
            messagebox.showinfo("Error!!", "Please enter correct Id and password")


Teacher_Login()