import tkinter as tk
from tkinter import Frame,messagebox
from Login_page import Login
from It_Help_desk import It_Help_desk
from customer_helpdesk import customer_help_desk
mainwindow = tk.Tk()
mainwindow.rowconfigure(0,weight=1)
mainwindow.columnconfigure(0,weight=1)


page1=Frame(mainwindow)
page2=Frame(mainwindow)
page3=Frame(mainwindow)

page1.configure(bg='MediumAquamarine')
page3.configure(bg='sky blue')



for frame in (page1,page2,page3):
    frame.grid(row=0,column=0,sticky='nsew')
    
    
def login(): 
    page2.tkraise()

# def login(page_num):
#     if page_num == 2:
#         page2.tkraise()
#     else:
#         page3.tkraise()
        
def logout():
    page1.tkraise()
    
def go_to_customer_help_desk():
    page3.tkraise()
    

Login(page1,login)
It_Help_desk(page2,logout,go_to_customer_help_desk)
customer_help_desk(page3,logout)


page1.tkraise()
mainwindow.title('Helpdesk')
mainwindow.geometry('1000x700')
mainwindow.resizable(True,True)
mainwindow.mainloop()
