import tkinter as tk,re
from tkinter import Button,Label,ttk,Entry,Listbox,messagebox,Text,Checkbutton
import pymysql.cursors
from datetime import datetime



# database connection
connection = pymysql.connect(
                                host='localhost',
                                user='root',
                                password='$$$$$$$$$$',
                                database='helpdesk_system'
)

cur = connection.cursor()
cur.execute("SELECT * FROM call_log")
cur.execute("SELECT * FROM personnel")
cur.execute("SELECT * FROM equipment")
cur.execute("SELECT * FROM software_license")
cur.execute("SELECT * FROM problem_types")
cur.execute("SELECT * FROM PreviousProblems")
cur.execute("SELECT * FROM RelatedProblems")
cur.execute("SELECT * FROM problem_resolution")
cur.execute("SELECT * FROM SpecialistAllocation")
cur.execute("SELECT * FROM Training")
data = cur.fetchall()


def It_Help_desk (page, logout,go_to_customer_help_desk):
    # styling the tabs
    style = ttk.Style()
    style.configure("CustomTab.TFrame", background="sky blue", fieldbackground="sky blue")
    
    l1=Label(page,text="It_Help_desk page")
    l1.pack()
    # Create tabs within the dashboard table and styling
    tab = ttk.Notebook(page)
    tab1 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab2 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab3 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab4 = ttk.Frame(tab, style="CustomTab.TFrame")
    tab5 = ttk.Frame(tab, style="CustomTab.TFrame")

    # Assign names to the tab tables
    tab.add(tab1, text='User_Information')
    tab.add(tab2, text='Problem_Report')
    tab.add(tab3, text='Assign_Issue')
    tab.add(tab4, text='Problem_Feedback')
    tab.add(tab5, text='Agent_Training')
    tab.pack(expand=1, fill='both')
    
    
    
    # confuguring tabs
    l0 = Label(tab1,text="User_Check")
    l0.config(bg="light green")
    l0.place(x=160,y=10)
    
    l2=Label(tab1,text="personnel_name")
    l2.config(bg="pink")
    l2.place(x=30,y=60)
    e1=Entry(tab1)
    e1.place(x=130,y=60)
    
    
    l3=Label(tab1,text="department")
    l3.config(bg="pink")
    l3.place(x=30,y=100)
    e2=Entry(tab1)
    e2.place(x=130,y=100)
    
    
    l4=Label(tab1,text="personnel_email")
    l4.config(bg="pink")
    l4.place(x=30,y=140)
    e3=Entry(tab1)
    e3.place(x=130,y=140)
    
    l5=Label(tab1,text="job_title")
    l5.config(bg="pink")
    l5.place(x=30,y=180)
    e4=Entry(tab1)
    e4.place(x=130,y=180)
    
    
    # ------------------------------------------------------------------------------



    l6=Label(tab1,text="Record_Log")
    l6.config(bg="light green",padx=3,pady=5)
    l6.place(x=420,y=10)
    
    l7=Label(tab1,text="Caller_Name")
    l7.config(bg="pink")
    l7.place(x=310,y=60)
    e5=Entry(tab1)
    e5.place(x=460,y=60)
    
    l8=Label(tab1,text="Operator_Name")
    l8.config(bg="pink")
    l8.place(x=310,y=100)
    e6=Entry(tab1)
    e6.place(x=460,y=100)
    
    l9=Label(tab1,text="Computer_Serial_Number")
    l9.config(bg="pink")
    l9.place(x=310,y=140)
    e7=Entry(tab1)
    e7.place(x=460,y=140)
    
    l10=Label(tab1,text="Operating_System")
    l10.config(bg="pink")
    l10.place(x=310,y=180)
    e8=Entry(tab1)
    e8.place(x=460,y=180)
    
    l11=Label(tab1,text="software")
    l11.config(bg="pink")
    l11.place(x=310,y=220)
    e9=Entry(tab1)
    e9.place(x=460,y=220)
    
    
    l12=Label(tab1,text="problem_description")
    l12.config(bg="pink")
    l12.place(x=310,y=260)
    e10=Entry(tab1)
    e10.place(x=460,y=260)
    
    

