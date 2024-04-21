# event management system
from tkinter import*
from PIL import ImageTk
from PIL import Image, ImageTk
import tkinter as tk
from participant import Part_Win
from seatbooking import Seat_booking
from detail import BookingDetail
from report import Report_win

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

if __name__ == "__main__":
    root = Tk()
    obj=EventManagementSystem(root)
    root.mainloop()
