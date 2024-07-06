import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon
from PIL import ImageTk, Image

#(pw = "<password>") -> entry your mysql root password 
pw = ""

#A list containing all the name of admin users
usernameList = []

#A list containing all the id of teacher
teacherIdList = []

#=============Creating a Database AMS=======================
try:
	conn = mycon.connect(host="localhost", user="root", password=pw)
	cur = conn.cursor()
	cur.execute("Create database AMS")
	conn.commit()
	conn.close()
except:
	pass

#=================Creating a Table for Student data=================
try:
	conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
	cur = conn.cursor()
	cur.execute("Create Table Student_Data(Roll_no Varchar(100) PRIMARY KEY, Name Varchar(100), Course Varchar(20), Department Varchar(20), Year Varchar(10), Semester Varchar(10), Section Varchar(100), Gender Varchar(20), DOB Varchar(20), Email Varchar(50), Phone varchar(25), Mentor Varchar(30), Address Varchar (1000), Present int, Total_CLasses int, Attendence_Percentage float)")
	conn.commit()
	conn.close()
except Exception as error:
	pass

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

#================Creating a table for Teacher data=====================	
try:
	conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
	cur = conn.cursor()
	cur.execute("create table Teacher_Data(Teacher_Id varchar(100) PRIMARY KEY, Name Varchar(100), Passwd Varchar(100))")
	conn.commit()
	conn.close()

except Exception as error:
	pass

#==================Accessing all the teacher id=================
def teacherId():
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
teacherId()

#==============Manage Student Data====================================
class Manage_Student:
	def __init__(self):
		self.root = tk.Toplevel()
		self.root.geometry("1440x900+0+0")
		self.root.title("Manage Student Data")

		self.title = tk.Label(self.root, text="Manage Student Data", bd = 10, font=("Comic Sans MS", 35, "bold"), bg="white", fg="black")
		self.title.pack(side = "top", fill="x")

#=========================Varialbles=======================================================================
		self.courseVar = tk.StringVar()
		self.departmentVar = tk.StringVar()
		self.yearVar = tk.StringVar()
		self.semesterVar = tk.StringVar()

		self.nameVar = tk.StringVar()
		self.rollNoVar = tk.StringVar()
		self.sectionVar = tk.StringVar()
		self.genderVar = tk.StringVar()
		self.dobVar = tk.StringVar()
		self.emailVar = tk.StringVar()
		self.phoneVar = tk.StringVar()
		self.mentorVar = tk.StringVar()

#=================Frame for course Details================================================================
		self.Course_Frame = tk.LabelFrame(self.root, text="Course Detail", font=("times new roman", 13, "italic"))
		self.Course_Frame.place(x=12, y=80, width=550, height=150)

        #Lable for course
		self.course = tk.Label(self.Course_Frame, text="Course: ", font=("times new roman", 15, "bold"))
		self.department = tk.Label(self.Course_Frame, text="Department: ", font=("times new roman", 15, "bold"))
		self.year = tk.Label(self.Course_Frame, text="Year: ", font=("times new roman", 15, "bold"))
		self.semester = tk.Label(self.Course_Frame, text="Semester: ", font=("times new roman", 15, "bold"))

		self.course.grid(row=0, column=0, sticky="w", padx=10, pady=20)
		self.department.grid(row=0, column=2, sticky="w", padx=10, pady=20)
		self.year.grid(row=1, column=0, sticky="w", padx=10, pady=5)
		self.semester.grid(row=1, column=2, sticky="w", padx=10, pady=5)

        #Entry for course
		self.courseEntry = ttk.Combobox(self.Course_Frame, textvariable=self.courseVar, font=("times new roman", 13), state="readonly", width=18)
		self.courseEntry['values'] = ("B.Tech", "B.Sc", "B.E", "MBBS", "B.Pharm", "BCA", "B.Arch")
		self.departmentEntry = ttk.Combobox(self.Course_Frame, textvariable=self.departmentVar, font=("times new roman", 13), state="readonly", width=18)
		self.departmentEntry['values'] = ("CSE", "ME", "CE", "ECE", "IT", "EE")
		self.yearEntry = ttk.Combobox(self.Course_Frame, textvariable=self.yearVar, font=("times new roman", 13), state="readonly", width=18)
		self.yearEntry['values'] = ("1st", "2nd", "3rd", "4th")
		self.semesterEntry = ttk.Combobox(self.Course_Frame, textvariable=self.semesterVar, font=("times new roman", 13), state="readonly", width=18)
		self.semesterEntry['values'] = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
		self.reset = tk.Button(self.Course_Frame, text="Reset", font=("bold"), command=self.resetCommand)

		self.courseEntry.grid(row=0, column=1, sticky="w")
		self.departmentEntry.grid(row=0, column=3, sticky="w")
		self.yearEntry.grid(row=1, column=1, sticky="w")
		self.semesterEntry.grid(row=1, column=3, sticky="w")
		self.reset.grid(row=2, columnspan=4)


