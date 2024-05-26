import streamlit as st
from tkinter import *
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
from PIL import Image
import re
import random
import smtplib
import time
import numpy as np
import cv2
import os

##############################################+=============================================================
root = tk.Tk()
root.configure(background="beige")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
img = Image.open("D:/Voting System/e-voting updated/vi.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
root.title("Login Form")




voter_id = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



# CREATE TABLE "user_reg" (
# 	"id"	INTEGER,
# 	"Fullname"	TEXT,
# 	"Adhar_No"	INTEGER,
# 	"Voter_ID"	TEXT,
# 	"Password"	TEXT,
# 	"Phone_No"	INTEGER,
# 	"Email_id"	TEXT,
# 	"status"	TEXT,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# );


def registration():
    from subprocess import call
    call(["python","face_registartion.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS user_reg "
                            "(id	INTEGER, Fullname TEXT, Adhar_No INTEGER, Voter_ID TEXT, Password TEXT,Phone_No INTEGER,Email_id TEXT , status TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM user_reg WHERE Voter_ID = ? and Password = ?')
         c.execute(find_entry, [(voter_id.get()), (password.get())])
         result = c.fetchall()
         for row in result: ##############################################################################
             print("id=",row[0],)########################################################################
             id=str(row[0])
             print(id)
             with open(r"id.txt", 'w') as f:
                 
             
                f.write(str(id))##########################################################################

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_R_V.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


#bg1_icon=ImageTk.PhotoImage(file="E:\\30%-phising-attack\\b2.png")

bg_icon=ImageTk.PhotoImage(file="L.jpg")
user_icon=ImageTk.PhotoImage(file="l1.png")
pass_icon=ImageTk.PhotoImage(file="p1.jpg")
        
# bg_lbl=tk.Label(root,image=bg1_icon, width=600,height=600)
# bg_lbl.place(x=50,y=50)
        
title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="black",fg="white")
title.place(x=650,y=100,width=300)
        
Login_frame=tk.Frame(root,bg="aquamarine4")
Login_frame.place(x=560,y=290,width=480,height=320)



def forgot_password():
    win = Toplevel()
    window_width = 600
    window_height = 280
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.iconbitmap('vi.ico')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)
    
    
    
    
    
    def generate_otp():
       return ''.join(random.choices('0123456789', k=6))  # Generates a 6-digit OTP

       # Function to send OTP via email
    def send_otp_email(receiver_email, otp):
        sender_email = "sdabholkar081@gmail.com"  # Replace with your email
        sender_password = "eiqb ichh seew zwbo"  # Replace with your email password or App Password

        message = f"Subject: Your OTP\n\nYour OTP is: {otp}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace smtp.example.com with your SMTP server
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message)
            ms.showinfo("OTP Sent", "OTP sent successfully!")
            return otp
        except Exception as e:
            ms.showerror("Error", f"Failed to send OTP. Error: {e}")
            return None
        # Function to verify OTP
    def verify_otp(input_otp, original_otp):
        return input_otp == original_otp
        # Function to handle sending OTP
    def send_otp():
        receiver_email = email_entry.get()
        if receiver_email:
            global otp  # Ensure 'otp' is accessible in the global scope
            otp = generate_otp()
            send_otp_email(receiver_email, otp)
        else:
            ms.showwarning("Warning", "Please enter an email address.")
       # Function to handle OTP verification
    def verify():
        user_input = otp_entry.get()
        if user_input:
            if verify_otp(user_input, otp):
                ms.showinfo("OTP Verified", "OTP verification successful!")
                update_pass()

    ##############--------- Face Athe File connection-------------                
                #import face_authe
                #face_authe.Test_database()
            else:
                ms.showerror("Invalid OTP", "Invalid OTP. Please try again.")
        else:
            ms.showwarning("Warning", "Please enter the OTP.")
           #         from subprocess import call
           #         call(["python", "face_authe.py"])  
            #     else:
          #         messagebox.showerror("Invalid OTP", "Invalid OTP. Please try again.")
            # else:
            #     messagebox.showwarning("Warning", "Please enter the OTP.")
                

        
        
        
        
        
        
        

    # ====== Email ====================
    email_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry.place(x=40, y=30, width=256, height=34)
    email_entry.config(highlightbackground="black", highlightcolor="black")
    email_label = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    email_label.place(x=40, y=0)
    
    
    
    submit_button = tk.Button(win, fg='#f8f8f8', text='Submit', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2',command=lambda: send_otp())
    submit_button.place(x=320, y=30, width=256, height=34)
    
    otp_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2, show='*')
    otp_entry.place(x=40, y=130, width=256, height=34)
    otp_entry.config(highlightbackground="black", highlightcolor="black")
    otp_label = Label(win, text='• Enter OTP', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    otp_label.place(x=40, y=100)
    
    
    def show_password():
        if otp_entry.cget('show')=='*':
            otp_entry.config(show='')
        else:
            otp_entry.config(show='*')
        
        
    check_button=Checkbutton(win, text="Show OTP",font=("yu gothic ui", 8, "bold underline"),bg='white', command=show_password)
    check_button.place(x=40, y=170)
    
    
    
    submit_button = tk.Button(win, fg='#f8f8f8', text='Submit', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2',command=lambda: verify())
    submit_button.place(x=320, y=130, width=256, height=34)
    
    

    # ====  New Password ==================
    
                
                
    def update_pass():
        win2 = Toplevel()
        window_width = 350
        window_height = 400
        screen_width = win2.winfo_screenwidth()
        screen_height = win2.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win2.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        win2.title('Forgot Password')
        win2.iconbitmap('vi.ico')
        win2.configure(background='#f8f8f8')
        win2.resizable(0, 0)
        
        
        
        new_password_entry = Entry(win2, fg="#a7a7a7", show='*', font=("yu gothic ui semibold", 12), highlightthickness=2)
        new_password_entry.place(x=40, y=30, width=256, height=34)
        new_password_entry.config(highlightbackground="black", highlightcolor="black")
        new_password_label = Label(win2, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        new_password_label.place(x=40, y=0)
        
        def show_password():
            if new_password_entry.cget('show')=='*':
                new_password_entry.config(show='')
            else:
                new_password_entry.config(show='*')
            
            
        check_button=Checkbutton(win2, text="Show Password",font=("yu gothic ui", 8, "bold underline"),bg='white', command=show_password)
        check_button.place(x=40, y=70)

        # ====  Confirm Password ==================
        confirm_password_entry = Entry(win2, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2, show='*')
        confirm_password_entry.place(x=40, y=140, width=256, height=34)
        confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
        confirm_password_label = Label(win2, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                       font=("yu gothic ui", 11, 'bold'))
        confirm_password_label.place(x=40, y=110)
        
        def show_password():
            if confirm_password_entry.cget('show')=='*':
                confirm_password_entry.config(show='')
            else:
                confirm_password_entry.config(show='*')
            
            
        check_button=Checkbutton(win2, text="Show Password",font=("yu gothic ui", 8, "bold underline"),bg='white', command=show_password)
        check_button.place(x=40, y=180)

        # ======= Update password Button ============
        update_pass = tk.Button(win2, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                             cursor='hand2', activebackground='#1b87d2', command=lambda: change_password())
        update_pass.place(x=40, y=250, width=256, height=50)
        
        
        def exit_window():
            win2.destroy()
            win.destroy()
            
        
        #DATABASE connection############################
        
        def change_password():
            if email_entry.get() == "" or new_password_entry.get() == "":
                ms.showerror("Error", "All fields are required" )
                exit_window()
                
            else:
                db = sqlite3.connect('evaluation.db')
                cursor = db.cursor()
                query = 'select * from user_reg where Email_id =?'
                cursor.execute(query, [(email_entry.get())])
                row = cursor.fetchone()
                if row == None :
                    ms.showerror("Error", "Email does not exist")
                    exit_window()
                    
                else :
                    query = '''update user_reg set Password=? where Email_id=?'''
                    cursor.execute(query,  [new_password_entry.get(), email_entry.get(),])
                    db.commit()
                    db.close()
                    ms.showinfo("Congrats","Password changed successfully")
                    exit_window()

forgotPassword = Button(Login_frame, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='aquamarine4',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=360, y=212)




        
logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=10)
        
lbluser=tk.Label(Login_frame,text="Voter_ID",image=user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=30,pady=5)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=voter_id,font=("",15))
txtuser.grid(row=1,column=1,padx=10)
        
lblpass=tk.Label(Login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=30,pady=5)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=10)

def show_password():
    if txtpass.cget('show')=='*':
        txtpass.config(show='')
    else:
        txtpass.config(show='*')
    
    
check_button=Checkbutton(root, text="Show Password",font=("yu gothic ui", 8, "bold underline"),bg='aquamarine4', command=show_password)
check_button.place(x=800, y=500)
        





btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="brown",fg="white")
btn_log.grid(row=3,column=1,pady=40)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="black",fg="white")
btn_reg.grid(row=3,column=0,pady=40)
        
####################################################################################################forgot


                    


       
        # Login Function

root.mainloop()