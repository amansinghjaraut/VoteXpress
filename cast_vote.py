import streamlit as st
import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  
from tkinter import messagebox as ms

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Vote Panel")
#------------------Frame----------------------

#Fulllname = tk.StringVar()
vote = tk.IntVar()
id = tk.IntVar()

# def login():
    
# ##### tkinter window ######
    
#     print("log")
#     from subprocess import call
#     call(["python", "Login1.py"])   
    


# #++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
image2 =Image.open('img12.jpg')
#image2 =image2.resize((w,h), Image.ANTIALIAS)
image2 = image2.resize((1630, 900))


background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


# Python program to convert a list to string
    
# Function to convert  
import functools
import operator
 
 
def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str
 
 
# Driver code
# tuple = ('g', 'e', 'e', 'k', 's')
# str = convertTuple(tuple)
# print(str)
 
# # Driver code
# str = convertTuple(tuple)
# print(str)

def cast_vote():
    
    #fname = Fulllname.get()
    vote1 = vote.get()
    
    f1 = open("id.txt","r")
    id = f1.read()
    print(id)
    f1.close()
    
    with sqlite3.connect('upload_cad.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM cast_vote WHERE id = ?')
    c.execute(find_user, [(id)])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    
    # if (fname.() or (fname == "")):
    #     ms.showinfo("Message", "please enter valid name")
    if (c.fetchall()):
        ms.showerror('Error!', 'You Already Voted')
  
    
    else:
        conn = sqlite3.connect('upload_cad.db')
        with conn:
             cursor = conn.cursor()
             cursor.execute('INSERT INTO cast_vote(id, vote) VALUES(?,?)',
                    (id, vote1))
             if vote1 == 1:
                find_user = ('SELECT Count FROM count WHERE Party = 1')
                print(find_user)
                c.execute(find_user)
                s = c.fetchall()
                print(s)
                print(type(s))
                a = s[0]
                print(a)
                #print(listToString(s))
                str1 = convertTuple(a)
                print(str1)
                 
                str2 = str1+1
                print(str2)
               # str2 = print(int(str2))
               # conn = sqlite3.connect('upload_cad.db')
                with conn:
                     cursor = conn.cursor()
                     cursor.execute("""UPDATE  count SET Count= '{0}' WHERE Party = 1 """.format(str2))
                     
                     conn.commit()
                     cursor.close()
                     db.close()
                     
             elif vote1 == 2:
                   find_user = ('SELECT Count FROM count WHERE Party = 2')
                   print(find_user)
                   c.execute(find_user)
                   s = c.fetchall()
                   print(s)
                   print(type(s))
                   a = s[0]
                   print(a)
                   #print(listToString(s))
                   str1 = convertTuple(a)
                   print(str1)
                    
                   str2 = str1+1
                   print(str2)
                  # str2 = print(int(str2))
                  # conn = sqlite3.connect('upload_cad.db')
                   with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE  count SET Count= '{0}' WHERE Party = 2 """.format(str2))
                        
                        conn.commit()
                        cursor.close()
                        db.close()
             elif vote1 == 3:
                      find_user = ('SELECT Count FROM count WHERE Party = 3')
                      print(find_user)
                      c.execute(find_user)
                      s = c.fetchall()
                      print(s)
                      print(type(s))
                      a = s[0]
                      print(a)
                      #print(listToString(s))
                      str1 = convertTuple(a)
                      print(str1)
                       
                      str2 = str1+1
                      print(str2)
                     # str2 = print(int(str2))
                     # conn = sqlite3.connect('upload_cad.db')
                      with conn:
                           cursor = conn.cursor()
                           cursor.execute("""UPDATE  count SET Count= '{0}' WHERE Party = 3 """.format(str2))
                           
                           conn.commit()
                           cursor.close()
                           db.close()
             elif vote1 == 4:
                         find_user = ('SELECT Count FROM count WHERE Party = 4')
                         print(find_user)
                         c.execute(find_user)
                         s = c.fetchall()
                         print(s)
                         print(type(s))
                         a = s[0]
                         print(a)
                         #print(listToString(s))
                         str1 = convertTuple(a)
                         print(str1)
                          
                         str2 = str1+1
                         print(str2)
                        # str2 = print(int(str2))
                        # conn = sqlite3.connect('upload_cad.db')
                         with conn:
                              cursor = conn.cursor()
                              cursor.execute("""UPDATE  count SET Count= '{0}' WHERE Party = 4 """.format(str2))
                              
                              conn.commit()
                              cursor.close()
                              db.close()
             elif vote1 == 5:
                         find_user = ('SELECT Count FROM count WHERE Party = 5')
                         print(find_user)
                         c.execute(find_user)
                         s = c.fetchall()
                         print(s)
                         print(type(s))
                         a = s[0]
                         print(a)
                         #print(listToString(s))
                         str1 = convertTuple(a)
                         print(str1)
                          
                         str2 = str1+1
                         print(str2)
                        # str2 = print(int(str2))
                        # conn = sqlite3.connect('upload_cad.db')
                         with conn:
                              cursor = conn.cursor()
                              cursor.execute("""UPDATE  count SET Count= '{0}' WHERE Party = 5 """.format(str2))
                              
                              conn.commit()
                              cursor.close()
                              db.close()
             
                
             
    
             conn.commit()
             db.close()
             ms.showinfo('Success!', 'Vote submit Successfully !')
                # window.destroy()
            

lbl = tk.Label(root, text="Cast Vote", font=('times', 35,' bold '), height=1, width=30,bg="black",fg="white")
lbl.place(x=300, y=5)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=20, y=100)
#++++++++++++++++++++++++++++++++++++++++++++

# l7 = tk.Label(root, text="AAP :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="BJP :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="CONG :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="NOTA :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)

# l7 = tk.Label(root, text="SS :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l7.place(x=130, y=350)
# # gender
image1 = Image.open('img/aap.png')
image1 = image1.resize((100, 100))

image_lab1 = ImageTk.PhotoImage(image1)

img_lb = tk.Label(root, image=image_lab1)

img_lb.image = image_lab1

img_lb.place(x=450, y=120)  # , relwidth=1, relheight=1)

tk.Radiobutton(root, text="AAP", padx=5, width=5, bg="snow", font=("bold", 15),variable=vote,value=1).place(x=650,y=150)


image2 = Image.open('img/bjp.png')
image2 = image2.resize((100, 100))

image_lab2 = ImageTk.PhotoImage(image2)

img_lb1 = tk.Label(root, image=image_lab2)

img_lb1.image = image_lab2

img_lb1.place(x=450, y=250)  

tk.Radiobutton(root, text="BJP", padx=5, width=4, bg="snow", font=("bold", 15),variable=vote,value=2).place(x=650, y=280)

image3 = Image.open('img/cong.jpg')
image3 = image3.resize((100, 100))

image_lab3 = ImageTk.PhotoImage(image3)

img_lb2 = tk.Label(root, image=image_lab3)

img_lb2.image = image_lab3

img_lb2.place(x=450, y=380) 

tk.Radiobutton(root, text="CONG", padx=5, width=5, bg="snow", font=("bold", 15),variable=vote,value=3).place(x=650,y=410)




image4 = Image.open('img/ss.png')
image4 = image4.resize((100, 100))

image_lab4 = ImageTk.PhotoImage(image4)

img_lb3 = tk.Label(root, image=image_lab4)

img_lb3.image = image_lab4

img_lb3.place(x=450, y=500) 

tk.Radiobutton(root, text="SIV", padx=5, width=5, bg="snow", font=("bold", 15),variable=vote,value=4).place(x=650,y=530)





image5 = Image.open('img/nota.jpg')
image5 = image5.resize((100, 100))

image_lab5 = ImageTk.PhotoImage(image5)

img_lb4 = tk.Label(root, image=image_lab5)

img_lb4.image = image_lab2

img_lb4.place(x=450, y=630) 

tk.Radiobutton(root, text="Nota", padx=5, width=5, bg="snow", font=("bold", 15),variable=vote,value=5).place(x=650,y=670)




btn = tk.Button(root, text="Submit", bg="red",font=("",20, "bold"),fg="white", command = cast_vote,width=9, height=1)
btn.place(x=1030, y=550)

def logout():
    root.destroy()
    
btn = tk.Button(root, text="Logout", bg="red",font=("",20, "bold"),fg="white", command = logout,width=9, height=1)
btn.place(x=1030, y=650)



#####For background Image
# button1 = tk.Button(framed, text='Login Now',width=15,height=3,bg='dark blue',fg='white',command=login,font='bold').place(x=20,y=35)
# button1 = tk.Button(framed, text='Register',width=17,height=3,bg='dark blue',fg='white',command=reg,font='bold').place(x=250,y=35)


root.mainloop()