#=====================Frame for Student===================================================================== 
		self.Student_Frame = tk.LabelFrame(self.root, text="Student Detail", font=("times new roman", 13, "italic"))
		self.Student_Frame.place(x=12, y=240, width=550, height=590)

        #Label for Student Detail
		self.name = tk.Label(self.Student_Frame, text="Name: ", font=("times new roman", 15, "bold"))
		self.rollNo = tk.Label(self.Student_Frame, text="Roll No: ", font=("times new roman", 15, "bold"))
		self.section = tk.Label(self.Student_Frame, text="Section: ", font=("times new roman", 15, "bold"))
		self.gender = tk.Label(self.Student_Frame, text="Gender: ", font=("times new roman", 15, "bold"))
		self.dob = tk.Label(self.Student_Frame, text="D.O.B: ", font=("times new roman", 15, "bold"))
		self.email = tk.Label(self.Student_Frame, text="E-mail: ", font=("times new roman", 15, "bold"))
		self.phone = tk.Label(self.Student_Frame, text="Phone No: ", font=("times new roman", 15, "bold"))
		self.mentor = tk.Label(self.Student_Frame, text="Mentor: ", font=("times new roman", 15, "bold"))
		self.address = tk.Label(self.Student_Frame, text="Address: ", font=("times new roman", 15, "bold"))
        

		self.name.grid(row=0, column=0, sticky="w", padx=10, pady=25)
		self.rollNo.grid(row=0, column=2, sticky="w", padx=10, pady=25)
		self.section.grid(row=1, column=0, sticky="w", padx=10, pady=25)
		self.gender.grid(row=1, column=2, sticky="w", padx=10, pady=25)
		self.dob.grid(row=2, column=0, sticky="w", padx=10, pady=25)
		self.email.grid(row=2, column=2, sticky="w", padx=10, pady=25)
		self.phone.grid(row=3, column=0, sticky="w", padx=10, pady=25)
		self.mentor.grid(row=3, column=2, sticky="w", padx=10, pady=25)
		self.address.grid(row=4, column=0, sticky="w", padx=10, pady=25)
        
        #Entry for Student Detail
		self.nameEntry = tk.Entry(self.Student_Frame, textvariable=self.nameVar, font=("times new roman", 13))
		self.rollNoEntry = tk.Entry(self.Student_Frame, textvariable=self.rollNoVar, font=("times new roman", 13))
		self.sectionEntry = ttk.Combobox(self.Student_Frame, textvariable=self.sectionVar, font=("times new roman", 13), state="readonly", width=18)
		self.sectionEntry['values'] = ("A", "B", "C/E", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "B1", "B2", "B3", "B4", "B5", "B6", "B7")
		self.genderEntry = ttk.Combobox(self.Student_Frame, textvariable=self.genderVar, font=("times new roman", 13), state="readonly", width=18)
		self.genderEntry['values'] = ("Male", "Female", "Others")
		self.dobEntry = tk.Entry(self.Student_Frame, textvariable=self.dobVar, font=("times new roman", 13))
		self.emailEntry = tk.Entry(self.Student_Frame, textvariable=self.emailVar, font=("times new roman", 13))
		self.phoneEntry = tk.Entry(self.Student_Frame, textvariable=self.phoneVar, font=("times new roman", 13))
		self.mentorEntry = tk.Entry(self.Student_Frame, textvariable=self.mentorVar, font=("times new roman", 13))
		self.addressEntry = tk.Text(self.Student_Frame, font=("times new roman", 15), height=8, width=48)
        
        
		self.nameEntry.grid(row=0, column=1, sticky="w")
		self.rollNoEntry.grid(row=0, column=3, sticky="w")
		self.sectionEntry.grid(row=1, column=1, sticky="w")
		self.genderEntry.grid(row=1, column=3, sticky="w")
		self.dobEntry.grid(row=2, column=1, sticky="w")
		self.emailEntry.grid(row=2, column=3, sticky="w")
		self.phoneEntry.grid(row=3, column=1, sticky="w")
		self.mentorEntry.grid(row=3, column=3, sticky="w")
		self.addressEntry.place(x=95, y=317)

#===============================Button for Add, Update, Delete, Clear==========================================================
		self.addButton = tk.Button(self.Student_Frame, text="Add", font=("bold"), command=self.addData)
		self.updateButton = tk.Button(self.Student_Frame, text="Update", font=("bold"), command=self.updateData)
		self.deleteButton = tk.Button(self.Student_Frame, text="Delete", font=("bold"), command=self.deleteData)
		self.clearButton = tk.Button(self.Student_Frame, text="Clear", font=("bold"), command=self.clearCommand)

		self.addButton.place(x=40, y=500, width=100, height=50)
		self.updateButton.place(x=160, y=500, width=100, height=50)
		self.deleteButton.place(x=280, y=500, width=100, height=50)
		self.clearButton.place(x=400, y=500, width=100, height=50)
        