#  this id should be extracted from problem table
    l16=Label(tab1,text="problem_type_name")
    l16.config(bg="pink")
    l16.place(x=310,y=300)
    e14=Entry(tab1)
    e14.place(x=460,y=300)
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    e4.delete(0,'end')
    
    # -----------------------
    lb=Listbox(tab1)
    lb.config(bg="grey")
    lb.place(x=660,y=30)
    lb.config(height=30,width=50)
    # --------------------------------------------------


    def onCheck():
        cur = connection.cursor()
        cur.execute("SELECT * FROM personnel WHERE personnel_name = %s AND personnel_email= %s",(e1.get(),e3.get()))
        existing_user = cur.fetchone()
        if not existing_user:
            messagebox.showerror("Invalid request","User with this email doesnot exists in the database.")
        else:    
            lb.insert(tk.END, existing_user)           
            messagebox.showinfo("Entry Found", "user with this email exixt in database.")
           
    global_problem_type_id = None
    global_problem_type_name = None
    current_call_id = None
    cur = None
        
   # Global variables to store the problem type details
    # Global variables to store the problem type details
    global_problem_type_id = None
    global_problem_type_name = None
    current_call_id = None
    cur = None

    def log_new_call():
        global cur, current_call_id, global_problem_type_name, global_problem_type_id
        try:
            call_time = datetime.now()
            cur = connection.cursor()
            problem_type_name = e14.get()
            global_problem_type_name = problem_type_name  # Store the problem type name globally

            # Retrieve personnel_id for the operator
            cur.execute("SELECT personnel_id FROM personnel WHERE personnel_email = %s", (e3.get(),))
            personnel_id_row = cur.fetchone()
            if personnel_id_row is not None:
                personnel_id = personnel_id_row[0]
            else:
                raise Exception(f"No personnel found with email {e3.get()}")
            
            # # Retrieve caller_id for the caller
            # cur.execute("SELECT personnel_id FROM personnel WHERE personnel_name = %s", (e5.get(),))
            # caller_id_row = cur.fetchone()
            # if caller_id_row is not None:
            #     caller_id = caller_id_row[0]
            # else:
            #     raise Exception(f"No personnel found with name {e5.get()}")
            # Retrieve problem_type_id for the problem type
            cur.execute("SELECT problem_type_id FROM problem_types WHERE problem_type_name = %s", (problem_type_name,))
            problem_type_id_row = cur.fetchone()
            if problem_type_id_row is not None:
                global_problem_type_id = problem_type_id_row[0]  # Store the problem type ID globally
            else:
                global_problem_type_id = None
                cur.execute("Insert into problem_types (problem_type_id,problem_type_name,parent_problem_type_id) value(%s,%s,%s)",(global_problem_type_id,problem_type_name,None) )
                problem_type_name = cur.fetchone()
                # You can also choose to log this information for future reference
                print(f"No problem type found with name so yoyr issue will be looked by the specialist {problem_type_name}")
                
            cur.execute("select operator_name from Operator where operator_name = %s ",(e6.get()))
            operator_name = cur.fetchone()
            if operator_name is not None:
                messagebox.showinfo("operator found", "The operator will now handel the issues")
            else:
                messagebox.showerror("operator not found")
                print(f"No operator found with name {operator_name}")
                

            cur.execute("SELECT MAX(caller_id) FROM call_log")
            max_caller_id = cur.fetchone()
            if max_caller_id[0] is not None:
                caller_id = max_caller_id[0] + 1
            else:
                caller_id = 1
            # Generate a unique problem number
            cur.execute("SELECT MAX(problem_number) FROM call_log")
            max_problem_number_row = cur.fetchone()
            if max_problem_number_row[0] is not None:
                problem_number = max_problem_number_row[0] + 1
            else:
                problem_number = 1

            # Insert new call into call_log table
            cur.execute("INSERT INTO call_log (caller_name, caller_id, personnel_id, operator_name, call_time, "
                        "computer_serial_number, operating_system, software, problem_description,"
                        "problem_number, problem_type_id) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (e5.get(), caller_id, personnel_id, operator_name, call_time, e7.get(), e8.get(), e9.get(), e10.get(),
                        problem_number, global_problem_type_id))

            # Commit the changes to the database
            connection.commit()

            # Set the current_call_id variable to the newly created call ID
            current_call_id = cur.lastrowid

            # Show success message
            messagebox.showinfo("Success", "New call logged successfully!")
            lb.insert(lb.size(), e5.get(), e6.get(), e8.get(), e9.get(), e10.get(), e14.get())

            # If problem type is not found, find a specialist for the unspecified problem type
            if global_problem_type_id is None:
                # find_specialist()
                # assign_specialist()
                populate_call_log_listbox()

        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))

        finally:
            cur.close()

            e5.delete(0, 'end')
            e6.delete(0, 'end')
            e7.delete(0, 'end')
            e8.delete(0, 'end')
            e9.delete(0, 'end')
            e10.delete(0, 'end')
            e14.delete(0, 'end')
    
  
  
  
