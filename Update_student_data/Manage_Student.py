import tkinter as tk # type: ignore
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon
pw=""

#=============Creating a Database=======================
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
	cur.execute("Create Table Student_Data(Roll_no Varchar(100) PRIMARY KEY, Name Varchar(100), Course Varchar(20), Department Varchar(20), Year Varchar(10), Semester Varchar(10), Section Varchar(100), Gender Varchar(20), DOB Varchar(20), Email Varchar(50), Phone varchar(25), Mentor Varchar(30), Address Varchar (1000), Present int, Total_CLasses int, Attendence_Percentage int)")
	conn.commit()
	conn.close()
except Exception as error:
	pass



class Manage_Student:
	def __init__(self):
		self.root = tk.Tk()
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
		self.sectionEntry = tk.Entry(self.Student_Frame, textvariable=self.sectionVar, font=("times new roman", 13))
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
		print(name+"qw")
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
		self.sectionEntry.delete(0, "end")
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
		self.nameEntry.insert(0, row[1])
		self.rollNoEntry.insert(0, row[0])
		self.sectionEntry.insert(0, row[6])
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



m = Manage_Student()