#=====================Frame for Searching=======================================================================
		self.Search_Frame = tk.LabelFrame(self.root, text="Student Information", font=("times new roman", 13, "italic"))
		self.Search_Frame.place(x=600, y=80, width=827, height=750)

		self.sort = tk.Label(self.Search_Frame, text="Search By:", font=("Comic Sans MS", 18, "bold"))
		self.sort.grid(row=0, column=0, sticky="e", padx= 30)

		self.sortEntry = ttk.Combobox(self.Search_Frame, state="readonly")
		self.sortEntry['values'] = ("Roll No", "Phone No", "Section", "Mentor")
		self.sortEntry.grid(row=0, column=1, sticky="w")

		self.sortData = tk.Entry(self.Search_Frame, width=30, font=("times new roman", 13))
		self.sortData.grid(row=0, column=2, sticky="w", padx=30)

		self.sortButton = tk.Button(self.Search_Frame, width=10, text="Search", font=("bold"))
		self.sortButton.grid(row=0, column=3, sticky="w", padx=5)

#=====================Frame for Detail==============================================================================
		self.Detail_Frame = tk.Frame(self.Search_Frame, bd=4, relief="groove")
		self.Detail_Frame.place(x=10, y=40, width=805, height=680)

        #ScrollBar
		self.xscroll = tk.Scrollbar(self.Detail_Frame, orient="horizontal")
		self.yscroll = tk.Scrollbar(self.Detail_Frame, orient="vertical")
        
		self.detailTable = ttk.Treeview(self.Detail_Frame, columns=("Roll No", "Name", "Course", "Department", "Year", "Semester", "Section", "Gender", "D.O.B", "E-mail", "Phone No", "Mentor", "Address"), xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)

		self.xscroll.pack(side="bottom", fill="x")
		self.xscroll.config(command=self.detailTable.xview)
		self.yscroll.pack(side="right", fill="y")
		self.yscroll.config(command=self.detailTable.yview)
        
        #Table Heading
		self.detailTable.heading("Roll No", text="Roll No")
		self.detailTable.heading("Name", text="Name")
		self.detailTable.heading("Course", text="Course")
		self.detailTable.heading("Department", text="Department")
		self.detailTable.heading("Year", text="Year")
		self.detailTable.heading("Semester", text="Semester")
		self.detailTable.heading("Section", text="Section")
		self.detailTable.heading("Gender", text="Gender")
		self.detailTable.heading("D.O.B", text="D.O.B")
		self.detailTable.heading("E-mail", text="E-mail")
		self.detailTable.heading("Phone No", text="Phone No")
		self.detailTable.heading("Mentor", text="Mentor")
		self.detailTable.heading("Address", text="Address")
		self.detailTable['show'] = 'headings'
		self.detailTable.column("Roll No", width=150)
		self.detailTable.column("Name", width=200)
		self.detailTable.column("Course", width=100)
		self.detailTable.column("Department", width=100)
		self.detailTable.column("Year", width=100)
		self.detailTable.column("Semester", width=100)
		self.detailTable.column("Section", width=100)
		self.detailTable.column("Gender", width=100)
		self.detailTable.column("D.O.B", width=100)
		self.detailTable.column("E-mail", width=200)
		self.detailTable.column("Phone No", width=150)
		self.detailTable.column("Mentor", width=100)
		self.detailTable.column("Address", width=500)
		self.detailTable.bind("<ButtonRelease-1>", self.get_data)
		self.show_detailTable()
		self.detailTable.pack(fill="both", expand=1)	
		
		self.root.mainloop()

#=====================Command to Add Data================================  
	def addData(self):
		present = 0
		totalClasses = 0
		percentage = 0
		name = self.nameVar.get()
		rollNo = self.rollNoVar.get()
		section = self.sectionVar.get()
		gender = self.genderVar.get()
		dob = self.dobVar.get()
		email = self.emailVar.get()
		phoneNo = self.phoneVar.get()
		mentor = self.mentorVar.get()
		course = self.courseVar.get()
		department = self.departmentVar.get()
		year = self.yearVar.get()
		semester = self.semesterVar.get()
		address = self.addressEntry.get('1.0', "end")
		#print(name+"qw")
		if(name=="" or rollNo=="" or section =="" or gender=="" or dob=="" or email=="" or phoneNo=="" or mentor=="" or course =="" or department=="" or year=="" or semester=="" or address==""):
			messagebox.showinfo("Error !!", "Please Enter All Fields")
		else:
			try:
				conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
				cur = conn.cursor()
				cur.execute("Insert into Student_Data (Roll_no, Name, Course, Department, Year, Semester, Section, Gender, DOB, Email, Phone, Mentor, Address, Present, Total_CLasses, Attendence_Percentage) Values ('"+str(rollNo)+"', '"+str(name)+"', '"+str(course)+"', '"+str(department)+"', '"+str(year)+"', '"+str(semester)+"', '"+str(section)+"', '"+str(gender)+"', '"+str(dob)+"', '"+str(email)+"', '"+str(phoneNo)+"', '"+str(mentor)+"', '"+str(address)+"', '"+str(present)+"', '"+str(totalClasses)+"', '"+str(percentage)+"')")
				conn.commit()
				self.show_detailTable()
				conn.close()
			except Exception as error:
				print(error)
				messagebox.showinfo("Error!!", "Student Details already Present")

