import tkinter as tk
from tkinter import ttk

class Check_Attendence2:
    def __init__(self, root):   
        self.root = root
        self.root.geometry("800x300+0+0")
        self.root.title("Attendence")

        self.title = tk.Label(self.root, text="Check Attendence", bg="white", fg="black", font=("Comic sans MS", 30, "bold"))
        self.title.pack(side="top", fill="x")

#=====================Frame for Attendence information=====================================
        self.attendenceInformation = tk.Frame(self.root, bg="grey")
        self.attendenceInformation.pack(fill="both", expand=1)

#======================Label for Attendence information=====================================
        self.rollNo = tk.Label(self.attendenceInformation, text="Roll No: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        self.name = tk.Label(self.attendenceInformation, text="Name: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        self.totalClasses = tk.Label(self.attendenceInformation, text="Total Classes: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        self.totalAttend = tk.Label(self.attendenceInformation, text="Total Attendence: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))
        self.percentage = tk.Label(self.attendenceInformation, text="Percentage: ", bg="grey", fg="Black", font=("Times new roman", 18, "bold"))


        self.rollNo.grid(row=0, column=0, padx=20, pady=10)   
        self.name.grid(row=0, column=2, padx=20, pady=10)   
        self.totalClasses.grid(row=1, column=0, padx=20, pady=10)   
        self.totalAttend.grid(row=1, column=2, padx=20, pady=10)   
        self.percentage.grid(row=2, column=1, pady=30, sticky="e")   

#========================Entry for Attendence information=====================================
        self.rollNoEntry = tk.Entry(self.attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        self.nameEntry = tk.Entry(self.attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        self.totalClassesEntry = tk.Entry(self.attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        self.totalAttendEntry = tk.Entry(self.attendenceInformation, fg="white", font=("Times new roman", 18, "bold"))
        self.percentageEntry = tk.Entry(self.attendenceInformation, fg="white", font=("Times new roman", 18, "bold"), width=10)

        self.rollNoEntry.grid(row=0, column=1)
        self.nameEntry.grid(row=0, column=3)
        self.totalClassesEntry.grid(row=1, column=1)
        self.totalAttendEntry.grid(row=1, column=3)
        self.percentageEntry.grid(row=2, column=2, sticky="w")

#=======================Done button for Attendence information=====================================
        self.done = tk.Button(self.attendenceInformation, text="DONE", width=10, font=("Times new roman", 18, "bold"), command=self.destroyCheck_Attendence2)
        self.done.grid(row=3, columnspan=4)

    def destroyCheck_Attendence2(self):
        self.rollNoEntry.delete(0, 100)

if __name__ == "__main__":
    main = tk.Tk()
    obj = Check_Attendence2(main)
    main.mainloop()