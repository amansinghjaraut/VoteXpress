import streamlit as st
from tkinter import *
import tkinter as tk
#from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Registration Form")
#root.resizable(False,False)
# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('im1.jpg')
image2 = image2.resize((w,h))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Registration Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="black", fg="white", width=67, height=2)
# label_l2.place(x=0, y=90)


frame_alpr = tk.LabelFrame(root, text="", width=600, height=650, bd=5, font=('times', 14, ' bold '),fg="black",bg="cadetblue3")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=500, y=50, width=700, height=700)

######################### Registration form #####################################################################

Fulllname = tk.StringVar()
adhar_card = tk.IntVar()
Voter_ID = tk.StringVar()
Password = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.StringVar()
# age = tk.IntVar()
Email = tk.StringVar()
#password1 = tk.StringVar()



# # database code
# db = sqlite3.connect('evaluation.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS registration"
#                "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT, password TEXT)")
# db.commit()

def login():
    from subprocess import call
    call(["python","login.py"])
    root.destroy()

def password_check(pass1): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(pass1) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(pass1) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in pass1): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in pass1): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in pass1): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in pass1): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fulllname.get()
    addr = adhar_card.get()
    un = Voter_ID.get()
    pass1 = Password.get()
    mobile = Phoneno.get()
    Status = "Voter"
    # time = age.get()
    email = Email.get()
    #cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM user_reg WHERE Voter_ID = ?')
    c.execute(find_user, [(Voter_ID.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter AdharNO")
        
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pass1 == ""):
        ms.showinfo("Message", "Please Enter valid password")
    # elif (var == False):
    #     ms.showinfo("Message", "Please Enter gender")
    elif(pass1=="")or(password_check(pass1))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    # elif (pwd != cnpwd):
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    # elif ((time > 100) or (time == 0)):
    #     ms.showinfo("Message", "Please Enter valid age")
   
    #     ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO user_reg(Fullname, Adhar_No, Voter_ID, Password, Phone_No, Email_id, status) VALUES(?,?,?,?,?,?,?)',
                (fname, addr, un, pass1, mobile, email,Status))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            



l1 = tk.Label(root, text="Registration Form", font=("Times new roman", 30, "bold"), bg="Black", fg="white")
l1.place(x=700, y=50)

# that is for label1 registration

l2 = tk.Label(root, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l2.place(x=600, y=150)
t1 = tk.Entry(root, textvar=Fulllname, width=20, font=('', 15))
t1.place(x=800, y=150)
# that is for label 2 (full name)


l3 = tk.Label(root, text="Aadhar_Card No :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l3.place(x=600, y=200)
t2 = tk.Entry(root, textvar=adhar_card, width=20, font=('', 15),show='*' )
t2.place(x=800, y=200)

def show_aadhar():
    if t2.cget('show')=='*':
        t2.config(show='')
    else:
        t2.config(show='*')
    
    
check_button1=Checkbutton(root, text="Show Aadhar" ,font= ('',8,"bold underline"), command=show_aadhar, bg="cadetblue3")
check_button1.place(x=1050, y=200)

l5 = tk.Label(root, text="Voter_ID :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l5.place(x=600, y=250)
t4 = tk.Entry(root, textvar=Voter_ID, width=20, font=('', 15))
t4.place(x=800, y=250)
# # that is for email address

l6 = tk.Label(root, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l6.place(x=600, y=300)
t5 = tk.Entry(root, textvar=Password, width=20, font=('', 15), show='*')
t5.place(x=800, y=300)

def show_password():
    if t5.cget('show')=='*':
        t5.config(show='')
    else:
        t5.config(show='*')
    
    
check_button=Checkbutton(root, text="Show Password" ,font= ('',8,"bold underline"), command=show_password, bg="cadetblue3")
check_button.place(x=1050, y=300)

# # # phone number
l7 = tk.Label(root, text="Phone_No :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l7.place(x=600, y=350)
t6 = tk.Entry(root, textvar=Phoneno, width=20, font=('', 15))
t6.place(x=800, y=350)

l8 = tk.Label(root, text="Email :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l8.place(x=600, y=400)
t6 = tk.Entry(root, textvar=Email, width=20, font=('', 15))
t6.place(x=800, y=400)


'''
l7 = tk.Label(root, text="Status :", width=12, font=("Times new roman", 15, "bold"), bg="cadetblue3")
l7.place(x=600, y=450)
# gender
tk.Radiobutton(root, text="Voter", padx=5, width=5, bg="cadetblue3", font=("bold", 15), variable=var, value="Voter").place(x=800,
                                                                                                                y=450)
tk.Radiobutton(root, text="Candidate", padx=20, width=4, bg="cadetblue3", font=("bold", 15), variable=var, value="Candidate").place(
    x=910, y=450)
'''
#var="Voter"


# l9 = tk.Label(window, text="Satate :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l9.place(x=130, y=500)
# t9 = tk.Entry(window, textvar=carno, width=20, font=('', 15), show="*")
# t9.place(x=330, y=500)

def Create_database():
            
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        cap = cv2.VideoCapture(0)
        
    #    id = input('enter user id')
        id=entry2.get()
        
        sampleN=0;
        
        while 1:
        
            ret, img = cap.read()
        
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
            for (x,y,w,h) in faces:
        
                sampleN=sampleN+1;
        
                cv2.imwrite("faceData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                cv2.waitKey(100)
        
            cv2.imshow('img',img)
        
            cv2.waitKey(1)
        
            if sampleN > 69:
        
                break
        
        cap.release()
        entry2.delete(0,'end')
        cv2.destroyAllWindows()
        root.destroy()
        from subprocess import call
        call(["python", "train.py"])
 
    

            

button1 = tk.Button(root, text="Create Face Data", command=Create_database,width=15, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button1.place(x=600, y=600)
    
entry2=tk.Entry(root,bd=4,width=9)
entry2.place(x=800, y=610)
btn = tk.Button(root, text="Register", bg="red",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=800, y=500)
btn = tk.Button(root, text="Login", bg="red",font=("",20),fg="white", width=9, height=1, command=login)
btn.place(x=960, y=500)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
root.mainloop()