#   CONFIGURING TAB 2 PROBLEM REPORT

# Equipment add to database
    l17=Label(tab1,text="Equipment Check")
    l17.config(bg="light green")
    l17.place(x=160,y=280)
    
    l18=Label(tab1,text="Equipment_type")
    l18.config(bg="pink")
    l18.place(x=30,y=320)
    e15=Entry(tab1)
    e15.place(x=130,y=320)
    
    
    l19=Label(tab1,text="Equipment_make")
    l19.config(bg="pink")
    l19.place(x=30,y=360)
    e16=Entry(tab1)
    e16.place(x=130,y=360)
    
    
    l20=Label(tab1,text="software_name")
    l20.config(bg="pink")
    l20.place(x=30,y=400)
    e17=Entry(tab1)
    e17.place(x=130,y=400)
    
    l21=Label(tab1,text="valid_license")
    l21.config(bg="pink")
    l21.place(x=30,y=440)
    c1 =Checkbutton(tab1,text="TRUE")
    c1.place(x=130,y=440)
    c2 =Checkbutton(tab1,text="FALSE")
    c2.place(x=130,y=470)
    
    # e18=Entry(tab1)
    # e18.place(x=130,y=440)
    
    # problem description 
    # l21=Label(tab1,text="problem_description")
    # l21.config(bg="light green")
    # l21.place(x=160, y=200)
    
    
    # l22=Label(tab1,text="Problem")
    # l22.config(bg="pink")
    # l22.place(x=30,y=250)
    # e18=Entry(tab1)
    # e18.place(x=130,y=250)
    
    # l23=Label(tab1,text="Problem")
    # l23.config(bg="pink")
    # l23.place(x=30,y=250)
    # e19=Entry(tab1)
    # e19.place(x=130,y=250)
    


    def check_equipments_and_software():
        try:
            cur = connection.cursor()
            cur.execute("SELECT personnel_id FROM personnel WHERE personnel_email = %s", (e3.get(),))
            personnel_id_row = cur.fetchone()
            if personnel_id_row is not None:
                personnel_id = personnel_id_row[0]
            
            # Check if equipment type and make exist in register of equipment
            cur.execute("SELECT * FROM equipment WHERE equipment_type = %s AND equipment_make = %s", (e15.get(), e16.get()))
            equipment_row = cur.fetchone()
            if equipment_row is not None:
                # Equipment type and make exist in register, insert into database
                cur.execute("INSERT INTO equipment(personnel_id, equipment_type, equipment_make) VALUES(%s, %s, %s)", (personnel_id, e15.get(), e16.get()))
                messagebox.showinfo("Success", "Equipment type and make exist in register!")
            else:
                messagebox.showerror("Error", "Equipment type and make do not exist in register!")
            
            # Check if software is under a valid license
            if c1.getboolean('1'):
                valuecbool = "True"
                # Software is under a valid license, insert into database
                cur.execute("INSERT INTO software_license(personnel_id, software_name, valid_license) VALUES(%s, %s, %s)", (personnel_id, e17.get(), c1.getboolean('1')))
                messagebox.showinfo("Success", "Software is under a valid license!")
            else:
                valuecbool = "False"
                messagebox.showerror("Error", "Software is not under a valid license!")
            lb.insert(lb.size(),e15.get(),e16.get(),e17.get(),valuecbool)
        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            connection.commit()
            connection.close()
        e15.delete(0, 'end')
        e16.delete(0, 'end')
        e17.delete(0, 'end')











    # ---------------------------------------------------------------------
    # confuguring tab2
    
    
    lb1=Listbox(tab2)
    lb1.config(bg="grey")
    lb1.place(x=430,y=30)
    lb1.config(height=30,width=90)
    # ------------------------------
    # def test_entry_value():
    #     value = e14.get()
    #     print(f"Test Entry Value: '{value}'")
    # e14 = tk.Entry(tab2)
    # e14.pack()
        
    # test_button = tk.Button(tab2, text="Test Entry Value", command=test_entry_value)
    # test_button.place(x=30)
    
    def lookup_previous_problems():
        global cur, global_problem_type_name
        try:
            cur = connection.cursor()

            # Retrieve problem type ID from the database
            problem_type_name = global_problem_type_name.strip()
            print(problem_type_name)
            print(f"Raw input from the global variable: '{global_problem_type_name}'")
            print(f"Searching for problem type: '{problem_type_name}'")

            cur.execute("SELECT problem_type_id FROM problem_types WHERE problem_type_name = %s", (problem_type_name,))
            problem_type_id_row = cur.fetchone()

            if problem_type_id_row is not None:
                problem_type_id = problem_type_id_row[0]
            else:
                raise Exception(f"No problem type found with name '{problem_type_name}'")  # For debugging

            # Query the database for previous problems of the same type
            cur.execute("SELECT * FROM call_log WHERE problem_type_id = %s", (problem_type_id,))
            previous_problems = cur.fetchall()

            # Display previous problems
            for problem in previous_problems:
                lb1.insert(tk.END, f"Problem number: {problem[13]}")  # Assuming problem_number is at index 9
                lb1.insert(tk.END, f"Problem name: {problem_type_name}")
                lb1.insert(tk.END, f"Problem description: {problem[9]}")  # Assuming problem_description is at index 8
                lb1.insert(tk.END, f"Solution description: {problem[10]}")  # Assuming solution_description is at index 10
                lb1.insert(tk.END, f"Advise_description: {problem[12]}")  # Assuming problem_number is at index 11
                lb1.insert(tk.END, "")

        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))

        finally:
            # Close the cursor
            cur.close()
            # Call the update_call_log function outside the try-except block to ensure cur is closed even if there's an exception
            update_call_log()

            
            
    l13=Label(tab2,text="solution_description")
    l13.config(bg="pink")
    l13.place(x=40,y=60)
    e11=Entry(tab2)
    e11.place(x=170,y=60)
    
    l14=Label(tab2,text="advise_description")
    l14.config(bg="pink")
    l14.place(x=40,y=105)
    e12=Entry(tab2)
    e12.place(x=170,y=105)
        
            
    
    def update_call_log():
        global current_call_id, cur
        try:
            if current_call_id is None:
                raise Exception("No call selected. Please log a new call or select an existing call from the list.")

            # Get the solution description and advice description from the entry fields
            solution_description = e11.get()
            advise_description = e12.get()

            # Update the solution description, solution time, and advice description in the call_log table
            solution_time = datetime.now()
            cur = connection.cursor()
            cur.execute("UPDATE call_log SET solution_description = %s, solution_time = %s, advise_description = %s WHERE call_id = %s",
                        (solution_description, solution_time, advise_description, current_call_id))

            # Commit the changes to the database
            connection.commit()

            # Show success message
            messagebox.showinfo("Success", "Call log updated successfully!")

            # Clear the entry fields after a successful update
            e11.delete(0, tk.END)
            e12.delete(0, tk.END)

        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))

        finally:
            # Close the cursor
            cur.close()
            
            
            
    lb_call_log = Listbox(tab3, bg="grey", height=10, width=50, selectmode=tk.SINGLE)
    lb_call_log.place(x=430, y=250)
    lb_specialist_info = Listbox(tab3, bg="grey", height=10, width=90, selectmode=tk.SINGLE)
    lb_specialist_info.place(x=430, y=30)
    lb_problem_types = Listbox(tab3, bg="grey", height=30, width=60, selectmode=tk.SINGLE)
    lb_problem_types.place(x=50, y=30)


    def populate_call_log_listbox():
        with connection.cursor() as cur:
            cur.execute("SELECT call_id, problem_description FROM call_log")
            call_log_entries = cur.fetchall()
            lb_call_log.delete(0, tk.END)
            for entry in call_log_entries:
                lb_call_log.insert(tk.END, f"Call ID: {entry[0]}, Problem: {entry[1]}")  # Using integer indices to access tuple elements


    populate_call_log_listbox()


    def populate_problem_types_listbox():
        with connection.cursor() as cur:
            cur.execute("SELECT problem_type_name FROM problem_types")
            problem_types = cur.fetchall()
            lb_problem_types.delete(0, tk.END)
            for problem_type in problem_types:
                lb_problem_types.insert(tk.END, problem_type[0])  # Accessing the first element of the tuple


    populate_problem_types_listbox()


    def populate_specialist_listbox():
        with connection.cursor() as cur:
            cur.execute("SELECT specialist_name FROM specialist")
            specialists = cur.fetchall()
            lb_specialist_info.delete(0, tk.END)
            for specialist in specialists:
                lb_specialist_info.insert(tk.END, specialist[0])


    populate_specialist_listbox()


    def select_problem(event=None):
        selected_index = lb_problem_types.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a problem from the list.")
            return

        selected_problem = lb_problem_types.get(selected_index[0])
        e_manual_problem.delete(0, tk.END)
        e_manual_problem.insert(tk.END, selected_problem)

        print("Selected Problem:", selected_problem)  # Add this line to check the selected problem


    b_select_problem = Button(tab3, text="Select problem", command=select_problem)
    b_select_problem.place(x=880, y=380)
    e_manual_problem = Entry(tab3)
    e_manual_problem.place(x=750, y=380)


    def select_specialist():
        selected_index = lb_specialist_info.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a specialist from the list.")
            return

        selected_specialist = lb_specialist_info.get(selected_index[0])
        e_manual_specialist.delete(0, tk.END)
        e_manual_specialist.insert(tk.END, selected_specialist)

        print("Selected Specialist:", selected_specialist)  # Add this line to check the selected specialist
        # Add button to assign specialist
        b_assign_specialist = Button(tab3, text="Assign Specialist", command=assign_specialist)
        b_assign_specialist.place(x=880, y=430)

    # Add button to select specialist
    b_select_specialist = Button(tab3, text="Select Specialist", command=select_specialist)
    b_select_specialist.place(x=880, y=343)

    # Add entry for specialist
    e_manual_specialist = Entry(tab3)
    e_manual_specialist.place(x=750, y=340)

    # Add button to select specialist
    # b_select_specialist = Button(tab3, text="Select Specialist", command=select_specialist)
    # b_select_specialist = Button(tab3, text="Select Specialist", command=assign_specialist)
    # b_select_specialist.place(x=880, y=343)

    e_manual_specialist = Entry(tab3)
    e_manual_specialist.place(x=750, y=340)


    def assign_to_call_log():
        selected_index = lb_call_log.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a call log from the list.")
            return

        selected_call_log = lb_call_log.get(selected_index[0])
        e_manual_call_log.delete(0, tk.END)
        e_manual_call_log.insert(tk.END, selected_call_log)

        print("Selected Call Log:", selected_call_log)  # Add this line to check the selected call log


    e_manual_call_log = Entry(tab3)
    e_manual_call_log.place(x=750, y=300)

    b_select_call_log = Button(tab3, text="Select Call Log", command=assign_to_call_log)
    b_select_call_log.place(x=880, y=300)

    def assign_specialist():
        selected_specialist = e_manual_specialist.get()  # Get the value from the entry widget
        with connection.cursor() as cur:
            # Check if the specialist exists in the database
            cur.execute("SELECT specialist_id FROM specialist WHERE specialist_name = %s", (selected_specialist,))
            specialist_id = cur.fetchone()

            if specialist_id is None:
                messagebox.showerror("Specialist Not Found", "The selected specialist does not exist in the database.")
                return

            # Get the call_id from the selected call log
            selected_call_log = e_manual_call_log.get()

            # Update the SpecialistAllocation table
            cur.execute("INSERT INTO SpecialistAllocation (specialist_id, call_id) VALUES (%s, %s)", (specialist_id[0], selected_call_log))
            connection.commit()

            # Update the specialist's workload
            cur.execute("UPDATE specialist SET current_workload = current_workload + 1 WHERE specialist_id = %s", (specialist_id[0],))
            connection.commit()

            messagebox.showinfo("Success", "Specialist assigned successfully and workload increased.\nThank you!")




    # def assign_specialist():
    #     cur=connection.cursor()
    #     cur.execute("select specialist_id from specialist where specialist_name = %s",(e_manual_specialist))
    #     specelist_id=cur.fetchone()
    #     if specelist_id is None:
    #         messagebox.ERROR("no specialist","specialist not found")
        
    #     allocated_expert =cur.execute("insert into SpecialistAllocation values(specialist_id,call_id)values(%s,%s)",(specelist_id,e_manual_call_log))
    #     if allocated_expert == True:
    #         cur.execute("UPDATE specialist SET current_workload = current_workload + 1 WHERE specialist_id = %s", (specelist_id))
    #         messagebox.showinfo("succesfully assigned","you have assigned to specialist and his workload is also incresed \n thank you!!!")


    
    # Add button to assign specialist
    b_assign_specialist = Button(tab3, text="Assign Specialist", command=assign_specialist)
    b_assign_specialist.place(x=880, y=430)


    # Add button to assign specialist to call log

    


