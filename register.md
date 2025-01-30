# User registration 
import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox

# Connect to the MySQL database
cn= mysql.connect (database= 'python', user= "root", password= "root")

# Create GUI window
w= gui.Tk()
w.geometry ("300x200")
w.title (" User Register")

# Define a function to register the user
def register():
   c= cn.cursor()
   try:
      name= e1.get()
      user= e2.get()
      pwd= e3.get()
      roll= 1
      c.execute ("insert into user values (%s, %s, %s ,%s)", params= (roll, name, user, pwd))
      
      tkinter.messagebox.showinfo (title= "info", message= "User Registered..")
      
      cn.commit()
      e1.delete (0, gui.END)
      e2.delete (0, gui.END)
      e3.delete (0, gui.END)
      
    except:
       tkinter.messagebox.showerror (title= "error", message= "Error in registrating user")
       
def close():
          w.destroy()
          
# Define labels and entry fields for name, username and password 
l1= gui.Label (w, text="Name", font= ("Arial", 14))
l2= gui.Label (w, text="Username", font= ("Arial", 14))
l3= gui.Label (w, text="Password", font= ("Arial", 14))

e1= gui.Entry (w, width= 20, font= ("Arial", 14))
e2= gui.Entry (w, width= 20, font= ("Arial", 14))
e3= gui.Entry (w, width= 20, font= ("Arial", 14), show= '*')

b1= gui.Button (w, text="Register", width= 10, font= ("Arial", 14), command= register)
b2= gui.Button (w, text="Exit", width=10, font= ("Arial", 14), command= close)


# Place labels, entry fields and button in window
l1.grid (row=1, column=1)
l2.grid (row=2, column=1)
l3.grid (row=3, column=1)

e1.grid (row=1, column=2)
e2.grid (row=2, column=2)
e3.grid (row=3, column=2)

b1.grid (row=4, column=1)
b2.grid (row=4, column=2)

w.mainloop()