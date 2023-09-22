from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_recog:
    def __init__(self,root):
        self.root=root
        #setting the dimension of the page....
        self.root.geometry("1530x790+0+0")

        #setting the title of the page....
        self.root.title("Face Recognizer")
        title_lbl_fr=Label(self.root,text="FACE RECOGNIZATION ",font=("script mt bold",40,"bold"),bg="Black",fg="light green")
        title_lbl_fr.place(x=0,y=0,width=1530,height=150)

        img_l=Image.open(r"Fr.jpg")
        img_l=img_l.resize((750,640),Image.Resampling.LANCZOS)
        self.photoimg_l=ImageTk.PhotoImage(img_l)
        f_lbl_l=Label(self.root,image=self.photoimg_l)
        f_lbl_l.place(x=10,y=151,width=750,height=640)

        img_r=Image.open(r"Face-Recognition.jpg")
        img_r=img_r.resize((750,640),Image.Resampling.LANCZOS)
        self.photoimg_r=ImageTk.PhotoImage(img_r)
        f_lbl_r=Label(self.root,image=self.photoimg_r)
        f_lbl_r.place(x=755,y=151,width=760,height=640)

        b13=Button(f_lbl_r,command=self.face_recog,text="Recognizer ",cursor="hand2",font=("times new roman",15,"bold","italic"),fg="black",bg="white")
        b13.place(x=30,y=360,width=300,height=50)

    def mark_attendence(self,i,r,n,d):
        with open("Prashant.csv","r+",newline="\n") as f:
            m_data_list=f.readlines()
            name_list=[]
            for line in m_data_list:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtstr=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstr},{d1},Present")


    #face recognization function
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Pby96@2000",database="face_recognition")
                my_cursor=conn.cursor()


                my_cursor.execute("select Name from student_data where ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll_no from student_data where Id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dept from student_data where Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select ID from student_data where ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if n == "None"  or i == "None":
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                elif confidence>77:
                    cv2.putText(img, f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll_no:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1) ==13:
                break
            
            
        video_cap.release()
        cv2.destroyAllWindows()

# calling from the main function
if __name__ == "__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()
 