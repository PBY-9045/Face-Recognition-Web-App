from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class About_us:
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("About Us")
        title_lbl_about=Label(self.root,text="About Us",font=("script mt bold",40,"bold"),fg="light green")
        title_lbl_about.place(x=0,y=0,width=1530,height=150)

        right_frame_about=LabelFrame(self.root,bd=2,relief=RIDGE,text="About Developer",font=("times new roman",12,"bold"))
        right_frame_about.place(x=700,y=170,width=675,height=550)
        img_about=Image.open(r"IMG_6821.JPG")
        img_about=img_about.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg_about=ImageTk.PhotoImage(img_about)
        f_lbl_aboutimg_about=Label(right_frame_about,image=self.photoimg_about)
        #placing the image
        f_lbl_aboutimg_about.place(x=455,y=0,width=220,height=220)

        dev_label1=Label(right_frame_about,text="hello my name is prashamnt bhooshan ",font=("times new roman",12,"bold"),bg="white")
        dev_label1.place(x=0,y=5)
# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=About_us(root)
    root.mainloop()
