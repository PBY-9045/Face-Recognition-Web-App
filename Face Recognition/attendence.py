from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("Face Recognition System")
        title_lb2=Label(self.root,text="Student Attendence Details",font=("script mt bold",50,"bold"),bg="light green",fg="red")
        title_lb2.place(x=0,y=0,width=1530,height=100)
        self.var_att_id=StringVar()
        self.var_att_roll=StringVar()
        self.var_att_name=StringVar()
        self.var_att_dept=StringVar()
        self.var_att_time=StringVar()
        self.var_att_date=StringVar()
        self.var_att_attendnce=StringVar()

        main_frame_attenc=Frame(self.root,bd=2,bg="yellow")
        main_frame_attenc.place(x=15,y=110,width=1500,height=640)
        img_bg_attendence=Image.open(r"studentdata.jpg")
        img_bg_attendence=img_bg_attendence.resize((1530,640),Image.Resampling.LANCZOS)
        self.photoimg_bg_attendence=ImageTk.PhotoImage(img_bg_attendence)
        f_lbl_attendence=Label(main_frame_attenc,image=self.photoimg_bg_attendence)
        #placing the image
        f_lbl_attendence.place(x=0,y=0,width=1530,height=640)
        left_frame_attendence=LabelFrame(main_frame_attenc,bd=2,relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        left_frame_attendence.place(x=50,y=20,width=675,height=550)

        img_bg_left_attendence=Image.open(r"data.png")
        img_bg_left_attendence=img_bg_left_attendence.resize((675,550),Image.Resampling.LANCZOS)
        self.photoimg_bg_left_attendence=ImageTk.PhotoImage(img_bg_left_attendence)
        f_lb_left_attendence=Label(left_frame_attendence,image=self.photoimg_bg_left_attendence)
        #placing the image
        f_lb_left_attendence.place(x=0,y=0,width=675,height=550)
        
        # relif is used for border styling 
        frame_attenc1=Frame(left_frame_attendence,bd=2,relief=RIDGE,bg="yellow")
        frame_attenc1.place(x=10,y=50,width=650,height=500)

        Attendence_label0=Label(frame_attenc1,text="Attendence id ",font=("times new roman",12,"bold"),bg="white")
        Attendence_label0.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        #making entry fiels
        Attendence_entry0=ttk.Entry(frame_attenc1,textvariable=self.var_att_id,width=30,font=("times new roman",12,"bold"))
        Attendence_entry0.grid(row=1,column=0,padx=10,sticky=W )

        Attendence_label1=Label(frame_attenc1,text="Roll no. ",font=("times new roman",12,"bold"),bg="white")
        Attendence_label1.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        #making entry fiels
        Attendence_entry1=ttk.Entry(frame_attenc1,textvariable=self.var_att_roll,width=30,font=("times new roman",12,"bold"))
        Attendence_entry1.grid(row=3,column=0,padx=10,sticky=W )

        Attendence_label2=Label(frame_attenc1,text="Name",font=("times new roman",12,"bold"),bg="white")
        Attendence_label2.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        #making entry fiels
        Attendence_entry2=ttk.Entry(frame_attenc1,textvariable=self.var_att_name,width=30,font=("times new roman",12,"bold"))
        Attendence_entry2.grid(row=5,column=0,padx=10,sticky=W )

        Attendence_label3=Label(frame_attenc1,text="Department",font=("times new roman",12,"bold"),bg="white")
        Attendence_label3.grid(row=6,column=0,padx=5,pady=5,sticky=W)
        #making entry fiels
        Attendence_entry3=ttk.Entry(frame_attenc1,textvariable=self.var_att_dept,width=30,font=("times new roman",12,"bold"))
        Attendence_entry3.grid(row=7,column=0,padx=10,sticky=W )

        Attendence_label4=Label(frame_attenc1,text="Time",font=("times new roman",12,"bold"),bg="white")
        Attendence_label4.grid(row=8,column=0,padx=5,pady=5,sticky=W)
        #making entry fiels
        Attendence_entry4=ttk.Entry(frame_attenc1,textvariable=self.var_att_time,width=30,font=("times new roman",12,"bold"))
        Attendence_entry4.grid(row=9,column=0,padx=10,sticky=W )

        Attendence_label5=Label(frame_attenc1,text="Date",font=("times new roman",12,"bold"),bg="white")
        Attendence_label5.grid(row=10,column=0,padx=5,pady=5,sticky=W)
        #making entry fiels
        Attendence_entry5=ttk.Entry(frame_attenc1,textvariable=self.var_att_date,width=30,font=("times new roman",12,"bold"))
        Attendence_entry5.grid(row=11,column=0,padx=10,sticky=W )

        Attendence_label6=Label(frame_attenc1,text="Attendence ",font=("times new roman",12,"bold"),bg="white")
        Attendence_label6.grid(row=12,column=0,padx=5,pady=5,sticky=W)
        gender_combo1=ttk.Combobox(frame_attenc1,textvariable=self.var_att_attendnce,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo1["values"]=("Status","Present","Absent")
        gender_combo1.current(0)
        gender_combo1.grid(row=13,column=0,padx=10,sticky=W)

        #making new frame for button
        btn_frame=Frame(frame_attenc1,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=280,y=290,width=157,height=125)

        import_btn=Button(btn_frame,text="Import csv",command=self.import_csv,width=16,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        import_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame,command=self.export_csv,text="Export csv",width=16,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        export_btn.grid(row=1,column=0,pady=10)
        #update_att_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        #update_att_btn.grid(row=2,column=0,pady=5)
        reset_att_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=16,font=("times new roman",13,"italic"),bg="skyblue",fg="black")
        reset_att_btn.grid(row=2,column=0,pady=5)

         #right frame
        right_frame_attendence=LabelFrame(main_frame_attenc,bd=2,relief=RIDGE,text="Attendence Data",font=("times new roman",12,"bold"))
        right_frame_attendence.place(x=775,y=20,width=675,height=550)
        img_bg_right_attendence=Image.open(r"data.png")
        img_bg_right_attendence=img_bg_right_attendence.resize((675,550),Image.Resampling.LANCZOS)
        self.photoimg_bg_right_attendence=ImageTk.PhotoImage(img_bg_right_attendence)
        f_lb_right_attendence=Label(right_frame_attendence,image=self.photoimg_bg_right_attendence)
        #placing the image
        f_lb_right_attendence.place(x=0,y=0,width=675,height=550)

        Table_frame=Frame(right_frame_attendence,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=10,y=5,width=650,height=520)

        #scroll bar and table
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(Table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll No")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #fetch data
    def get_data(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    # function for import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.get_data(mydata)

    # function for import csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO data","NO data found in file",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data is exported successfully to :"+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_att_id.set(rows[0])
        self.var_att_roll.set(rows[1])
        self.var_att_name.set(rows[2])
        self.var_att_dept.set(rows[3])
        self.var_att_time.set(rows[4])
        self.var_att_date.set(rows[5])
        self.var_att_attendnce.set(rows[6])

    def reset_data(self):
        self.var_att_id.set("")
        self.var_att_roll.set("")
        self.var_att_name.set("")
        self.var_att_dept.set("")
        self.var_att_time.set("")
        self.var_att_date.set("")
        self.var_att_attendnce.set("Status")


if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
