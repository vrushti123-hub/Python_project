import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox

# Establish connection to the database
try:
    cn = mysql.connect(database="userdatabase1", user="root", password="vrushti123")
except mysql.Error as err:
    tkinter.messagebox.showerror("Database Error", f"Error: {err}")
    exit()

# Main window setup
w = gui.Tk()
w.geometry("300x200")

# Function to handle marks entry window
def marks_window():
    w1 = gui.Tk()
    w1.geometry("300x200")
    
    # Labels and entries for Roll No, Name, and Subjects
    l1 = gui.Label(w1, text="Rollno", font=("Arial", 14))
    l2 = gui.Label(w1, text="Name", font=("Arial", 14))
    l3 = gui.Label(w1, text="Subject1", font=("Arial", 14))
    l4 = gui.Label(w1, text="Subject2", font=("Arial", 14))
    
    e1 = gui.Entry(w1, width=10)
    e2 = gui.Entry(w1, width=10)
    e3 = gui.Entry(w1, width=10)
    e4 = gui.Entry(w1, width=10)
    
    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    l3.grid(row=3, column=1)
    l4.grid(row=4, column=1)
    
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)
    e4.grid(row=4, column=2)
    
    # Save function to insert data into the database
    def save():
        rno = e1.get()
        name = e2.get()
        s1 = e3.get()
        s2 = e4.get()
        
        try:
            # Check if inputs are valid
            if not rno or not name or not s1 or not s2:
                tkinter.messagebox.showwarning(title="Input Error", message="All fields must be filled")
                return
            
            # Use tuple for parameters
            c = cn.cursor()
            c.execute("insert into student_marks(rollno, name, sub1, sub2) values(%s, %s, %s, %s)", (rno, name, s1, s2))
            cn.commit()
            
            # Success message
            tkinter.messagebox.showinfo(title="Info", message="Marks details are saved")
            
            # Clear entry fields
            e1.delete(0, gui.END)
            e2.delete(0, gui.END)
            e3.delete(0, gui.END)
            e4.delete(0, gui.END)
        
        except mysql.Error as err:
            # Handle MySQL errors
            tkinter.messagebox.showerror(title="Database Error", message=f"Error: {err}")
        except Exception as e:
            # Handle other errors
            tkinter.messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    
    b1 = gui.Button(w1, text="Save", command=save)
    b1.grid(row=5, column=1)

# Function to handle find result window
def find_window():
    w3 = gui.Tk()
    w3.geometry("300x200")
    w3.title("Find Result")
    
    l1 = gui.Label(w3, text="Rollno", font=("Arial", 14))
    e1 = gui.Entry(w3, width=10)
    
    l1.grid(row=1, column=1)
    e1.grid(row=1, column=2)
    
    # Find result function
    def find():
        try:
            c = cn.cursor()
            
            # Execute the query to get the student's details
            c.execute("select rollno, name, sub1, sub2, sub1 + sub2 from student_marks where rollno = %s", (e1.get(),))
            row = c.fetchone()
            
            if row is None:
                tkinter.messagebox.showinfo(title="Info", message="Invalid Rollno")
            else:
                # Check pass/fail status
                result = "Pass" if int(row[2]) >= 40 and int(row[3]) >= 40 else "Fail"
                
                # Format the result into a readable string
                result_text = (
                    f"Roll No: {row[0]}\n"
                    f"Name: {row[1]}\n"
                    f"Subject 1: {row[2]}\n"
                    f"Subject 2: {row[3]}\n"
                    f"Total: {row[4]}\n"
                    f"Result: {result}"
                )
                
                # Display the formatted result
                l2 = gui.Label(w3, text=result_text, font=("Arial", 14), justify=gui.LEFT)
                l2.grid(row=2, column=1)
    
        except mysql.Error as err:
            # Handle MySQL errors
            tkinter.messagebox.showerror(title="Database Error", message=f"Error: {err}")
        except Exception as e:
            # Handle other errors
            tkinter.messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    
    b1 = gui.Button(w3, text="Find Result", command=find)
    b1.grid(row=3, column=1)

# Buttons for main window
b1 = gui.Button(w, text="Marks Entry", font=("Arial", 14), command=marks_window)
b2 = gui.Button(w, text="Find Result", font=("Arial", 14), command=find_window)

# Pack the buttons
b1.pack(fill=gui.BOTH, expand=True)
b2.pack(fill=gui.BOTH, expand=True)

w.mainloop()
