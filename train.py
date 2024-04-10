from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title label
        title_lb1=Label(self.root,text="Train data set",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\New folder\FACE RECOGNIZATION  SYSTEM\images\student3jpeg.jpeg")
        img_top=img_top.resize((1530,325))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        label1=Label(self.root,image=self.photoimg_top)
        label1.place(x=0,y=55,width=1530,height=325)

        img_bottom=Image.open(r"D:\New folder\FACE RECOGNIZATION  SYSTEM\images\student3jpeg.jpeg")
        img_bottom=img_bottom.resize((1530,325))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        # button
        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=379,width=1430,height=60)
        
        label1=Label(self.root,image=self.photoimg_bottom)
        label1.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ====== Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clasifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")

if __name__=='__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()