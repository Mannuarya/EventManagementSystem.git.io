from tabnanny import check
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1273x685+0+0")

        #+++++++++++++++++++++++++++++   variables              +++++++++++++++++++++
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securtiyA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

#           ((((((((((((((((((((((((((((((((((((((((((((((((        bg image        ))))))))))))))))))))))))))))))))))))))))))))))))
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mannu\OneDrive\Desktop\mk-python\pexels-no-name-66997.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#           ((((((((((((((((((((((((((((((((((((((((((((((((((      left image      ))))))))))))))))))))))))))))))))))))))))))))))))))
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\mannu\OneDrive\Desktop\mk-python\vertical-pictures-r93cdchwdse79vvv (1).jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=80,width=400,height=450)

#           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  main frame           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=80,width=700,height=450)

        reg_lbl=Label(frame,text="REGISTER HERE",font=("Comic Sans MS",15,"bold"),fg="darkgreen",bg="white")
        reg_lbl.place(x=20,y=20)


#-------------------label and entries-----------------~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #   ***********************************        row-1           *******************************
        fname=Label(frame,text="First Name",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        fname.place(x=50,y=90)
        self.txt_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Comic Sans MS",10,"bold"))
        self.txt_entry.place(x=50,y=115,width=210)
                                ###################################
        l_name=Label(frame,text="Last Name",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=90)
        self.txtname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Comic Sans MS",10,"bold"))
        self.txtname_entry.place(x=370,y=115,width=210)




        #       *******************************        row---2                  *************************
        cont_lbl=Label(frame,text="Contact No.",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        cont_lbl.place(x=50,y=160)
        self.txtentry=ttk.Entry(frame,textvariable=self.var_contact,font=("Comic Sans MS",10,"bold"))
        self.txtentry.place(x=50,y=185,width=210)
                                ################################
        email_lbl=Label(frame,text="Email",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        email_lbl.place(x=370,y=160)
        self.txt_email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Comic Sans MS",10,"bold"))
        self.txt_email_entry.place(x=370,y=185,width=210)




        #         *********************************             row--3          ***************************
        securtiy_lbl=Label(frame,text="Select Security Question",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        securtiy_lbl.place(x=50,y=230)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Comic Sans MS",8,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your EX Name-if you remember","Your Pet Name")
        self.combo_security_Q.place(x=50,y=255,width=210)
        self.combo_security_Q.current(0)
                                ##################################
        securityans_lbl=Label(frame,text="Security Answer",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        securityans_lbl.place(x=370,y=230)
        self.txtsecurityans=ttk.Entry(frame,textvariable=self.var_securtiyA,font=("Comic Sans MS",10,"bold"))
        self.txtsecurityans.place(x=370,y=255,width=210)




        #       ***********************************             row--4          ******************************
        pass_lbl=Label(frame,text="Password",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        pass_lbl.place(x=50,y=300)

        self.txt_pass_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("Comic Sans MS",10,"bold"))
        self.txt_pass_entry.place(x=50,y=325,width=210)
                        ########################################
        conf_pass_lbl=Label(frame,text="Confirm Password",font=("Comic Sans MS",10,"bold"),bg="white",fg="black")
        conf_pass_lbl.place(x=370,y=300)
        
        self.txt_conf_pass_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("Comic Sans MS",10,"bold"))
        self.txt_conf_pass_entry.place(x=370,y=325,width=210)


#                               check button @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        checkbtn=Checkbutton(frame,text="I Agree The Terms And Condition",variable=self.var_check,font=("Comic Sans MS",7,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=358)


        #########################               buttons                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        img1=Image.open(r"C:\Users\mannu\OneDrive\Desktop\mk-python\register.png")
        img1=img1.resize((100,40),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.register_data,borderwidth=0,cursor="hand2",font=("Comic Sans MS",15,"bold"))
        b1.place(x=55,y=394,width=100)

        img2=Image.open(r"C:\Users\mannu\OneDrive\Desktop\mk-python\login-button-png-1 (1).png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(frame,image=self.photoimg2,command=self.logout,borderwidth=0,cursor="hand2",font=("Comic Sans MS",15,"bold"))
        b2.place(x=350,y=394,width=100)

        
#                                                               function declaration ***********************************************************
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password Does Not Match with Confirm Password!")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Condition")

        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Address")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Please","Participant already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(), #its a tupple!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securtiyA.get(),
                                                                                        self.var_pass.get()
                                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully:")

            
    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()