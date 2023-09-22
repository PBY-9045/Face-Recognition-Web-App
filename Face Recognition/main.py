#tickner is imported to design the page it contains items related to designing...
from tkinter import*
#ttk is also a library of tknier for designing and alignment purpose...
from tkinter import ttk
from tkinter import messagebox
#pil is for working on images it contains the libraries related to images...
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from recognize import Face_recog
from attendence import Attendence
from about_app import About_us
from help import Help
from time import strftime
from datetime import datetime



class face_recognition_system:
    #making a function and in this init always root and self is passed to make a platform and the root of the platform ...
    def __init__(self,root):
        self.root=root
        #setting the dimension of the root page with .geometry...
        self.root.geometry("1530x790+0+0")

        #setting the title of the root page....
        self.root.title("Face Recognition System")
        # label is used for setting the label for anything or simply the name or heading of something font is for setting font (name, size of font ,style)
        #fg is for fareground color and bg is for background color...
        title_lbl=Label(text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("script mt bold",40,"bold"),bg="black",fg="light green")
        #.place is used to give the position of something and place it at their proper place..
        title_lbl.place(x=0,y=0,width=1530,height=150)
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background='black',foreground='light green')
        lbl.place(x=5,y=(-15),width=100,height=50)
        time()
        #setting the background of the page...
        #image.open is use to import any image from anywhere by giving path either we use r to set directory or we will use forward slash in place of backward slash...
        img=Image.open(r"img1.jpg")
        #resize is used for setting the size of place  and antialisas is used for smoothening the image 
        img=img.resize((1530,640),Image.Resampling.LANCZOS)
        #PhotoImage and image tk is for image setting
        self.photoimg=ImageTk.PhotoImage(img)
        #when we make label of image we pass parameter in it (where it is places on inage or on root then image path )
        f_lbl=Label(self.root,image=self.photoimg)
        #placing the image
        f_lbl.place(x=0,y=151,width=1530,height=640)

        #setting the button 1 student data....
        img1=Image.open(r"studentdata.jpg")
        img1=img1.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(f_lbl,command=self.Student_detail,image=self.photoimg1,cursor="hand2")
        b1.place(x=200,y=80,width=220,height=220)
        b11=Button(f_lbl,command=self.Student_detail,text="Student Data",cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b11.place(x=200,y=280,width=220,height=50)
        
        #setting the button 1 Face capture....
        img2=Image.open(r"capture face.jpg")
        img2=img2.resize((220,220),Image.Resampling.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(f_lbl,command=self.Recognizer,image=self.photoimg2,cursor="hand2")
        b2.place(x=500,y=80,width=220,height=220)
        b12=Button(f_lbl,command=self.Recognizer,text="Face Recognizer",cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b12.place(x=500,y=280,width=220,height=50)
        
        #setting the button 1 Attendence ....
        img3=Image.open(r"attendence.jpg")
        img3=img3.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(f_lbl,command=self.attend,image=self.photoimg3,cursor="hand2")
        b3.place(x=800,y=80,width=220,height=220)
        b13=Button(f_lbl,command=self.attend,text="Attendence ",cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b13.place(x=800,y=280,width=220,height=50)
        
        #setting the button 4 Help....
        img4=Image.open(r"help.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(f_lbl,command=self.help,image=self.photoimg4,cursor="hand2")
        b4.place(x=1100,y=80,width=220,height=220)
        b14=Button(f_lbl,text="Help",command=self.help,cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b14.place(x=1100,y=280,width=220,height=50)
        
        #setting the button 5 Train Data....
        img5=Image.open(r"train data.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b5=Button(f_lbl,command=self.train_data,image=self.photoimg5,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)
        b15=Button(f_lbl,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b15.place(x=200,y=580,width=220,height=50)
        
        #setting the button 6 Photos....
        img6=Image.open(r"photos.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b6=Button(f_lbl,image=self.photoimg6,cursor="hand2",command=self.open_image)
        b6.place(x=500,y=380,width=220,height=220)
        b16=Button(f_lbl,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b16.place(x=500,y=580,width=220,height=50)
        
        #setting the button 7 About APP....
        img7=Image.open(r"about us.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b7=Button(f_lbl,command=self.about,image=self.photoimg7,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)
        b17=Button(f_lbl,command=self.about,text="About APP",cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b17.place(x=800,y=580,width=220,height=50)

        #setting the button 8 Exit....
        img8=Image.open(r"exit.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b8=Button(f_lbl,command=self.iexit,image=self.photoimg8,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)
        b18=Button(f_lbl,command=self.iexit,text="Exit",cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b18.place(x=1100,y=580,width=220,height=50)

    def Student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def open_image(self):
        os.startfile("Data")

    def Recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recog(self.new_window)

    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def about(self):
        self.new_window=Toplevel(self.root)
        self.app=About_us(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def iexit(self):
        self.iexit = messagebox.askyesno("Face recognition ", "Are you sure you want to exit this project")
        if self.iexit>0:
            self.root.destroy()
        else:
            return

# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()

