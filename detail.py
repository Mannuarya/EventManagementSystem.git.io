from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class BookingDetail:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking Management System")
        self.root.geometry("1082x520+202+200")



# ====================== title ================
        lbl_title=Label(self.root,text="seats",font=("@SimSun",16,"bold","underline"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1065,height=40)
# ====================== logo ==================
        img2=Image.open(r"C:\Users\mannu\Desktop\mk-python\Screenshot 2023-12-09 001106.png")
        img2=img2.resize((100,38),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=2,y=2,width=100,height=38)


        self.var_seats=StringVar()
        self.var_stages=StringVar()
        self.var_evtype=StringVar()

# ================== label frame ============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add New Events",font=("Broadway",10,"bold"),padx=2)
        labelframeleft.place(x=5,y=40,width=440,height=250)
#############################################           label and entries        ##########################################



        lbl_name=Label(labelframeleft,text="New-Seats.:-",font=("Broadway",10),padx=2,pady=6)
        lbl_name.grid(row=0,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,width=29,textvariable=self.var_seats,font=("Broadway"))
        entry_name.grid(row=0,column=1)


# available seats
        lbl_name=Label(labelframeleft,text="Stages:-",font=("Broadway",10),padx=2,pady=6)
        lbl_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,width=29,textvariable=self.var_stages,font=("Broadway"))
        entry_name.grid(row=1,column=1)


# event type
        lbl_name=Label(labelframeleft,text="Event Type:-",font=("Broadway",10),padx=2,pady=6)
        lbl_name.grid(row=2,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,width=29,textvariable=self.var_evtype,font=("Broadway"))
        entry_name.grid(row=2,column=1)



#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ======================= buttons ==============
#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=180,width=337,height=28)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("@SimSun",11),bg="aquamarine4",fg="white",width=9)
        btnadd.grid(row=0,column=0,padx=0)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("@SimSun",11),bg="aquamarine4",fg="white",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete_seat,font=("@SimSun",11),bg="aquamarine4",fg="white",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset_data,font=("@SimSun",11),bg="aquamarine4",fg="white",width=9)
        btnreset.grid(row=0,column=3,padx=1)


# ===============================================================================================================================
# ==================== table frame search system==========================
# ===============================================================================================================================
        tabelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Seat seats", font=("Broadway", 10, "bold"), padx=2,)
        tabelframeleft.place(x=460, y=40, width=550, height=250)


        scroll_x = ttk.Scrollbar(tabelframeleft, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabelframeleft, orient=VERTICAL)

        self.seat_table = ttk.Treeview(tabelframeleft, column=("Newseats","stages","Eventtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.seat_table.xview)
        scroll_y.config(command=self.seat_table.yview)

    
        
        self.seat_table.heading("Newseats", text="New-Seats")
        self.seat_table.heading("stages",text="Stages")
        self.seat_table.heading("Eventtype", text="Event-Type")


        self.seat_table["show"] = "headings"

        
        self.seat_table.column("Newseats", width=100)
        self.seat_table.column("stages",width=100)
        self.seat_table.column("Eventtype", width=100)

        self.seat_table.pack(fill=BOTH, expand=1)
        self.seat_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



        #add data======================================================
    def add_data(self):
        if self.var_stages.get()=="" or self.var_evtype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="manish1234",database="eventmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into seats values(%s,%s,%s)",(
                                                                
                                                                self.var_seats.get(),
                                                                self.var_stages.get(),
                                                                self.var_evtype.get()
                                                                                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Seat Has Added Successfully",parent=self.root)
             except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #===============fetch data===========================================================
 #===============fetch data===========================================================
  # ===============fetch data===========================================================
    def fetch_data(self):
        try:
                conn = mysql.connector.connect(host="localhost", username="root", password="manish1234", database="eventmanagement")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM seats")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.seat_table.delete(*self.seat_table.get_children())
                        for row in rows:
                                self.seat_table.insert("", END, values=row)
                conn.commit()
                conn.close()
        except mysql.connector.Error as err:
                print(f"Error fetching data: {err}")

# get cursor============================================================================================================
    def get_cursor(self, event=""):
        cursor_row = self.seat_table.focus()
        content = self.seat_table.item(cursor_row)
        row = content["values"]

        if len(row) >= 2:
                self.var_seats.set(row[0])
                self.var_stages.set(row[1])
                self.var_evtype.set(row[2])


    #update seat function==============================================================================================
# Update seat function
    def update(self):
        try:
                if self.var_stages.get() == "":
                        messagebox.showerror("Error", "Please Enter Stages", parent=self.root)
                else:
                        conn = mysql.connector.connect(host="localhost", user="root", password="manish1234", database="eventmanagement")
                        my_cursor = conn.cursor()
                        my_cursor.execute("update seats set stages=%s, Eventtype=%s WHERE Newseats=%s", (
                                self.var_stages.get(),
                                self.var_evtype.get(),
                                self.var_seats.get()
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Update", "Seat seats have been updated successfully:", parent=self.root)

        except mysql.connector.Error as err:
                # Display the error message using messagebox
                messagebox.showerror("Error", f"Error updating seat seats: {err}", parent=self.root)
                





        #delete seat function=========================================================================================================
    def delete_seat(self):
        # Ask for confirmation
        delete = messagebox.askyesno("Event Management System:", "Do you want to delete this seat?", parent=self.root)

        if delete:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="manish1234", database="eventmanagement")
                my_cursor = conn.cursor()

                # Delete the seat based on Newseats
                query = "DELETE FROM seats WHERE Newseats = %s"
                value = (self.var_seats.get(),)
                my_cursor.execute(query, value)

                # Commit changes and close the connection
                conn.commit()
                conn.close()

                # Refresh the Treeview to reflect the changes
                self.fetch_data()

                messagebox.showinfo("Success", "Seat Deleted Successfully!")
        else:
                messagebox.showinfo("Delete", "Deletion Cancelled.")



# reset @@@@@@@@@@@@@@@@@@@@@@@@@@22
    def reset_data(self):

        self.var_stages.set(""),
        self.var_seats.set(""),
        self.var_evtype.set(""),


if __name__ == "__main__":
    root = Tk()
    obj = BookingDetail(root)
    root.mainloop()