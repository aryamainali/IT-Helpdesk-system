import tkinter as tk
from tkinter import Button,Label,Entry,messagebox
import pymysql,hashlib
# database connection


connection = pymysql.connect(
                                host='localhost',
                                user='admin',
                                password='$$$$$$$$$$',
                                database='helpdesk_system'
)
cur=connection.cursor()
cur.execute("SELECT * FROM USERS")
data = cur.fetchall()


def Login(page,login): 
    l1=Label(page,text="login page")
    l1.pack()
    
    
    l2 =Label(page,text="User Name")
    l2.place(x=60,y=60)    
    e1 =Entry(page)
    e1.place(x=140,y=60)
    
    l3 =Label(page,text="Password")
    l3.place(x=60,y=90)    
    e2 =Entry(page,show="*")
    e2.place(x=140,y=90)
    
    import hashlib

    # def Login_to_helpdesk():
    #     username = e1.get()
    #     password = e2.get()

    #     cur = connection.cursor()
    #     cur.execute("SELECT * FROM USERS WHERE LOWER(USERNAME) = %s", (username.lower(),))
    #     result = cur.fetchone()

    #     if result is not None:
    #         db_username = result[0]
    #         db_password = result[1]

    #         hashed_password = hashlib.sha256(password.encode()).hexdigest()

    #         if db_password == hashed_password:
    #             messagebox.showinfo("Success", "Successfully logged in")
    #             if db_username.lower() == "customer":
    #                 login(3)
    #             elif db_username.lower() == "operator":
    #                 login(2)
    #         else:
    #             messagebox.showerror("Error", "Invalid password")
    #     else:
    #         messagebox.showerror(" Access Denied", "Invalid user")

    #     # Clear the entry fields
    #     e1.delete(0, 'end')
    #     e2.delete(0, 'end')


    # login_button = Button(page, text="Login", command=Login_to_helpdesk)
    # login_button.place(x=330, y=140)

    login_button = Button(page, text="Login",command=login)
    login_button.place(x=330, y=140)


    