#======================command to clear all parameters=====================================================
	def clearCommand(self):
		self.nameEntry.delete(0, "end")
		self.rollNoEntry.delete(0, "end")
		self.sectionEntry.set("")
		self.genderEntry.set("")
		self.dobEntry.delete(0, "end")
		self.emailEntry.delete(0, "end")
		self.phoneEntry.delete(0, "end")
		self.mentorEntry.delete(0, "end")
		self.addressEntry.delete("1.0", "end")

	def resetCommand(self):
		self.courseEntry.set("")
		self.departmentEntry.set("")
		self.yearEntry.set("")
		self.semesterEntry.set("")

#====================dunction to show data in the detailTable===========================
	def show_detailTable(self):
		try:
			conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
			cur = conn.cursor()
			cur.execute("select * from Student_Data")
			data = cur.fetchall()
			if len(data) != 0:
				self.detailTable.delete(*self.detailTable.get_children())
				for row in data:
					self.detailTable.insert('', "end", values=row)
			conn.commit()
			conn.close()

		except Exception as error:
			print(error)
                  
#============funnction to show data in the respective entry boxes========================
	def get_data(self, event):
		self.clearCommand()
		self.resetCommand()
		cursor = self.detailTable.focus()
		data = self.detailTable.item(cursor)
		row = data['values']
		#print(row)
		self.nameEntry.insert(0, row[1])
		self.rollNoEntry.insert(0, row[0])
		self.sectionEntry.set(row[6])
		self.genderEntry.set(row[7])
		self.dobEntry.insert(0, row[8])
		self.emailEntry.insert(0, row[9])
		self.phoneEntry.insert(0, row[10])
		self.mentorEntry.insert(0, row[11])
		self.addressEntry.insert("end", row[12])
		self.courseEntry.set(row[2])
		self.departmentEntry.set(row[3])
		self.yearEntry.set(row[4])
		self.semesterEntry.set(row[5])
	
#=============function to delete data==========================
	def deleteData(self):
		rollNo = self.rollNoEntry.get()
		if(rollNo==""):
			messagebox.showinfo("Error!!", "Please Enter a Valid Roll Number")
		else:
			try:
				conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
				cur = conn.cursor()
				cur.execute("delete from Student_Data where Roll_No="+rollNo)
				conn.commit()
				self.show_detailTable()
				self.clearCommand()
				self.resetCommand()
				conn.close()
	
			except Exception as error:
				print(error)

#===============Funtion to update data=======================
	def updateData(self):
		name = self.nameVar.get()
		rollNo = self.rollNoVar.get()
		section = self.sectionVar.get()
		gender = self.genderVar.get()
		dob = self.dobVar.get()
		email = self.emailVar.get()
		phoneNo = self.phoneVar.get()
		mentor = self.mentorVar.get()
		course = self.courseVar.get()
		department = self.departmentVar.get()
		year = self.yearVar.get()
		semester = self.semesterVar.get()
		address = self.addressEntry.get('1.0', "end")
		if(rollNo==""):
			messagebox.showinfo("Error!!", "Please Enter a Valid Roll Number")
		else:
			try:
				conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
				cur = conn.cursor()
				cur.execute("update Student_Data set Name='"+name+"', Course='"+course+"', Department='"+department+"', Year='"+year+"', Semester='"+semester+"', Section='"+section+"', Gender='"+gender+"', DOB='"+dob+"', Email='"+email+"', Phone='"+phoneNo+"', Mentor='"+mentor+"', Address='"+address+"' where Roll_No="+rollNo)
				conn.commit()
				self.show_detailTable()
				self.clearCommand()
				self.resetCommand()
				conn.close()
			except Exception as error:
				print(error)

#==============Check student attendence======================
class Check_Attendence:
    def __init__(self):   
        self.root = tk.Toplevel()
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

#================shows attendence===============================
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

#=================Admin access to student data=======================
class Admin_Login_Student:
    def __init__(self):
        self.root = tk.Toplevel()
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

