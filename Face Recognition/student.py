from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("Face Recognition System")
        title_lb2=Label(self.root,text="Student Details",font=("script mt bold",50,"bold"),bg="light green",fg="red")
        title_lb2.place(x=0,y=0,width=1530,height=100)
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_Name=StringVar()
        self.var_semester=StringVar()
        self.var_acad_year=StringVar()
        self.var_ID=StringVar()
        self.var_roll_no=StringVar()
        self.var_regd_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phno=StringVar()
        self.var_address=StringVar()
        self.var_mentor=StringVar()

        # setting the framefor the details window.... 
        main_frame=Frame(self.root,bd=2,bg="yellow")
        main_frame.place(x=15,y=110,width=1500,height=640)
        img_bg=Image.open(r"studentdata.jpg")
        img_bg=img_bg.resize((1530,640),Image.Resampling.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)
        f_lbl=Label(main_frame,image=self.photoimg_bg)
        #placing the image
        f_lbl.place(x=0,y=0,width=1530,height=640)
        # designing label frame 
        #left side
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=50,y=20,width=675,height=550)

        img_bg_left=Image.open(r"data.png")
        img_bg_left=img_bg_left.resize((675,550),Image.Resampling.LANCZOS)
        self.photoimg_bg_left=ImageTk.PhotoImage(img_bg_left)
        f_lb_left=Label(left_frame,image=self.photoimg_bg_left)
        #placing the image
        f_lb_left.place(x=0,y=0,width=675,height=550)
        #designing in left frame layout,entries etc....
        #current course details.....
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current course details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=0,y=10,width=620,height=200)
        img_bg_curr=Image.open(r"studentdata.jpg")
        img_bg_curr=img_bg_curr.resize((600,200),Image.Resampling.LANCZOS)
        self.photoimg_bg_curr=ImageTk.PhotoImage(img_bg_curr)
        f_lbl_curr=Label(current_course_frame,image=self.photoimg_bg_curr)
        #placing the image
        f_lbl_curr.place(x=0,y=0,width=600,height=200)

        # designing labels in current course...
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        #designing the combo box in which the values are filled 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=50,state="readonly")
        #filling the values in the deaprtment.....
        dep_combo["values"]=("Select department","CSE","ECE","MME","MECH","CIVIL","BIOTECH","CHEMISTRY","PHYSICS","MATHEMATICS","MANAGEMENT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

         #Course
        dep_label4=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label4.grid(row=1,column=0)
        #designing the combo box in which the values are filled 
        dep_combo4=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=50,state="readonly")
        #filling the values in the course.....
        dep_combo4["values"]=("Select Course","B.Tech","M.C.A.","M.Tech","M.Sc.","M.B.A.")
        dep_combo4.current(0)
        dep_combo4.grid(row=1 ,column=1,padx=5,pady=5,sticky=W)

        #course year
        dep_label1=Label(current_course_frame,text="Course Year",font=("times new roman",12,"bold"),bg="white")
        dep_label1.grid(row=2,column=0)
        #designing the combo box in which the values are filled 
        dep_combo1=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=50,state="readonly")
        #filling the values in the course year.....
        dep_combo1["values"]=("Select Course Year","First Year","Second Year","Third Year","Fourth Year")
        dep_combo1.current(0)
        dep_combo1.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        # semester 
        dep_label2=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label2.grid(row=3,column=0)
        #designing the combo box in which the values are filled 
        dep_combo2=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=50,state="readonly")
        #filling the values in the semester.....
        dep_combo2["values"]=("Select Semester","ODD Semester","EVEN Semester")
        dep_combo2.current(0)
        dep_combo2.grid(row=3 ,column=1,padx=5,pady=5,sticky=W)

        #Academic Year
        dep_label3=Label(current_course_frame,text="Academic Year",font=("times new roman",12,"bold"),bg="white")
        dep_label3.grid(row=4,column=0)
        #designing the combo box in which the values are filled 
        dep_combo3=ttk.Combobox(current_course_frame,textvariable=self.var_acad_year,font=("times new roman",12,"bold"),width=50,state="readonly")
        #filling the values in the deaprtment.....
        dep_combo3["values"]=("Select Academic Year","2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23","2023-24")
        dep_combo3.current(0)
        dep_combo3.grid(row=4 ,column=1,padx=5,pady=5,sticky=W)




        # making another entry column for other details...
        class_Student_Frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_Student_Frame.place(x=0,y=220,width=620,height=300)

        img_bg_stu=Image.open(r"studentdata.jpg")
        img_bg_stu=img_bg_stu.resize((600,300),Image.Resampling.LANCZOS)
        self.photoimg_bg_stu=ImageTk.PhotoImage(img_bg_stu)
        f_lbl_stu=Label(class_Student_Frame,image=self.photoimg_bg_stu)
        #placing the image
        f_lbl_stu.place(x=0,y=0,width=600,height=300)

        #designing the labels or entry field in student info... 
        stu_label0=Label(class_Student_Frame,text="Student id ",font=("times new roman",12,"bold"),bg="white")
        stu_label0.grid(row=0,column=0,padx=5,pady=5)
        #making entry fiels
        id_entry0=ttk.Entry(class_Student_Frame,textvariable=self.var_ID,width=20,font=("times new roman",12,"bold"))
        id_entry0.grid(row=0,column=1,padx=10,sticky=W )

        stu_label1=Label(class_Student_Frame,text="Roll No. ",font=("times new roman",12,"bold"),bg="white")
        stu_label1.grid(row=1,column=0,padx=5,pady=5)
        id_entry1=ttk.Entry(class_Student_Frame,textvariable=self.var_roll_no,width=20,font=("times new roman",12,"bold"))
        id_entry1.grid(row=1,column=1,padx=10,sticky=W )

        stu_label2=Label(class_Student_Frame,text="Regd No.",font=("times new roman",12,"bold"),bg="white")
        stu_label2.grid(row=2,column=0,padx=5,pady=5)
        id_entry2=ttk.Entry(class_Student_Frame,textvariable=self.var_regd_no,width=20,font=("times new roman",12,"bold"))
        id_entry2.grid(row=2,column=1,padx=10,sticky=W )

        stu_label3=Label(class_Student_Frame,text="E-mail Id ",font=("times new roman",12,"bold"),bg="white")
        stu_label3.grid(row=3,column=0,padx=5,pady=5)
        id_entry3=ttk.Entry(class_Student_Frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        id_entry3.grid(row=3,column=1,padx=10,sticky=W )

        stu_label4=Label(class_Student_Frame,text="Address ",font=("times new roman",12,"bold"),bg="white")
        stu_label4.grid(row=4,column=0,padx=5,pady=5)
        id_entry4=ttk.Entry(class_Student_Frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        id_entry4.grid(row=4,column=1,padx=10,sticky=W )

        stu_label5=Label(class_Student_Frame,text="Student Name ",font=("times new roman",12,"bold"),bg="white")
        stu_label5.grid(row=0,column=2,padx=5,pady=5)
        id_entry5=ttk.Entry(class_Student_Frame,textvariable=self.var_Name,width=20,font=("times new roman",12,"bold"))
        id_entry5.grid(row=0,column=3,padx=10,sticky=W )

        stu_label6=Label(class_Student_Frame,text="Gender ",font=("times new roman",12,"bold"),bg="white")
        stu_label6.grid(row=1,column=2,padx=5,pady=5)
        gender_combo1=ttk.Combobox(class_Student_Frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo1["values"]=("Select Gender","Male","Female","Other")
        gender_combo1.current(0)
        gender_combo1.grid(row=1,column=3,padx=10,sticky=W)


        stu_label7=Label(class_Student_Frame,text="D.O.B. ",font=("times new roman",12,"bold"),bg="white")
        stu_label7.grid(row=2,column=2,padx=5,pady=5)
        id_entry7=ttk.Entry(class_Student_Frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        id_entry7.grid(row=2,column=3,padx=10,sticky=W )


        dep_label8=Label(class_Student_Frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        dep_label8.grid(row=3,column=2,padx=5,pady=5)
        id_entry8=ttk.Entry(class_Student_Frame,textvariable=self.var_phno,width=20,font=("times new roman",12,"bold"))
        id_entry8.grid(row=3,column=3,padx=10,sticky=W )

        dep_label9=Label(class_Student_Frame,text="Mentor ",font=("times new roman",12,"bold"),bg="white")
        dep_label9.grid(row=4,column=2,padx=5,pady=5)
        id_entry9=ttk.Entry(class_Student_Frame,textvariable=self.var_mentor,width=20,font=("times new roman",12,"bold"))
        id_entry9.grid(row=4,column=3,padx=10,sticky=W )


        #radio buttons
        self.var_radio1=StringVar()
        rbtn1=ttk.Radiobutton(class_Student_Frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        rbtn1.grid(row=5,column=0)
       
        rbtn2=ttk.Radiobutton(class_Student_Frame,variable=self.var_radio1,text="No photo sample",value="No")
        rbtn2.grid(row=5,column=1)

        #making new frame for button
        btn_frame=Frame(class_Student_Frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width=600,height=35)

        save_btn=Button(btn_frame, command=self.add_data,text="Save",width=16,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,command=self.Update_data,text="Update",width=15,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        update_btn.grid(row=0,column=1)
        delete_btn=Button(btn_frame,command=self.del_data,text="Delete",width=15,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        delete_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=16,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_Frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=600,height=35)
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=35,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        update_photo_btn.grid(row=0,column=3)

        #right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        right_frame.place(x=775,y=20,width=675,height=550)
        img_bg_right=Image.open(r"data.png")
        img_bg_right=img_bg_right.resize((675,550),Image.Resampling.LANCZOS)
        self.photoimg_bg_right=ImageTk.PhotoImage(img_bg_right)
        f_lb_right=Label(right_frame,image=self.photoimg_bg_right)
        #placing the image
        f_lb_right.place(x=0,y=0,width=675,height=550)

        # searchsystem
        search_Frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_Frame.place(x=10,y=20,width=600,height=60)

        search_label=Label(search_Frame,text="Search By:- ",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0)

        search_combo=ttk.Combobox(search_Frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        #filling the values in the deaprtment.....
        search_combo["values"]=("Select ","Roll no.","Phone no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_btn=Button(search_Frame,text="Search",width=10,font=("times new roman",13,"italic"),bg="skyblue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        show_all_btn=Button(search_Frame,text="Show All",width=10,font=("times new roman",13,"italic"),bg="skyblue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)

        search_entry=ttk.Entry(search_Frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W )
        

        #creating databse table...
        table_Frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_Frame.place(x=10,y=85,width=600,height=440)

        #makig scroll bar
        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_Frame,columns=("Name","dept","course","year","semester","acad_year","ID","roll no","regd no","gender","dob","email","phoneno","address","mentor","sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Course year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("acad_year",text="A/Y")
        self.student_table.heading("ID",text="Stu. ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("roll no",text="Roll No.")
        self.student_table.heading("regd no",text="Regd No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="D.O.B.")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("phoneno",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("mentor",text="Mentor")
        self.student_table.heading("sample",text="Photo Sample")
        self.student_table["show"]="headings"
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("acad_year",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("regd no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("mentor",width=100)
        self.student_table.column("sample",width=100)
       
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dept.get()=="Select department"or self.var_Name.get()==""or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pby96@2000",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                            self.var_Name.get(),
                                                                                                                            self.var_dept.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_semester.get(),
                                                                                                                            self.var_acad_year.get(),
                                                                                                                            self.var_ID.get(),
                                                                                                                            self.var_roll_no.get(),
                                                                                                                            self.var_regd_no.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_phno.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_mentor.get(),
                                                                                                                            self.var_radio1.get()
                                                                                            
                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pby96@2000",database="face_recognition")
        my_cursor=conn.cursor()    
        my_cursor.execute("select * from student_data")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Name.set(data[0])
        self.var_dept.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_acad_year.set(data[5])
        self.var_ID.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_regd_no.set(data[8])
        self.var_gender.set(data[9])
        self.var_dob.set(data[10])
        self.var_email.set(data[11])
        self.var_phno.set(data[12])
        self.var_address.set(data[13])
        self.var_mentor.set(data[14])
        self.var_radio1.set(data[15])

    def Update_data(self):
         if self.var_dept.get()=="Select department"or self.var_Name.get()==""or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
         else:
            try:
                Update=messagebox.askyesno("Update","Do you want to upgrade this student detail ",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Pby96@2000",database="face_recognition")
                     my_cursor=conn.cursor() 
                     my_cursor.execute("update student_data Set Name=%s,dept=%s,course=%s,year=%s,semester=%s,acad_year=%s,roll_no=%s,regd_no=%s,gender=%s,dob=%s,email=%s,phno=%s,address=%s,mentor=%s,sample=%s where ID=%s",(
                         
                                                                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                                                                self.var_dept.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_acad_year.get(),
                                                                                                                                                                                                                self.var_roll_no.get(),
                                                                                                                                                                                                                self.var_regd_no.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phno.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_mentor.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_ID.get()
                                                                                            
                                                                                                                                                                                                             ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def del_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID is required to delete the data",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Data","Do you want to delete the data of this student",parent=self.root)
                if delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Pby96@2000",database="face_recognition")
                     my_cursor=conn.cursor()
                     sql="delete from student_data where ID=%s"
                     val=(self.var_ID.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Data Deleted",f"The data of {str(val)} is deletedd successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_Name.set(""),
        self.var_dept.set("Select department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Course Year"),
        self.var_semester.set("Select Semester"),
        self.var_acad_year.set("Select Academic Year"),
        self.var_ID.set("")
        self.var_roll_no.set(""),
        self.var_regd_no.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phno.set(""),
        self.var_address.set(""),
        self.var_mentor.set(""),
        self.var_radio1.set(""),
        
    #generate dataset and take photo sample
    def generate_dataset(self):
         if self.var_dept.get()=="Select department"or self.var_Name.get()==""or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
         else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pby96@2000",database="face_recognition")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student_data")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student_data set Name=%s,dept=%s,course=%s,year=%s,semester=%s,acad_year=%s,roll_no=%s,regd_no=%s,gender=%s,dob=%s,email=%s,phno=%s,address=%s,mentor=%s,sample=%s where ID=%s",(
                         
                                                                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                                                                self.var_dept.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_acad_year.get(),
                                                                                                                                                                                                                self.var_roll_no.get(),
                                                                                                                                                                                                                self.var_regd_no.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phno.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_mentor.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_ID.get()==id+1
                                                                                            
                                                                                                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #loading predefined data on face frontal from open cv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor,minimum neighbour are two values passed above

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame=cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame),(300,300))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==20:
                         break
                cap.release()   
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset completed successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                

# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
