from tkinter import*
import sqlite3

root=Tk()
root.title('VINCE Project')
root.geometry("500x500")

conn=sqlite3.connect('mydata.db')

c = conn.cursor()

'''

c.execute("""CREATE TABLE "mydata" (
	"f name"	TEXT,
	"L name"	TEXT,
	"age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT
)""")

'''

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

L_name=Entry(root,width=30)
L_name.grid(row=1,column=1,padx=20)

age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)

email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)

def submit():

    conn=sqlite3.connect('C:/Users\STUDENT6/Pictures/vince/mydata.db')

submit_btn=Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

c.execute("INSERT INTO Student_info VALUES(:f_name,:L_name,:age,:address,:email)",
          {
            'f_name':f_name.get()
            'L_name':L_name.get()
            'age':age.get()
            'adress':address.get()
            'email':email.get()
    
          })
                  
conn.commit()
conn.close()

root.mainloop()