#============checks and login the admin=================
    def adminLogin(self):
        username = self.usernameEntry.get()
        passwd = self.passwordEntry.get()
        if username in usernameList:
            #print("present")
            conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
            cur = conn.cursor()
            cur.execute("select * from admin_data")
            admindata = cur.fetchall()
            conn.commit()
            conn.close()
            for i in admindata:
                if(i[0] == username):
                    realPasswd = i[1]
                    break
            if(realPasswd == passwd):
                #print("correct")
                self.root.destroy()
                Manage_Student()
                
            else:
                messagebox.showinfo("Error!!", "Invalid  Password")
        else:
            messagebox.showinfo("Error!!", "Please enter correct username and password")

#===============Admin access to teacher data=======================
class Admin_Login_Teacher:
    def __init__(self):
        self.root = tk.Toplevel()
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

#==================checking admin username and passwprd=================
    def adminLogin(self):
        username = self.usernameEntry.get()
        passwd = self.passwordEntry.get()
        if username in usernameList:
            #print("present")
            conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
            cur = conn.cursor()
            cur.execute("select * from admin_data")
            admindata = cur.fetchall()
            conn.commit()
            conn.close()
            for i in admindata:
                if(i[0] == username):
                    realPasswd = i[1]
                    break
            if(realPasswd == passwd):
                #print("correct")
                self.root.destroy()
                Manage_Teacher()
                
            else:
                messagebox.showinfo("Error!!", "Invalid  Password")
        else:
            messagebox.showinfo("Error!!", "Please enter correct username and password")

#============Manage teacher data==================================
class Manage_Teacher:
	def __init__(self):
		self.root = tk.Toplevel()
		self.root.geometry("1000x450+0+0")
		self.root.title("Manage Teacher Data")

		self.title = tk.Label(self.root, text="Manage Teacher Data", bd = 10, font=("Comic Sans MS", 30, "bold"), bg="white", fg="black")
		self.title.pack(side = "top", fill="x")

#============Variables for Teacher data===================
		self.teacherIdVar = tk.StringVar()
		self.nameVar = tk.StringVar()
		self.passVar = tk.StringVar()
		self.repassVar = tk.StringVar()

#============Frame for Teacher Detail=======================
		self.teacherDetail_Frame = tk.LabelFrame(self.root, text="Teacher Details", font=("times new roman", 13, "italic"))
		self.teacherDetail_Frame.place(x=12, y=80, width=395, height=350)

		#Lable for teacher detail
		self.teacherId = tk.Label(self.teacherDetail_Frame, text="Id: ", font=("times new roman", 18, "bold"))
		self.teacherName = tk.Label(self.teacherDetail_Frame, text="Name: ", font=("times new roman", 18, "bold"))

		self.teacherId.place(x=40, y=60)
		self.teacherName.place(x=40, y=120)

		#Entry for teacher detail
		self.teacherIdEntry = tk.Entry(self.teacherDetail_Frame, textvariable=self.teacherIdVar, font=("times new roman", 15))
		self.teacherNameEntry = tk.Entry(self.teacherDetail_Frame, textvariable=self.nameVar, font=("times new roman", 15))

		self.teacherIdEntry.place(x=100, y=60, width=250)
		self.teacherNameEntry.place(x=100, y=120, width=250)

		#Button for add, delete and clear
		self.addButton = tk.Button(self.teacherDetail_Frame, text="Add", font=("bold"), width=7, height=3, command=self.chechkpasswd)
		self.deleteButton = tk.Button(self.teacherDetail_Frame, text="Delete", font=("bold"), width=7, height=3, command=self.deleteTeacher)
		self.clearButton = tk.Button(self.teacherDetail_Frame, text="Clear", font=("bold"), width=7, height=3, command=self.clearCommand)

		self.addButton.place(x=20, y=250)
		self.deleteButton.place(x=145, y=250)
		self.clearButton.place(x=270, y=250)

#================Frame to teachers data============================
		self.teacherInfo = tk.LabelFrame(self.root, text="Teacher Information", font=("times new roman", 13, "italic"))
		self.teacherInfo.place(x=420, y=80, height=350, width=568)

		#search options
		self.searchLable = tk.Label(self.teacherInfo, text="Id: ", font=("times new roman", 15, "bold"))
		self.searchEntry = tk.Entry(self.teacherInfo, width=25, font=("times new roman", 15, "bold"))
		self.searchButton = tk.Button(self.teacherInfo, text="Search", font=("bold"), width=10, height=1)
		self.resetButton = tk.Button(self.teacherInfo, text="Reset", font=("bold"), width=8, height=1)

		self.searchLable.grid(row=0, column=0, padx=30, sticky="e")
		self.searchEntry.grid(row=0, column=1)
		self.searchButton.grid(row=0, column=2, padx=10)
		self.resetButton.grid(row=0, column=3)

