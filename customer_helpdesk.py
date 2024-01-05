import tkinter as tk
from tkinter import Button,Label,Entry,messagebox,Frame,ttk,Listbox
import pymysql
from datetime import datetime
connection = pymysql.connect(
                                host='localhost',
                                user='root',
                                password='$$$$$$$$$$$$$',
                                database='helpdesk_system'
)
cur = connection.cursor()
cur.execute("SELECT * FROM problem_resolution")
data = cur.fetchall()


def customer_help_desk(page,logout):
    l1=Label(page,text="customer page")
    l1.pack()
    
    style = ttk.Style()
    style.configure("CustomTab.TFrame", background="sky blue", fieldbackground="sky blue")
    
    lb1=Listbox(page)
    lb1.config(bg="grey",width=150,height=20)
    lb1.place(x=30,y=42)
    
    def issue_status():
        try:
            # Fetch problem numbers and caller names from call_log
            cur.execute("SELECT DISTINCT call_log.problem_number, call_log.caller_name "
                        "FROM call_log JOIN problem_resolution ON call_log.call_id = problem_resolution.call_id")
            resolutions_with_caller = cur.fetchall()

            if not resolutions_with_caller:
                messagebox.showinfo("Info", "No issues found in the database.")
                return

            lb1.delete(0, tk.END)

            for problem_num, caller_name in resolutions_with_caller:
                # Fetch data from the problem_resolution table for the current problem number
                cur.execute("SELECT call_id, resolution_time, resolution_description, resolution_duration "
                            "FROM problem_resolution WHERE call_id = %s ORDER BY call_id ASC", (problem_num,))
                resolutions = cur.fetchall()

                if not resolutions:
                    continue  # Skip if no resolution found for this problem number

                for resolution_data in resolutions:
                    call_id = resolution_data[0]
                    resolution_time = resolution_data[1]
                    resolution_description = resolution_data[2]
                    resolution_duration = resolution_data[3]

                    lb1.insert(tk.END, f"Caller Name: {caller_name}")
                    lb1.insert(tk.END, f"Problem Number: {problem_num}")
                    lb1.insert(tk.END, f"Call ID: {call_id}")
                    lb1.insert(tk.END, f"Resolution time: {resolution_time}")
                    lb1.insert(tk.END, f"Resolution Description: {resolution_description}")
                    lb1.insert(tk.END, f"Resolution Duration: {resolution_duration}")
                    lb1.insert(tk.END, "")

        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))
            
    
    b0=Button(page,text="logout",command=logout)
    b0.place(x=630, y=390)
    
    b1=Button(page,text="see your issue status",command=issue_status)
    b1.place(x=90,y=390)