from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("Train data")
        title_lbl_Train=Label(self.root,text="Train The dataset",font=("script mt bold",40,"bold"),bg="Black",fg="light green")
        title_lbl_Train.place(x=0,y=0,width=1530,height=150)

        img_bg=Image.open(r"Train_data.jpeg")
        img_bg=img_bg.resize((1530,640),Image.Resampling.LANCZOS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)
        f_lbl_bg=Label(self.root,image=self.photoimg_bg)
        #placing the image
        f_lbl_bg.place(x=0,y=151,width=1530,height=640)
        img1=Image.open(r"studentdata.jpg")
        img1=img1.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(f_lbl_bg,command=self.train_class,image=self.photoimg1,cursor="hand2")
        b1.place(x=200,y=80,width=220,height=220)
        b11=Button(f_lbl_bg,text="Train Data",command=self.train_class,cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b11.place(x=200,y=280,width=220,height=50)


    def train_class(self):
        data_dir=("Data")
        path= [os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#converting image in grayscale
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifier and save it
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
       




# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
