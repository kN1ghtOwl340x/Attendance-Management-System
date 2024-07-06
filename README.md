# Attendance-Management-System
Main_Login.py contains the main program

the folders are the intial option and contains the individual program if you want just some specific password_entry

*How the code works*
1. The code initially creates a database name "AMS"
2. In this databse table are created(Student_Data, Teacher_Data and admin_data)
3. All the tables are empty except admin_data
4. By default an admin user "admin" and password "123" are added to admin_data on the first run of the program
5. admin_data is used to store admin data which is used to add and update teacher and students
6. admin_data is managed directly from mysql



login -> Check_attecdence -> Student_login -> Check

login -> Updata_student_data -> admin_login_student -> student_data(add, update, delete)

login -> Update_teacher_data -> admin_login_teacher -> teacher_data(add -> password_entry, delete)

login -> Mark_Attendence -> teacher_login -> class_select -> give_attendence