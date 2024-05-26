# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:37:36 2021

@author: sheet
"""
import streamlit as st
import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np
import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.geometry("%dx%d+0+0"%(w,h))
img = Image.open("D:/Voting System/e-voting updated/vi.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
root.title("GUI")


#------------------Frame----------------------
image2 =Image.open('img9.jpg')
image2 =image2.resize((w,h)) #######################################################################################

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "face_registartion.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "admin_login.py"])   
    


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image



lbl = tk.Label(root, text="Smart Online Voting System", font=('times', 40,' bold '), height=1, width=50,bg="black",fg="white")
lbl.place(x=0, y=5)

framed = tk.LabelFrame(root, text="", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="cadetblue4")########################
framed.grid(row=0, column=0, sticky='nw')#############################################################################
framed.place(x=500, y=300)##############################################################################################################
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Admin',width=15,height=3,bg='dark blue',fg='white',command=login,font='bold').place(x=70,y=70)
button1 = tk.Button(framed, text='User',width=17,height=3,bg='dark blue',fg='white',command=reg,font='bold').place(x=250,y=70)


root.mainloop()