# -------------------------------------------------
# -------------------------conf tab 4
    lb3=Listbox(tab4,height=30,width=150)
    lb3.config(bg="grey")
    lb3.place(x=30,y=50)

    def show_resolution():
        try:
            with connection.cursor() as cur:
                cur.execute("SELECT call_id, resolution_time, resolution_description,resolution_duration FROM problem_resolution ORDER BY call_id ASC")
                resolution = cur.fetchall()
                # cur.execute("SELECT problem_description FROM  call_log WHERE call_id = %s ",(resolution,))
                # problem_name =cur.fetchall
            if not resolution:
                messagebox.showerror("Error", "No resolution found in the database.")
                return

            lb3.delete(0, tk.END)
            for resolution in resolution:
                call_id = resolution[0]
                # problem_desc =problem_name[1]
                resolution_time = resolution[1]
                resolution_description = resolution[2]
                resolution_duration = resolution[3]

                lb3.insert(tk.END, f"Call ID: {call_id}")
                # lb3.insert(tk.END, f"Problem Descriprion: {problem_desc}")
                lb3.insert(tk.END, f"Resolution time: {resolution_time}")
                lb3.insert(tk.END, f"Resolution Description: {resolution_description}")
                lb3.insert(tk.END, f"Resolution Duration: {resolution_duration}")
                lb3.insert(tk.END, "")

        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))
    show_resolution()



