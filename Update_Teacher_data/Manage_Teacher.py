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

#================Creating a table for Teacher data=====================
try:
	conn = mycon.connect(host="localhost", user="root", password=pw, database="AMS")
	cur = conn.cursor()
	cur.execute("create table Teacher_Data(Teacher_Id varchar(100) PRIMARY KEY, Name Varchar(100), Passwd Varchar(100))")
	conn.commit()
	conn.close()

except Exception as error:
	pass

class Manage_Teacher:
	def __init__(self):
		self.root = tk.Tk()
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
			master.destroy()
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


Manage_Teacher()