# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:33:41 2022

@author: Beautiful Mishika
"""

from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Private Variable Login Page")

label_name = Label(root, text="Name : ")
label_name.place(relx=0.3, rely=0.1, anchor=CENTER)

input_name =  Entry(root)
input_name.place(relx=0.6, rely=0.1, anchor=CENTER)

label_pwd = Label(root, text="Password : ")
label_pwd.place(relx=0.3, rely=0.2, anchor=CENTER)

input_pwd = Entry(root)
input_pwd.place(relx=0.6, rely=0.2, anchor=CENTER)


label_captcha = (root, text="Captcha : ")
label_pwd.place(relx=0.3, rely=0.3, anchor=CENTER)

input_captcha = Entry(root)
input_captcha.place(relx=0.6, rely=0.3, anchor=CENTER)

label_showname = Label(root)
label_showname.place(relx=0.5, rely=0.7, anchor=CENTER)


label_showpwd = Label(root)
label_showpwd.place(relx=0.5, rely=0.8, anchor=CENTER)


label_showcaptcha = Label(root)
label_showcaptcha.place(relx=0.5, rely=0.9, anchor=CENTER)


class userDB():
     def __init__(self):
         self.__username = "James"
         self.__pwd ="James76*"
         self.captcha = "A7d"
         
    def showUser():
        label_show_name["text"] = "Name : " + self.__username
        label_showpwd["text"] = "Password : " + self.__pwd
        label_showcaptcha["text"] = "Captcha : " + self.captcha
user = userDB()
def addUser():
    global user
    user.username = input_name.get()
    user.password= input_pwd.get()
    user.captcha = input_captcha.get()
    print("Details Updated")
    
btn = Button(root, text="Update Login Details", command=addUser)
btn.place(relx=0.3, rely=0.5, anchor=CENTER)
btn = Button(root, text="Show Profile", command=user.showUser)
btn.place(relx=0.7, rely=0.5, anchor=CENTER)
root.mainloop()