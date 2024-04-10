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
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

    # ============== Variables ========================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_Attendance=StringVar()

    #first Image
        img=Image.open(r"images\student1jpeg.jpeg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)
        label1=Label(self.root,image=self.photoimg)
        label1.place(x=0,y=0,width=800,height=200)

        #second Image
        img1=Image.open(r"images\student2jpeg.jpeg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        label1=Label(self.root,image=self.photoimg1)
        label1.place(x=800,y=0,width=800,height=200)

        #bg Image
        img3=Image.open(r"images\IMG-20230919-WA0005.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        #title label
        title_lb1=Label(bg_img,text="Attendance Management system",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=-100,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1343,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=500)


        img_left=Image.open(r"images\student3jpeg.jpeg")
        img_left=img_left.resize((645,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        label1=Label(Left_frame,image=self.photoimg_left)
        label1.place(x=5,y=0,width=645,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=650,height=300)

        # Lable and entry
        # Attendance ID
        AttendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=5,sticky=W)

        AttendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll
        rolllabel=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=10,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)
        
        # Name
        namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        namelabel.grid(row=1,column=0,padx=10,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Department
        deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        deplabel.grid(row=1,column=2,padx=10,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)

        # time
        timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timelabel.grid(row=2,column=0,padx=10,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        
        # Date
        datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        datelabel.grid(row=2,column=2,padx=10,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

        # Attendance
        Attendancelabel=Label(left_inside_frame,text="Attendance:",font=("times new roman",13,"bold"),bg="white")
        Attendancelabel.grid(row=3,column=0,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_Attendance,width=18,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=10,pady=1,sticky=W)
        self.atten_status.current(0)

         #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=213,width=458,height=34)

        save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        # delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=650,height=500)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=639,height=399)

        # =========== Scroll bar table==========

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID") 
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ========== fatch data ===================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #========import csv==========
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ========== Export csv==============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data Export","Your data Exported to "+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    #======= get cursor================

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_Attendance.set(rows[6])

    #============ Reset data==============

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_Attendance.set("")





if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()