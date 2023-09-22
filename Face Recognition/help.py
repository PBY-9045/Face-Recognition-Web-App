from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help :
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("Help")
        title_lbl_help=Label(self.root,text="Help Desk",font=("script mt bold",40,"bold"),fg="light green")
        title_lbl_help.place(x=0,y=0,width=1530,height=150)

        right_frame_help=LabelFrame(self.root,bd=2,relief=RIDGE,text="For Any Queries",font=("times new roman",12,"bold"))
        right_frame_help.place(x=200,y=170,width=675,height=250)
        img_help=Image.open(r"IMG_6821.JPG")
        img_help=img_help.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg_help=ImageTk.PhotoImage(img_help)
        f_lbl_aboutimg_help=Label(right_frame_help,image=self.photoimg_help)
        #placing the image
        f_lbl_aboutimg_help.place(x=455,y=0,width=220,height=220)

        dev_label1=Label(right_frame_help,text=" Email:- pby@gmail.com ",font=("times new roman",12,"bold"),bg="white")
        dev_label1.place(x=20,y=5)
# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
