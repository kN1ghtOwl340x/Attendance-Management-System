import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon
pw = ""


class Check_Attendence:
    def __init__(self):   
        self.root = tk.Tk()
        self.root.geometry("700x400+0+0")
        self.root.title("Attendence")

        self.title = tk.Label(self.root, text="Check Attendence", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        self.title.pack(side="top", fill="x")

#======================Frame for Login=================================
        self.option = tk.Frame(self.root, bg="grey", bd=3, relief="raised")
        self.option.place(x=75, y=75, height=300, width=550)

#======================Login============================================
        self.rollNo = tk.Label(self.option, text="Roll No: ", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        self.rollNoEntry = tk.Entry(self.option, fg="white", bd=0, font=("Times new roman", 18, "bold"))
        self.semester = tk.Label(self.option, text="Semester: ", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        self.semesterEntry = ttk.Combobox(self.option, font=("times new roman", 18), state="readonly", width=13)
        self.semesterEntry['values'] = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        #self.dob = tk.Label(self.option, text="D.O.B: ", bg="grey", fg="black", font=("Times new roman", 18, "bold"))
        #self.dobEntry = tk.Entry(self.option, fg="white", bd=0, font=("Times new roman", 18, "bold"))

        self.rollNo.place(x=150, y=80)
        self.rollNoEntry.place(x=260, y=80, width=146)
        self.semester.place(x=150, y=120)
        self.semesterEntry.place(x=260, y=120)
        #self.dob.place(x=150, y=160)
        #self.dobEntry.place(x=260, y=160, width=146)

#=====================Button for submit================================
        self.submitButton = tk.Button(self.option, text="Submit", fg="black", font=("times new roman", 18, "bold"), width=10, command=self.submitButto)
        self.submitButton.place(x=220, y=220)
        self.root.mainloop()

    def check(self, no, nam, present, totalClass, percent):
        root = tk.Tk()
        root.geometry("800x300+0+0")
        root.title("Attendence")

        title = tk.Label(root, text="Check Attendence", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        title.pack(side="top", fill="x")

#=====================Frame for Attendence information=====================================
        attendenceInformation = tk.Frame(root, bg="grey")
        attendenceInformation.pack(fill="both", expand=1)

#======================Label for Attendence information=====================================
        rollNo = tk.Label(attendenceInformation, text="Roll No: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        name = tk.Label(attendenceInformation, text="Name: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        totalClasses = tk.Label(attendenceInformation, text="Total Classes: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        totalAttend = tk.Label(attendenceInformation, text="Total Attendence: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        percentage = tk.Label(attendenceInformation, text="Percentage: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))


        rollNo.grid(row=0, column=0, padx=20, pady=10)   
        name.grid(row=0, column=2, padx=20, pady=10)   
        totalClasses.grid(row=1, column=0, padx=20, pady=10)   
        totalAttend.grid(row=1, column=2, padx=20, pady=10)   
        percentage.grid(row=2, column=1, pady=30, sticky="e")   

#========================Entry for Attendence information=====================================
        rollNoEntry = tk.Entry(attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        nameEntry = tk.Entry(attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        totalClassesEntry = tk.Entry(attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        totalAttendEntry = tk.Entry(attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        percentageEntry = tk.Entry(attendenceInformation, fg="white", font=("Times new roman", 18, "bold"), width=10)

        rollNoEntry.grid(row=0, column=1)
        nameEntry.grid(row=0, column=3)
        totalClassesEntry.grid(row=1, column=1)
        totalAttendEntry.grid(row=1, column=3)
        percentageEntry.grid(row=2, column=2, sticky="w")

        rollNoEntry.insert(0, no)
        nameEntry.insert(0, nam)
        totalClassesEntry.insert(0, totalClass)
        totalAttendEntry.insert(0, present)
        percentageEntry.insert(0, percent)


        rollNoEntry.config(state="disabled")
        nameEntry.config(state="disabled")
        totalClassesEntry.config(state="disabled")
        totalAttendEntry.config(state="disabled")
        percentageEntry.config(state="disabled")

#=======================Done button for Attendence information=====================================
        done = tk.Button(attendenceInformation, text="DONE", width=10, font=("Times new roman", 18, "bold"), command=root.destroy)
        done.grid(row=3, columnspan=4)


#===========Buttuon to show Attendence=================
    def submitButto(self):
        rollNo = self.rollNoEntry.get()
        semester = self.semesterEntry.get()
        #dob = self.dobEntry.get()

        if(rollNo=="" or semester==""):
            messagebox.showinfo("Error!!", "Please Enter all the fields.")
        else:
            conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
            cur = conn.cursor()
            cur.execute("select Roll_No from Student_Data")
            rollNoList = cur.fetchall()
            newList = []
            for roll in rollNoList:
                newList.append(roll[0])
            if rollNo in newList:
                cur.execute("select * from Student_Data where Roll_No="+rollNo)
                data = cur.fetchall()
                #print(data)
                conn.commit()
                conn.close()

                rollNo = data[0][0]
                name = data[0][1]
                totalClass = data[0][14]
                present = data[0][13]
                percentage = data[0][15]
                self.check(rollNo, name, present, totalClass, percentage)

            else:
                messagebox.showinfo("Error!!", "Roll no does not exist.")



Check_Attendence()