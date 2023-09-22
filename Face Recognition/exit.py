from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("Student Data")
        #title_lbl=Label(text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("script mt bold",40,"bold"),fg="light green")
        #title_lbl.place(x=0,y=0,width=1530,height=150)
# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
