from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
Pass = "Aman@1012"
Database="aman"

connection = pymysql.connect(host="localhost",user="root",password=Pass,database=Database)
cur = connection.cursor()

# Enter Table Names here
bookTable = "books" 
    
def Viewbooks(): 
    
    arsng = Tk()
    arsng.title("Library Management System")
    arsng.minsize(width=400,height=400)
    arsng.geometry("600x500")


    my_canvas = Canvas(arsng) 
    my_canvas.config(bg="#698B69")
    my_canvas.pack(expand=True,fill=BOTH)
        
        
    frame_heading = Frame(arsng,bg="#FFBB00",bd=1)
    frame_heading.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    Label_heading = Label(frame_heading, text="View Books", bg='black', fg='white', font=('Courier',15), relief= RAISED)
    Label_heading.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    Frame_label = Frame(arsng,bg='black',bd=1)
    Frame_label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.35
    
    Label(Frame_label, text="%-15s%-40s%-40s%-0s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.04,rely=0.1)
    Label(Frame_label, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.01,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        connection.commit()
        for i in cur:
            Label(Frame_label, text="%-10s%-35s%-40s%-0s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.04,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitButtn = Button(arsng,text='Exit', bg='blue', command=arsng.destroy)
    quitButtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    
    arsng.mainloop()
Viewbooks()