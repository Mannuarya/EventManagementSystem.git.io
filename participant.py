from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import re
import random
import mysql.connector
from tkinter import messagebox
class Part_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Participant Management System")
        self.root.geometry("1082x520+202+200")

        #====================== variable ====================
        #======================================================
        self.var_ecode=StringVar()
        x=random.randint(1000,9999)
        self.var_ecode.set(str(x))

        self.var_name=StringVar()
        #self.var_Etype=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        #self.var_event=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

# ====================== title ================
        lbl_title=Label(self.root,text="Add Participant details",font=("@SimSun",16,"bold","underline"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=100,y=0,width=1065,height=40)

# ====================== logo ==================
        img2=Image.open(r"C:\Users\mannu\Desktop\mk-python\Screenshot 2023-12-09 001106.png")
        img2=img2.resize((105,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=105,height=40)

# ================== label frame ============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="participant details",font=("Comic Sans MS",10,"bold"),padx=2,)
        labelframeleft.place(x=2,y=40,width=319,height=400)


#############################################           label and entries        ##########################################

# partcpnt name
        lbl_name=Label(labelframeleft,text="Participant Name :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_name.grid(row=0,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_name,width=25,font=("Comic Sans MS",8,"bold"))
        entry_name.grid(row=0,column=1)




#eventcode
        lbl_ecode=Label(labelframeleft,text="Event code :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_ecode.grid(row=1,column=0,sticky=W)

        entry_ecode=ttk.Entry(labelframeleft,textvariable=self.var_ecode,width=25,font=("Comic Sans MS",8,"bold"),state="readonly")
        entry_ecode.grid(row=1,column=1)


#EVENTS combobox
        #lbl_branch=Label(labelframeleft,text="Events :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        #lbl_branch.grid(row=2,column=0,sticky=W)

        ##combo_branch=ttk.Combobox(labelframeleft,textvariable=self.var_event,font=("Comic Sans MS",8,"bold"),width=22,state="readonly")
        3#3combo_branch["value"]=("Select Events","Fresher","Farewell","Annual-sports","Annual-Function","College-Seminar")
        #combo_branch.current(0)
        #combo_branch.grid(row=2,column=1)



# event type
     #   lbl_event=Label(labelframeleft,text="Event Type :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
      #  lbl_event.grid(row=3,column=0,sticky=W)
#
 #       combo_event=ttk.Combobox(labelframeleft,textvariable=self.var_Etype,font=("Comic Sans MS",8,"bold"),width=22,state="readonly")
  ##     combo_event.current(0)
    #    combo_event.grid(row=3,column=1)


#gender combobox
        lbl_gender=Label(labelframeleft,text="Gender :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=2,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("Comic Sans MS",8,"bold"),width=22,state="readonly")
        combo_gender["value"]=("Select Gender","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)


#mobile number
        lbl_mbnumber=Label(labelframeleft,text="Mobile number:-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_mbnumber.grid(row=3,column=0,sticky=W)

        entry_mbnumber=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=25,font=("Comic Sans MS",8,"bold"))
        entry_mbnumber.grid(row=3,column=1)

#email
        lbl_email=Label(labelframeleft,text="Email :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_email.grid(row=4,column=0,sticky=W)

        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=25,font=("Comic Sans MS",8,"bold"))
        entry_email.grid(row=4,column=1)


#idproof type combobox
        lbl_idproof=Label(labelframeleft,text="ID proof-Type :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_idproof.grid(row=5,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("Comic Sans MS",8,"bold"),width=22,state="readonly")
        combo_idproof["value"]=("Select ID","Aadhar","Pan-Card","Std.ID","College-ID","Dep.ID")
        combo_idproof.current(0)
        combo_idproof.grid(row=5,column=1)


#id number
        lbl_id=Label(labelframeleft,text="ID-Number :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_id.grid(row=6,column=0,sticky=W)

        lbl_id=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=25,font=("Comic Sans MS",8,"bold"))
        lbl_id.grid(row=6,column=1)

#address
        lbl_add=Label(labelframeleft,text="Address :-",font=("Comic Sans MS",8,"bold"),padx=2,pady=6)
        lbl_add.grid(row=7,column=0,sticky=W)

        lbl_add=ttk.Entry(labelframeleft,textvariable=self.var_address,width=25,font=("Comic Sans MS",8,"bold"))
        lbl_add.grid(row=7,column=1)




#==============================================================================================================================
# ======================= buttons ==============
#==============================================================================================================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=330,width=295,height=28)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("Comic Sans MS",8,"bold"),bg="aquamarine4",fg="white",width=9,cursor="hand2",activebackground="aquamarine4",activeforeground="aquamarine4")
        btnadd.grid(row=0,column=0,padx=0)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("Comic Sans MS",8,"bold"),bg="aquamarine4",fg="white",width=9,cursor="hand2",activebackground="aquamarine4",activeforeground="aquamarine4")
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("Comic Sans MS",8,"bold"),bg="aquamarine4",fg="white",width=9,cursor="hand2",activebackground="aquamarine4",activeforeground="aquamarine4")
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("Comic Sans MS",8,"bold"),bg="aquamarine4",fg="white",width=9,cursor="hand2",activebackground="aquamarine4",activeforeground="aquamarine4")
        btnreset.grid(row=0,column=3,padx=1)




#===============================================================================================================================
# ==================== table frame search system==========================
#===============================================================================================================================
        tabelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("Comic Sans MS",10,"bold"),padx=2,)
        tabelframeleft.place(x=315,y=40,width=750,height=400)

        lblsearchby=Label(tabelframeleft,text="Search By :",font=("Comic Sans MS",10,"bold"),bg="aquamarine4",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelframeleft,textvariable=self.search_var,font=("Comic Sans MS",10,"bold"),width=30,state="readonly")
        combo_search["value"]=("Select","Mobile","EventCode")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)



        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tabelframeleft,textvariable=self.txt_search,width=20,font=("Comic Sans MS",10,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(tabelframeleft,text="Search",command=self.search,font=("Comic Sans MS",8,"bold"),bg="aquamarine4",fg="white",width=9,cursor="hand2",activebackground="aquamarine4",activeforeground="aquamarine4")
        btnsearch.grid(row=0,column=3,padx=0)

        btnshowall=Button(tabelframeleft,text="Show All",command=self.fetch_data,font=("Comic Sans MS",8,"bold"),bg="aquamarine4",fg="white",width=9,cursor="hand2",activebackground="aquamarine4",activeforeground="aquamarine4")
        btnshowall.grid(row=0,column=4,padx=1)


#=============================================================================================================================
# ============== show data table =================================
#=============================================================================================================================
        details_table=Frame(tabelframeleft,bd=2,relief=RIDGE)
        details_table.place(x=0,y=30,width=742,height=290)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.part_details_Table=ttk.Treeview(details_table,column=("EventCode","ParticipantName","Gender","Mobile","Email","IDProofType","ID_Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.part_details_Table.xview)
        scroll_y.config(command=self.part_details_Table.yview)


        
        self.part_details_Table.heading("EventCode",text="Event Code")
        self.part_details_Table.heading("ParticipantName",text="Participant Name")
        #self.part_details_Table.heading("EventsType",text="Event Type")
        self.part_details_Table.heading("Gender",text="Gender")
        self.part_details_Table.heading("Mobile",text="Mobile Number")
        self.part_details_Table.heading("Email",text="E-mail")
        self.part_details_Table.heading("IDProofType",text="IDProofType")
        self.part_details_Table.heading("ID_Number",text="ID_Number")
        self.part_details_Table.heading("Address",text="Address")
   
        

        self.part_details_Table["show"]="headings"

        self.part_details_Table.column("EventCode",width=150)
        self.part_details_Table.column("ParticipantName",width=100)
       # self.part_details_Table.column("EventsType",width=100)
        self.part_details_Table.column("Gender",width=100)
        self.part_details_Table.column("Mobile",width=100)
        self.part_details_Table.column("Email",width=100)
        self.part_details_Table.column("IDProofType",width=100)
        self.part_details_Table.column("ID_Number",width=100)
        self.part_details_Table.column("Address",width=100)
       
        

        self.part_details_Table.pack(fill=BOTH,expand=1)
        self.part_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_ecode.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Address")
        else:
             try:
                conn=mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into participant values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ecode.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get()
                                                                                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Participant has been added",parent=self.root)
             except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from participant")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.part_details_Table.delete(*self.part_details_Table.get_children())
            for i in rows:
                self.part_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.part_details_Table.focus()
        content=self.part_details_Table.item(cursor_row)
        row=content["values"]

        if len(row) >= 2:
                self.var_ecode.set(row[0]),
                self.var_name.set(row[1]),
                self.var_gender.set(row[2]),
                self.var_mobile.set(row[3]),
                self.var_email.set(row[4]),
                self.var_address.set(row[5]),
                self.var_id_proof.set(row[6]),
                self.var_id_number.set(row[7])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("update participant set ParticipantName=%s,Gender=%s,Mobile=%s,Email=%s,Address=%s,IDProofType=%s,ID_Number=%s  where EventCode=%s",(
                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                self.var_ecode.get()
                                                                                                                                                                
                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Participant details has been updated successfully :",parent=self.root)


    def delete(self):
        delete=messagebox.askyesno("Event Management System :","Do You Want Delete This Participant",parent=self.root)
        if delete>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
                my_cursor=conn.cursor()
                query="delete from participant where EventCode=%s"
                value=(self.var_ecode.get(),)
                my_cursor.execute(query,value)
        else:
                if not delete:
                        return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        
        self.var_name.set(""),
      
        self.var_mobile.set(""),
        self.var_email.set(""),
    
        self.var_address.set(""),
       
        self.var_id_number.set("")
        x=random.randint(1000,9999)
        self.var_ecode.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from participant where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
             self.part_details_Table.delete(*self.part_details_Table.get_children())
             for i in rows:
                  self.part_details_Table.insert("",END,values=i)
             conn.commit()
        conn.close()

if __name__== "__main__":
    root=Tk()
    obj=Part_Win(root)
    root.mainloop()
