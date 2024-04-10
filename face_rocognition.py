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


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title label
        title_lb1=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #first image
        img_top=Image.open(r"D:\New folder\FACE RECOGNIZATION  SYSTEM\images\IMG-20230919-WA0004.jpg")
        img_top=img_top.resize((630,620))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        label1=Label(self.root,image=self.photoimg_top)
        label1.place(x=0,y=55,width=630,height=620)

        #second image
        img_bottom=Image.open(r"D:\New folder\FACE RECOGNIZATION  SYSTEM\images\student3jpeg.jpeg")
        img_bottom=img_bottom.resize((950,620))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        label1=Label(self.root,image=self.photoimg_bottom)
        label1.place(x=630,y=55,width=950,height=620)

        # button
        b1_1=Button(label1,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=330,y=500,width=200,height=40)


        #=================== Attendence ==================

    def mark_attendence(self,i,r,n,d):
        with open("av.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now= datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #=============  face recognition =============

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Gudda@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                # n=str(n)
                n="".join(n)
            

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                # r=str(r)
                r="".join(r)


                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                # d=str(d)
                d="".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                # i=str(i)
                i="".join(i)
                # if n=="None" or d=="None" or i=="None" or r=="None":
                #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                #     cv2.putText(img,"Unkonwn Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                if confidence>85:
                    cv2.putText(img,f"Roll :{n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name :{r}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID :{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department :{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unkonwn Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clasifier.xml")
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()