# -------------------------------------------------
# -------------------------conf tab 5
    lb4=Listbox(tab5,height=30,width=150)
    lb4.config(bg="grey")
    lb4.place(x=30,y=50)
    
    def show_specialist_training():
        try:
            with connection.cursor() as cur:
                cur.execute("SELECT specialist_id, training_name, training_date,training_duration FROM Training ORDER BY training_date ASC")
                training = cur.fetchall()

            if not training:
                messagebox.showerror("Error", "No training found in the database.")
                return

            lb4.delete(0, tk.END)
            for training in training:
                specialist_id = training[0]
                training_name = training[1]
                training_date = training[2]
                training_duration = training[3]

                lb4.insert(tk.END, f"Specialist ID: {specialist_id}")
                lb4.insert(tk.END, f"Training Name: {training_name}")
                lb4.insert(tk.END, f"Training Date: {training_date}")
                lb4.insert(tk.END, f"Training Duration: {training_duration}")
                lb4.insert(tk.END, "")

        except Exception as e:
            # Show error message
            messagebox.showerror("Error", str(e))
    show_specialist_training()













# Create another listbox to display the specialist information
        
    b0=Button(page, text="logout",command=logout)
    b0.place(x=780,y=600)

    b1 = Button(tab1,text="check",command=onCheck)
    b1.place(x=50, y=230)
    
    b2 = Button(tab1,text="submit",command=log_new_call)
    b2.place(x=510,y=450)
    
    b3 =Button(tab1,text="go to customer helpdesk",command=go_to_customer_help_desk)
    b3.place(x=780,y=620)
    
    b4=Button(tab1,text="check_equips",command=check_equipments_and_software)
    b4.place(x=50, y=520)
    
    b5 = Button(tab2, text="Lookup Previous Problems", command=lookup_previous_problems)
    b5.place(x=270,y=350)
    
    # Add button to Assign_Issue tab
    # b6 = Button(tab3, text="Assign Specialist", command=assign_specialist)
    # b6.place(x=850,y=500)
    
    b7 =Button(tab2,text="update call_log",command=update_call_log)
    b7.place(x=150,y=220)