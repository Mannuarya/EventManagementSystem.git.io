from tkinter import *
from typing_extensions import ReadOnly
from PIL import Image, ImageTk
from tkinter import ttk
import pandas as pd 

class Report_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Details About Our Software & Project Developers")
        self.root.state('zoomed')

        lbl_title = Label(self.root, text="What our project Do.....?", font=("@SimSun", 16, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1278, height=50)

        frameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="EVENT MANAGEMENT SYSTEM", font=("@SimSun", 20, "bold"), padx=2, bg="black", fg="white")
        frameleft.place(x=0, y=53, width=1278, height=698)


       # btn_frame=Frame(frameleft,bg="black",bd=4,relief=RIDGE)
        #btn_frame.place(x=0,y=30,width=198,height=190)
        # ================== down images ===========================
        img4=Image.open(r"C:\Users\mannu\Desktop\mk-python\Screenshot 2023-12-09 001106.png")
        img4=img4.resize((230,172),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(frameleft,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=0,width=230,height=172)


        img5=Image.open(r"C:\Users\mannu\Desktop\mk-python\upcoming-img.jpg")
        img5=img5.resize((230,172),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(frameleft,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=172,width=230,height=172)


        img6=Image.open(r"C:\Users\mannu\Desktop\mk-python\upcoming-img.jpg")
        img6=img6.resize((230,172),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lblimg6=Label(frameleft,image=self.photoimg6,bd=4,relief=RIDGE)
        lblimg6.place(x=0,y=342,width=230,height=172)

        img7=Image.open(r"C:\Users\mannu\Desktop\mk-python\Screenshot 2023-12-09 001106.png")
        img7=img7.resize((230,102),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        lblimg7=Label(frameleft,image=self.photoimg7,bd=4,relief=RIDGE)
        lblimg7.place(x=0,y=510,width=230,height=102)

        #_______________________________________________________________________________________
######################        frame for paragraph            ##############################
        #____________________________________________________________________________________
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="floralwhite")
        main_frame.place(x=230, y=82, width=1045, height=698)

        img0=Image.open(r"C:\Users\mannu\Desktop\mk-python\upcoming-img.jpg")
        img0=img0.resize((1078,172),Image.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)

        lblimg0=Label(main_frame,image=self.photoimg0,bd=4,relief=RIDGE)
        lblimg0.place(x=0,y=0,width=1078,height=172)








#############   start paragraph*************************************************
        #__________________________________________________________________________________
        paragraph = '''           
                    _________________________________________________________________________________________________________________________
                    |
                    |                                                 CREDIT's
                    |
                    |                                                        
                    |
                    |            "TEAM-MEMBERS"                      "Developer"                         "DOCUMENTATION HANDLER"
                    |    
                    |    1. Indra singh jeena                    __MANISH KUMAR ARYA__                        1.Kalpana Mer
                    |    
                    |    2. Gaurav kabdwal                                                                    2.Neha Rana
                    |    
                    |    3. Neha Rana
                    |    
                    |    4. Kalpana Mer
                    |    
                    |    5. Manish Kumar Arya
                    |
                    | 
                    |                                                           
                    |            
                    |    
                    |                    "IMAGES PROVIDERS"                          "HELPING HANDS"        
                    |    
                    |                1.Manish Kumar Arya                             1.Inder Singh Jeena
                    |    
                    |                2.Gaurav Kabdwal                                2.Gaurav Kabdwal
                    |    
                    |                                                                3.Neha Rana'''
                                                                            

        new_paragraph =  '''
                    |    Event Management System is a powerful tool designed to streamline the process of organizing and managing events. 
                    |    Our system provides a user-friendly interface that allows users to easily plan, coordinate, and execute various 
                    |    types of events. Whether it's a conference, wedding, or corporate gathering, our system has you covered.
                    |
                    |    Key Features:
                    |    - Easy event creation and management
                    |    - Attendee registration and tracking
                    |    - Schedule and agenda management
                    |    - Real-time collaboration and communication
                    |    - Customizable templates for different event types
                    |                                                                                '''
        


          # New paragraph with a different font color (e.g., green)
        
        secondnew_paragraph ='''
                    |    Event Management System
                    |    1. Overview:
                    |        Your project is an Event Management System designed to simplify and streamline the process of
                    |        organizing and managing various types of events.
                    |
                    |    2. Main Features:
                    |        Event Creation and Management:
                    |            Users can easily create and manage events, including conferences, weddings,
                    |            and corporate gatherings.
                    |
                    |       Attendee Registration and Tracking:
                    |        The system allows for attendee registration, making it convenient to keep track of participants.
                    |
                    |       Schedule and Agenda Management:
                    |        Users can schedule events and manage agendas, ensuring smooth coordination during the event.
                    |
                    |       Real-time Collaboration and Communication:
                    |        The system supports real-time collaboration and communication, facilitating effective interaction 
                    |        among event organizers and participants.
                    |
                    |       Customizable Templates:
                    |        Customizable templates are available for different types of events, providing flexibility and 
                    |        efficiency in event planning.
                    |
                    |    3. User Interface:
                    |        Title Bar:
                    |        The application features a title bar with relevant details about the software and project.
                    |
                    |       Frames:
                    |        Utilizes frames for organizing different sections, such as event details and a paragraph
                    |        providing information about the project.
                    |
                    |       Text Area:
                    |        A text area is included to display a detailed paragraph about the Event Management System,
                    |        its key features, and goals.
                    |
                    |    4. Aesthetics:
                    |        Background Image:
                    |            The interface incorporates a background image to enhance visual appeal.
                    |
                    |        Color Scheme:
                    |            The color scheme includes black, white, and red, providing a professional and visually pleasing lo'''
                
                        
            
        another_new_paragraph = '''
                    |    5. Developer Information:
                    |        Details about the project developers are not explicitly mentioned in the provided code. If you have 
                    |        a separate section or window for developer information,you can highlight the team members, their roles,
                    |        and any relevant details about their contributions.
                    |    
                    |                   
                    |
                    |    6. Project Goal:
                    |        Simplify Event Management:
                    |        The ultimate goal is to simplify the event management process, making it efficient and enjoyable for
                    |        both organizers and participants.
                    |
                    |    7. Next Steps:
                    |        Ensure that the developer information section is added and appropriately populated.
                    |        Test the application thoroughly to identify and fix any potential issues.
                    |        Consider adding additional features or enhancements based on project requirements.
                    |
                    |        Remember, this is just a generalized overview based on the provided code. You can customize and expand 
                    |        upon these details to better reflect the specific goals and functionalities of your Event Management System. 
                    |        If you have any specific questions or
                    |        if there's anything specific you'd like to highlight, feel free to let me know!  
                                                                                                                '''
        another3rd_new_paragraph ='''
                    |                                     SEAT-BOOKING-INTERFACE :-
                    |
                    |
                    |
                    |
                    |                   For Adding some new Event-type:
                    |           here are the keys such as:
                    |
                    |
                    |   1.      NSS
                    |   2.      Farewell
                    |   3.      Fresher
                    |   4.      Football
                    |   5.      College--Anniversery
                    |   6.      Annual-Day
                    |   7.      Christmas
                    |
                    |
                    |
                    |
                    |           Because our EVENT-MANAGEMENT SYSTEM is a static type software system , that's why for "BILLING-METHOD" 
                    |            the organizer must have to some knowledge about "CRUD-OPERTAION" IN PYTHON 
                    |                    or if not then the time of setuping the system for any organization
                    |             , so the organization have to provide their EVENT-TYPE according to their self. 
                    |         Then the system will perform tasks as according to the organization for the systemn is provided .


'''

#frame for paragraph***************************************************
        txt_paragraph = Text(main_frame, wrap="word", font=("@SimSun", 10), bg="black", height=30, width=80)



#______1st paragraph------------------------------------
        txt_paragraph.tag_configure("paragraph_color", foreground="paleturquoise1")# Configure a tag named "paragraph_color" with the original font color (e.g., yellow)
        txt_paragraph.insert("1.0", paragraph, "paragraph_color")    # Apply the "paragraph_color" tag to the existing paragraph
        

#______2nd paragraph------------------------------------
        txt_paragraph.tag_configure("new_paragraph_color", foreground="lightseagreen")# Configure a new tag named "new_paragraph_color" with the new font color (e.g., green)
        txt_paragraph.insert("end", "\n\n" + new_paragraph, "new_paragraph_color") # Insert the new paragraph with the "new_paragraph_color" tag


#_______3rd paragraph--------------------------------------
        txt_paragraph.tag_configure("secondnew_paragraph_color", foreground="cyan4")# Configure a new tag named "new_paragraph_color" with the new font color (e.g., green)
        txt_paragraph.insert("end", "\n\n" + secondnew_paragraph, "secondnew_paragraph_color")



#______4rth paaragraph------------------------------------
        txt_paragraph.tag_configure("another_new_paragraph_color", foreground="darkseagreen")# Configure another new tag named "another_new_paragraph_color" with a different font color (e.g., blue)
        txt_paragraph.insert("end", "\n\n" + another_new_paragraph, "another_new_paragraph_color") # Insert another new paragraph with the "another_new_paragraph_color" tag


#______5th paaragraph------------------------------------
        txt_paragraph.tag_configure("another3rd_new_paragraph_color", foreground="azure")# Configure another new tag named "another_new_paragraph_color" with a different font color (e.g., blue)
        txt_paragraph.insert("end", "\n\n" + another3rd_new_paragraph, "another3rd_new_paragraph_color") # Insert another new paragraph with the "another_new_paragraph_color" tag



        txt_paragraph.place(x=0, y=159, width=1040, height=450)

        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=txt_paragraph.yview)
        scrollbar.place(x=1043, y=161, height=450, anchor="ne")
        txt_paragraph.config(yscrollcommand=scrollbar.set)


    

if __name__ == "__main__":
    root = Tk()
    obj = Report_win(root)
    root.mainloop()
