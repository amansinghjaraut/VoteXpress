import streamlit as st
from tkinter import *
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox 
import random
import smtplib
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
    
 ##############################################+=============================================================
    
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
    
    
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
img = Image.open("vi.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
root.title("Smart Voting System")
    
num = tk.StringVar()
otp = tk.StringVar()

image2 =Image.open('img1.jpg')
image2 =image2.resize((w,h))

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

lbl = tk.Label(root, text="Smart Voting System", font=('times', 30,' bold '), height=1, width=65,bg="black",fg="white")
lbl.place(x=0, y=5)

    # frame_alpr = tk.LabelFrame(root, text="", width=280, height=300, bd=5, font=('times', 15, ' bold '),bg="seashell4")
    # frame_alpr.grid(row=0, column=0, sticky='nw')
    # frame_alpr.place(x=600, y=250)

    # Function to generate OTP
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
        messagebox.showinfo("OTP Sent", "OTP sent successfully!")
        return otp
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send OTP. Error: {e}")
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
        messagebox.showwarning("Warning", "Please enter an email address.")
   # Function to handle OTP verification
def verify():
    user_input = otp_entry.get()
    if user_input:
        if verify_otp(user_input, otp):
            messagebox.showinfo("OTP Verified", "OTP verification successful!")

##############--------- Face Athe File connection-------------                
            import face_authe
            face_authe.Test_database()
        else:
            messagebox.showerror("Invalid OTP", "Invalid OTP. Please try again.")
    else:
        messagebox.showwarning("Warning", "Please enter the OTP.")
       #         from subprocess import call
       #         call(["python", "face_authe.py"])  
        #     else:
      #         messagebox.showerror("Invalid OTP", "Invalid OTP. Please try again.")
        # else:
        #     messagebox.showwarning("Warning", "Please enter the OTP.")
            
def vote():
    global email_entry, otp_entry
    frame_display = tk.LabelFrame(root, text=" ---- ", width=600, height=400, bd=5, font=('times', 14, ' bold '),bg="#736AFF")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=450, y=100)
        
    l2 = tk.Label(frame_display, text="OTP Authentication", width=20, font=("Times new roman", 15, "bold"),bd=5, fg="black")
    l2.place(x=150, y=40)
        
    l2 = tk.Label(frame_display, text="Enter Email id", width=20, font=("Times new roman", 15, "bold"),bd=5, fg="black")
    l2.place(x=30, y=100)
    email_entry = tk.Entry(frame_display, textvar=num,width=20, font=('', 15))
    email_entry.place(x=300, y=100)
       
    button2 = tk.Button(frame_display, text="Submit ",command=send_otp, width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
    button2.place(x=200, y=170)

    l2 = tk.Label(frame_display, text="Enter OTP", width=20, font=("Times new roman", 15, "bold"),bd=5, fg="black")
    l2.place(x=30, y=240)
    otp_entry = tk.Entry(frame_display,textvar=otp, width=20, font=('', 15), show='*')
    otp_entry.place(x=300, y=240)
    
    def show_otp():
        if otp_entry.cget('show')=='*':
            otp_entry.config(show='')
        else:
            otp_entry.config(show='*')
        
        
    check_button=Checkbutton(root, text="Show OTP" ,bg="#736AFF", font=("yu gothic ui", 8, "bold underline"), command=show_otp)
    check_button.place(x=760, y=400)

    button3 = tk.Button(frame_display, text="Submit OTP",command=verify, width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
    button3.place(x=200, y=320)
        
        
    def ID(): 
        frame_display = tk.LabelFrame(root, text=" ---- ", width=600, height=400, bd=5, font=('times', 14, ' bold '),bg="#736AFF")
        frame_display.grid(row=0, column=0, sticky='nw')
        frame_display.place(x=450, y=100)
        my_conn = sqlite3.connect('upload_cad.db')
        r_set=my_conn.execute("SELECT * FROM count")
        i=1 # row value inside the loop 
        for student in r_set: 
            for j in range(len(student)):
                    
                e=tk.Label(frame_display,width=50,text='Party',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                e.grid(row=0,column=0)
                e=tk.Label(frame_display,width=50,text='Count',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
                e.grid(row=0,column=1)
                e = tk.Label(frame_display,text=student[j], width=50, fg='blue',borderwidth=2, relief='ridge', anchor="w") 
                e.grid(row=i, column=j)
                    #i=1

                   # e.insert(END, student[j])
            i=i+1

def window():
    root.destroy()

button2 = tk.Button(root, text="Email-Verification",command = vote, width=20, height=2, font=('times', 15, ' bold '),bg="orange",fg="white")
button2.place(x=50, y=150)

exit = tk.Button(root, text="Exit", command=window, width=20, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=50, y=250)

root.mainloop()