#===============Frame for information================================
		self.infoFrame = tk.Frame(self.teacherInfo, bd=2, relief="groove")
		self.infoFrame.place(x=7, y=40, height=285, width=550)

		#ScrollBar
		self.xscroll = tk.Scrollbar(self.infoFrame, orient="horizontal")
		self.yscroll = tk.Scrollbar(self.infoFrame, orient="vertical")

		self.infoTable = ttk.Treeview(self.infoFrame, columns=(1,2,3), xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)
		self.xscroll.pack(side="bottom", fill="x")
		self.xscroll.config(command=self.infoTable.xview)
		self.yscroll.pack(side="right", fill="y")
		self.yscroll.config(command=self.infoTable.yview)

		#TableHeading
		self.infoTable.heading(1, text="Teacher Id")
		self.infoTable.heading(2, text="Name")
		self.infoTable.heading(3, text="Password")
		self.infoTable['show'] = 'headings'
		#self.infoTable.column(1, width=150)
		#self.infoTable.column(2, width=150)
		#self.infoTable.column(3, width=150)
		self.infoTable.bind("<ButtonRelease-1>", self.get_data)
		self.show_TeacherInfoTable()
		self.infoTable.pack(fill="both", expand=1)


		self.root.mainloop()

#================funtion to add teacher data===================
	def chechkpasswd(self):
		self.Tid = self.teacherIdEntry.get()
		self.Tname = self.teacherNameEntry.get()
		if(self.Tid=="" or self.Tname==""):
			messagebox.showinfo("Error!!", "Please enter all fields.")
		else:
			passwdWin = tk.Toplevel()
			passwdWin.geometry("500x225+0+0")
			passwdWin.title("Enter Password")

			enterPasswd = tk.Label(passwdWin, text="Enter Password: ", font=("times new roman", 13, "bold"))
			self.enterPasswdEntry = tk.Entry(passwdWin, width=30, show="*", textvariable=self.passVar)
			reenterPasswd = tk.Label(passwdWin, text="Re-Enter Password: ", font=("times new roman", 13, "bold"))
			self.reenterPasswdEntry = tk.Entry(passwdWin, width=30, show="*", textvariable=self.repassVar)
			doneButton = tk.Button(passwdWin, text="Submit", height=3, width=10, command=lambda: self.addData(passwdWin))

			enterPasswd.grid(row=0, column= 0, pady=30, padx=30)
			reenterPasswd.grid(row=1, column=0)
			self.enterPasswdEntry.grid(row=0, column=1)
			self.reenterPasswdEntry.grid(row=1, column=1)
			doneButton.grid(row=2, columnspan=2, pady=20)
			passwdWin.mainloop()
			
#===============checks the password and add the data into teacher data==================
	def addData(self, master):
		passwd = self.enterPasswdEntry.get()
		repasswd = self.reenterPasswdEntry.get()
		self.enterPasswdEntry.delete(0, "end")
		self.reenterPasswdEntry.delete(0, "end")
		if(passwd=="" or repasswd==""):
			messagebox.showinfo("Error!!", "Please enter all fields.")
		elif(passwd != repasswd):
			messagebox.showinfo("Error!!", "Password does not match")
		else:
			try:
				conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
				cur = conn.cursor()
				cur.execute("Insert into Teacher_Data(Teacher_Id, Name, Passwd) values('"+self.Tid+"', '"+self.Tname+"', '"+passwd+"')")
				conn.commit()
				self.show_TeacherInfoTable()
				self.clearCommand()
				conn.close()
			except:
				messagebox.showinfo("Error!!", "Teacher detail already present.")
            
			master.destroy()
                  


#====================Funtion to see teacher table in teacher info================================	
	def show_TeacherInfoTable(self):
		try:
			conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
			cur = conn.cursor()
			cur.execute("select * from Teacher_Data")
			data = cur.fetchall()
			if len(data) != 0:
				self.infoTable.delete(*self.infoTable.get_children())
				for row in data:
					self.infoTable.insert('', "end", values=row)
			conn.commit()
			conn.close()
		except Exception as error:
			print(error)

#=============funtion to clear all fields=======================
	def clearCommand(self):
		self.teacherIdEntry.delete(0, "end")
		self.teacherNameEntry.delete(0, "end")

#============function to show data in entry boxes from table=========
	def get_data(self, event):
		self.clearCommand()
		cursor = self.infoTable.focus()
		data = self.infoTable.item(cursor)
		row = data["values"]
		#print(row)
		self.teacherIdEntry.insert(0, row[0])
		self.teacherNameEntry.insert(0, row[1])
	
