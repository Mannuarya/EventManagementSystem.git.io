from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import re
import mysql.connector
from participant import Part_Win
from seatbooking import Seat_booking
from detail import BookingDetail
from event import EventManagementSystem
from report import Report_win

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login To Be A Part Of Our Participant:")
        self.root.geometry("1270x698+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mannu\Desktop\mk-python\loginimg.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #(((((((((((((((((((((())))))))))))))))))))))         frame            (((((((((((((((((((((((((((((())))))))))))))))))))))))))))))
        frame=Frame(self.root,bg="black")
        frame.place(x=480,y=100,width=340,height=450)

        img1=Image.open(r"C:\Users\mannu\Desktop\mk-python\images.png")
        img1=img1.resize((100,90),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg,bg="black",borderwidth=0)
        lblimg1.place(x=600,y=105,width=100,height=90)

        get_str=Label(frame,text="Login-Here",font=("@SimSun",20,"bold"),fg="light goldenrod",bg="black")
        get_str.place(x=87,y=95)

        #((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((          label        ))))))))))))))))))))))))))))))))))))))))))))))))))))
        username=lbl=Label(frame,text="Username",font=("@SimSun",15),fg="gold",bg="black")
        username.place(x=50,y=155)

        self.txtemail=ttk.Entry(frame,font=("@SimSun",14,"bold"))
        self.txtemail.place(x=30,y=185,width=270)


        password=lbl=Label(frame,text="Password",font=("@SimSun",15),fg="gold",bg="black")
        password.place(x=50,y=220)

        self.txtpass=ttk.Entry(frame,font=("@SimSun",14,"bold"), show="*")
        self.txtpass.place(x=30,y=250,width=270)

        #(((((((((((((((((((((((((((((((((((((((((              icon images               )))))))))))))))))))))))))))))))))))))))))
        img2=Image.open(r"C:\Users\mannu\Desktop\mk-python\images.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=255,width=25,height=25)

        img3=Image.open(r"C:\Users\mannu\Desktop\mk-python\128590131-black-invisible-or-hide-icon-isolated-on-black-background-silver-square-button-vector-illustration.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img3)

        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=500,y=320,width=25,height=25)

        #(((((((((((((((((((((((((((((((((((((((((((((((        login button        )))))))))))))))))))))))))))))))))))))))))))))))
        loginbtn=Button(frame,text="Login",command=self.login,font=("@SimSun",11),cursor="hand2",bd=3,relief=RIDGE,fg="white",bg="red3",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #(((((((((((((((((((((((((((((((((((((((((((((((        register button       )))))))))))))))))))))))))))))))))))))))))))))))
        registerbtn=Button(frame,text="Register ",command=self.register_window,font=("@SimSun",10),cursor="hand2",fg="gold",bg="black",borderwidth=0,activebackground="black",activeforeground="gold")
        registerbtn.place(x=96,y=337,width=160)

        #((((((((((((((((((((((((((((((((((((((((((((((((       forgetpassword button   ))))))))))))))))))))))))))))))))))))))))))))))))
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("@SimSun",10),cursor="hand2",fg="gold",bg="black",borderwidth=0,activebackground="black",activeforeground="gold")
        forgetbtn.place(x=90,y=363,width=165)


#register window function for ----------------------REGISTER BUTTON-------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       login function          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def login(self):
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.txtemail.get()):
            messagebox.showerror("Error", "Invalid Email Format")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",(
                                                                                        self.txtemail.get(),
                                                                                        self.txtpass.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=EventManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


#--------#################################          RESET PASSWORD                  ########################----------------------
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txtsecurityans.get()=="":
            messagebox.showerror("Error","Enter your answer",parent=self.root2)
        elif self.txt_pass_entrycls.get()=="":
            messagebox.showerror("Error","Enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="manish1234",database="eventmanagement")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securtiyA=%s")
            value=(self.txtemail.get(),self.combo_security_Q.get(),self.txtsecurityans.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.txt_pass_entrycls.get(),self.txtemail.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Now login with new password",parent=self.root2)

                self.root2.destroy()





#--------#################################          FORGET PASWORD WINDOW           ########################----------------------
                

    def forgot_password_window(self):
        if self.txtemail.get() == "":
            messagebox.showerror("Error", "Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="manish1234", database="eventmanagement")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtemail.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror('Username Not Found', 'This Username is not registered')
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+480+110")

                self.bg1=ImageTk.PhotoImage(file=r"C:\Users\mannu\Desktop\mk-python\c.jpg")
                lbl_bg1=Label(self.root2,image=self.bg1)
                lbl_bg1.place(x=0,y=0,relwidth=1,relheight=1)

                l = Label(self.root2, text="Forget Password", font=("@SimSun", 18,"bold","underline"), fg="red", bg="black")  # Set bg to black
                l.place(x=0, y=15, relwidth=1)

                securtiy_lbl = Label(self.root2, text="Select Security Question", font=("@SimSun", 12, "bold"), bg="black", fg="white")
                securtiy_lbl.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("@SimSun", 12, "bold"), state="readonly",cursor="hand2")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Father Name", "Your Sister name if you remember", "Your Pet Name")

                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                securityans_lbl = Label(self.root2, text="Security Answer", font=("@SimSun", 12, "bold"), bg="black", fg="white")
                securityans_lbl.place(x=50, y=140)

                self.txtsecurityans = ttk.Entry(self.root2, font=("@SimSun", 12, "bold"),cursor="hand2")
                self.txtsecurityans.place(x=50, y=170, width=210)

                new_pass = Label(self.root2, text="New-Password", font=("@SimSun", 13,"bold"), bg="black", fg="white")
                new_pass.place(x=50, y=240)

                self.txt_pass_entrycls = ttk.Entry(self.root2, font=("@SimSun", 13),cursor="hand2")
                self.txt_pass_entrycls.place(x=50, y=270, width=210)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("@SimSun", 15,"bold"), bg="green", fg="black",bd=0,cursor="hand2",borderwidth=0,activebackground="green",activeforeground="black")
                btn.place(x=133, y=345)



#################______________________register window__________________________##############################################
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
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mannu\Desktop\mk-python\pexels-no-name-66997.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#           ((((((((((((((((((((((((((((((((((((((((((((((((((      left image      ))))))))))))))))))))))))))))))))))))))))))))))))))
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\mannu\Desktop\mk-python\vertical-pictures-r93cdchwdse79vvv (1).jpg")
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
        img1=Image.open(r"C:\Users\mannu\Desktop\mk-python\register.png")
        img1=img1.resize((100,40),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.register_data,borderwidth=0,cursor="hand2",font=("Comic Sans MS",15,"bold"))
        b1.place(x=55,y=394,width=100)

        img2=Image.open(r"C:\Users\mannu\Desktop\mk-python\login-button-png-1 (1).png")
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

    def return_login(self):
        self.root.destroy()



###########################__________________________Event window___________________________################################
class EventManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Event Management System")
        self.root.geometry("1300x800+0+0")


# ===================== 1st image ==========
        img1=Image.open(r"C:\Users\mannu\Desktop\mk-python\upcoming-img.jpg")
        img1=img1.resize((1110,120),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=180,y=0,width=1098,height=120)



# ====================== logo ==================
        img2=Image.open(r"C:\Users\mannu\Desktop\mk-python\Screenshot 2023-12-09 001106.png")
        img2=img2.resize((180,120),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=180,height=120)



# ====================== title ================
        lbl_title=Label(self.root,text="MANAGE YOUR EVENTS",font=("@SimSun",23,"bold","underline"),bg="black",fg="mintcream",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=120,width=1276,height=52)





#============================================================================================
#========================= main frame ==========
#===========================================================================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        main_frame.place(x=0,y=170,width=1276,height=645)









# ====================== menu ==================
        lbl_menu=Label(main_frame,text="MANAGE-EVENTS",font=("@SimSun",15,"bold"),bg="black",fg="mediumorchid4",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=196)


#========================= button ==========
        btn_frame=Frame(main_frame,bg="black",bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=198,height=190)


        cust_btn=Button(btn_frame,text="Participant",command=self.part_details,width=19,font=("@SimSun",13,"bold"),bg="black",fg="cornflowerblue",bd=0,cursor="hand2",borderwidth=0,activebackground="cornflowerblue",activeforeground="black")
        cust_btn.grid(row=0,column=0,pady=1)

        rm_btn=Button(btn_frame,text="Book-Seat",command=self.seatbooking,width=19,font=("@SimSun",13,"bold"),bg="black",fg="cornflowerblue",bd=0,cursor="hand2",borderwidth=0,activebackground="cornflowerblue",activeforeground="black")
        rm_btn.grid(row=1,column=0,pady=1)

        det_btn=Button(btn_frame,text="Details",width=19,command=self.booking_details,font=("@SimSun",13,"bold"),bg="black",fg="cornflowerblue",bd=0,cursor="hand2",borderwidth=0,activebackground="cornflowerblue",activeforeground="black")
        det_btn.grid(row=2,column=0,pady=1)

        rep_btn=Button(btn_frame,text="Report",width=19,command=self.Reportwin,font=("@SimSun",13,"bold"),bg="black",fg="cornflowerblue",bd=0,cursor="hand2",borderwidth=0,activebackground="cornflowerblue",activeforeground="black")
        rep_btn.grid(row=3,column=0,pady=1)

        lgt_btn=Button(btn_frame,text="Log-Out",width=19,command=self.logout,font=("@SimSun",13,"bold"),bg="black",fg="cornflowerblue",bd=0,cursor="hand2",borderwidth=0,activebackground="cornflowerblue",activeforeground="black")
        lgt_btn.grid(row=4,column=0,pady=1)



# ================= right side image ===============
        img3=Image.open(r"C:\Users\mannu\Desktop\mk-python\radiant-energy-heatwaves-illustration.png")
        img3=img3.resize((1082,520),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=195,y=0,width=1082,height=520)



# ================== down images ===========================
        img4=Image.open(r"C:\Users\mannu\Desktop\mk-python\abstract-neon-background-luminous-swirling-260nw-2153188987.png")
        img4=img4.resize((196,168),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=190,width=196,height=168)


        img5=Image.open(r"C:\Users\mannu\Desktop\mk-python\magical-purple-ring-light-smoke-260nw-2315950049.png")
        img5=img5.resize((195,168),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=352,width=196,height=168)



    def part_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Part_Win(self.new_window)


    def seatbooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Seat_booking(self.new_window)

    def booking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=BookingDetail(self.new_window)

    def Reportwin(self):
        self.new_window=Toplevel(self.root)
        self.app=Report_win(self.new_window)

    def EventManagementSystem(self):
        self.new_window=Toplevel(self.root)
        self.app=EventManagementSystem(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__=="__main__":
    main()



























