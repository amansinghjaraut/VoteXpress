import streamlit as st
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:37:36 2021

@author: sheet
"""

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
root.title("GUI")
#------------------Frame----------------------
image2 =Image.open('im.jpg')
image2 = image2.resize((1630, 1200))
#image2 =image2.resize((w,h), Image.ANTIALIAS)

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
    call(["python", "add_cand.py."])   
    
def ID(): 
     frame_display = tk.LabelFrame(root, text="", width=600, height=400, bd=5, font=('times', 14, ' bold '),bg="#736AFF")
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
         
                 

#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image



lbl = tk.Label(root, text="Smart Online Voting System", font=('times', 40,' bold '), height=1, width=50,bg="black",fg="white")
lbl.place(x=0, y=5)

framed = tk.LabelFrame(root, text="", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="cadetblue4")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=500, y=300)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='View Result',width=15,height=3,bg='dark blue',fg='white',command=ID,font='bold').place(x=70,y=50)
button2 = tk.Button(framed, text='add Candidate',width=17,height=3,bg='dark blue',fg='white',command=login,font='bold').place(x=250,y=50)
#button3 = tk.Button(framed, text='Fingerprint',width=15,height=3,bg='dark blue',fg='white',command=fingerprint,font='bold').place(x=180,y=150)

root.mainloop()