#==============function to delete data==================
	def deleteTeacher(self):
		Teacherid = self.teacherIdEntry.get()
		if(Teacherid==""):
			messagebox.showinfo("Error!!", "Please Enter a Valid Teacher Id")
		else:
			try:
				conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
				cur = conn.cursor()
				cur.execute("delete from Teacher_Data where Teacher_Id="+Teacherid)
				conn.commit()
				self.show_TeacherInfoTable()
				self.clearCommand()
				conn.close()
	
			except Exception as error:
				print(error)

#====================Teacher login to mark attendence=======================
class Teacher_Login:
    def __init__(self):
        self.root = tk.Toplevel()
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
        teacherId()
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
                self.root.destroy()
                Class_Select()

            else:
                messagebox.showinfo("Error!!", "Invalid  Password")
        else:
            messagebox.showinfo("Error!!", "Please enter correct Id and password")

#==============option to select student class and mark attendence================
class Class_Select:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("700x400+0+0")
        self.root.title("Select Class")

        self.title = tk.Label(self.root, text="Select Class", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        self.title.pack(side="top", fill="x")

#==============Variables================================
        self.courseVar = tk.StringVar()
        self.departmentVar = tk.StringVar()
        self.sectionVar = tk.StringVar()
        self.semesterVar = tk.StringVar()

        #Image
        self.checked = ImageTk.PhotoImage(Image.open("checked.png"))
        self.unchecked = ImageTk.PhotoImage(Image.open("unchecked.png"))

#======================Frame for Login=================================
        self.option = tk.Frame(self.root, bg="grey", bd=3, relief="raised")
        self.option.place(x=75, y=75, height=300, width=550)

        #Lable for course
        self.course = tk.Label(self.option, text="Course: ", bg="grey", font=("times new roman", 15, "bold"))
        self.department = tk.Label(self.option, text="Department: ", bg="grey", font=("times new roman", 15, "bold"))
        self.section = tk.Label(self.option, text="Section: ", bg="grey", font=("times new roman", 15, "bold"))
        self.semester = tk.Label(self.option, text="Semester: ", bg="grey", font=("times new roman", 15, "bold"))

        self.course.grid(row=0, column=0, sticky="w", padx=10, pady=60)
        self.department.grid(row=0, column=2, sticky="w", padx=10, pady=20)
        self.section.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.semester.grid(row=1, column=2, sticky="w", padx=10, pady=5)

        #Entry for course
        self.courseEntry = ttk.Combobox(self.option, textvariable=self.courseVar, font=("times new roman", 13), state="readonly", width=18)
        self.courseEntry['values'] = ("B.Tech", "B.Sc", "B.E", "MBBS", "B.Pharm", "BCA", "B.Arch")
        self.departmentEntry = ttk.Combobox(self.option, textvariable=self.departmentVar, font=("times new roman", 13), state="readonly", width=18)
        self.departmentEntry['values'] = ("CSE", "ME", "CE", "ECE", "IT", "EE")
        self.sectionEntry = ttk.Combobox(self.option, textvariable=self.sectionVar, font=("times new roman", 13), state="readonly", width=18)
        self.sectionEntry['values'] = ("A", "B", "C/E", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "B1", "B2", "B3", "B4", "B5", "B6", "B7")
        self.semesterEntry = ttk.Combobox(self.option, textvariable=self.semesterVar, font=("times new roman", 13), state="readonly", width=18)
        self.semesterEntry['values'] = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        self.reset = tk.Button(self.option, text="Submit", font=("bold"), height=3, width=10, command=self.submitButton)

        self.courseEntry.grid(row=0, column=1, sticky="w")
        self.departmentEntry.grid(row=0, column=3, sticky="w")
        self.sectionEntry.grid(row=1, column=1, sticky="w")
        self.semesterEntry.grid(row=1, column=3, sticky="w")
        self.reset.grid(row=2, columnspan=4, pady=40)

        self.root.mainloop()
        
#==================funtion for showing list of student===========================
    def submitButton(self):
        course = self.courseEntry.get()
        department = self.departmentEntry.get()
        section = self.sectionEntry.get()
        semester = self.semesterEntry.get()

        if(course=="" or department=="" or section=="" or semester==""):
            messagebox.showinfo("Error!!", "Please fill all fields.")

        else:    
            #self.root.destroy()
            root = tk.Toplevel()
            root.geometry("700x800+0+0")
            root.title("Mark Attendence")

            header = tk.Label(root, text="Mark Attendence", bd = 10, font=("Comic Sans MS", 35, "bold"), bg="white", fg="black")
            header.pack(side="top", fill="x")

            #attendence frame
            attendenceFrame = tk.Frame(root, bg="grey", bd=3, relief="raised")
            attendenceFrame.place(x=10, y=90, height=630, width=680)

            #scroll bar
            xscrollbar = tk.Scrollbar(attendenceFrame, orient="horizontal")
            yscrollbar = tk.Scrollbar(attendenceFrame, orient="vertical")

            headings = ttk.Treeview(attendenceFrame, columns=(1,2,3,4), xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

            xscrollbar.pack(side="bottom", fill="x")
            xscrollbar.config(command=headings.xview)
            yscrollbar.pack(side="right", fill="y")
            yscrollbar.config(command=headings.yview)

            #headings for attendence
            style = ttk.Style(headings)
            style.configure('Treeview', rowheight=30)
            headings.tag_configure('checked', image=self.checked)
            headings.tag_configure('unchecked', image=self.unchecked)
            headings.heading('#0', text="Present")
            headings.heading("#1", text="Roll No")
            headings.heading("#2", text="Name")
            headings.heading("#3", text="Mentor")
            headings.heading("#4", text="Phone No")
            #headings['show'] = 'headings'
            #headings.column(1)
            #headings.column(2)
            #headings.column(3)
            #headings.column(4)

            #checks and unchecks the row
            def toggelCheck(event):
                rowid = headings.identify_row(event.y)
                tag = headings.item(rowid, "tags")[0]
                tags = list(headings.item(rowid, "tags"))
                tags.remove(tag)
                #print(tag)
                headings.item(rowid, tags=tags)
                if(tag == "checked"):
                    headings.item(rowid, tags="unchecked")
                else:
                    headings.item(rowid, tags="checked")

            headings.bind('<Button 1>', toggelCheck)
            headings.pack(fill="both", expand=1)

            #done Button
            doneButton = tk.Button(root, text="Submit", width=10, height=3, command=lambda: self.updateAttendence(headings, root))
            doneButton.pack(side="bottom", pady=10)

            try:
                conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
                cur = conn.cursor()
                cur.execute("select Roll_No, Name, Mentor, Phone from Student_Data where Course ='"+course+"' and Department='"+department+"' and Section='"+section+"' and Semester='"+semester+"'")
                data = cur.fetchall()
                if len(data) != 0:
                    headings.delete(*headings.get_children())
                    for row in data:
                        headings.insert('', "end", values=row, tags="unchecked")
                conn.commit()
                conn.close()
            except Exception as error:
                print(error)

            root.mainloop()


#===============Update attendence details====================
    def updateAttendence(self, heading, master):
        for i in heading.get_children():
            val = heading.item(i, "values")
            val = val[0]
            try:
                conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
                cur = conn.cursor()
                cur.execute("update Student_Data set Total_Classes = Total_Classes+1 where Roll_no="+val)
                cur.execute("update Student_Data set Attendence_Percentage = (Present*100)/Total_Classes where Roll_no="+val)
                conn.commit()
                conn.close()
            except Exception as error:
                print(error)

        for i in heading.get_children():
            tag = heading.item(i, "tags")[0]
            tags = list(heading.item(i, "tags"))
            tags.remove(tag)
            val = heading.item(i, "values")
            val = val[0]
            if tag == "checked":
                try:
                    conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
                    cur = conn.cursor()
                    cur.execute("update Student_Data set Present = Present+1 where Roll_no="+val)
                    cur.execute("update Student_Data set Attendence_Percentage = (Present*100)/Total_Classes where Roll_no="+val)
                    conn.commit()
                    conn.close()
                except Exception as error:
                    print(error)
        master.destroy()


#===============main login that shows the first window=====================
class Main_Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x400+0+0")
        self.root.title("Login")

        self.title = tk.Label(self.root, text="Login", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        self.title.pack(side="top", fill="x")

#=======================Frame for button===================================
        self.buttonFrame = tk.Frame(self.root, bg="grey")
        self.buttonFrame.place(x=2, y=50, height=347, width=696)

#======================Buttons for Options=================================
        self.checkAttendence = tk.Button(self.buttonFrame, text="Check\nAttendence", bd=2, relief="groove", bg="white", fg="black", height=5, width=10, command=lambda: Check_Attendence())
        self.markAttendence = tk.Button(self.buttonFrame, text="Mark\nAttendence", bd=2, relief="groove", bg="white", fg="black", height=5, width=10, command=lambda: Teacher_Login())
        self.updateTeacher = tk.Button(self.buttonFrame, text="Update\nTeacher Details", bd=2, relief="groove", bg="white", fg="black", height=5, width=10, command=lambda: Admin_Login_Teacher())
        self.updateStudent = tk.Button(self.buttonFrame, text="Update\nStudent Details", bd=2, relief="groove", bg="white", fg="black", height=5, width=10, command=lambda: Admin_Login_Student())

        self.checkAttendence.grid(row=0, column=0, padx=145, pady=50)
        self.markAttendence.grid(row=0, column=1)
        self.updateTeacher.grid(row=1, column=0)
        self.updateStudent.grid(row=1, column=1)

    


if __name__ == "__main__":
    root = tk.Tk()
    login = Main_Login(root)
    root.mainloop()