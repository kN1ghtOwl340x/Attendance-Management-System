import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mycon
from PIL import ImageTk, Image

pw = ""

#==============option to select student class and mark attendence================
class Class_Select:
    def __init__(self):
        self.root = tk.Tk()
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





        




Class_Select()
