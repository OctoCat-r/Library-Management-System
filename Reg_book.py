from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def Reg_book():
    
    b_id = bookInfo1.get()
    book_name = bookInfo2.get()
    writer = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+b_id+"','"+book_name+"','"+writer+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        connection.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(b_id)
    print(book_name)
    print(writer)
    print(status)


    arsng.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,my_canvas,connection,cur,bookTable,arsng
    
    arsng = Tk()
    arsng.title("Library Management System")
    arsng.minsize(width=400,height=400)
    arsng.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    Pass = "Aman@1012"
    Database="aman"

    connection = pymysql.connect(host="localhost",user="root",password=Pass,database=Database)
    cur = connection.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    my_canvas = Canvas(arsng)
    
    my_canvas.config(bg="#698B69")
    my_canvas.pack(expand=True,fill=BOTH)
        
    frame_heading = Frame(arsng,bg="#FFBB00",bd=2)
    frame_heading.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    Label_heading = Label(frame_heading, text="Add Books", bg='black', fg='white', font=('Courier',15))
    Label_heading.place(relx=0,rely=0, relwidth=1, relheight=1)


    Frame_label = Frame(arsng,bg='black')
    Frame_label.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    label1 = Label(Frame_label,text="Book ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(Frame_label)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    label2 = Label(Frame_label,text="Title : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(Frame_label)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    label3 = Label(Frame_label,text="Author : ", bg='black', fg='white')
    label3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(Frame_label)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    label4 = Label(Frame_label,text="Status(Avail/issued) : ", bg='black', fg='white')
    label4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(Frame_label)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitButtn = Button(arsng,text="SUBMIT",bg='#d1ccc0', fg='black',command=Reg_book, relief=RAISED)
    SubmitButtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitButtn = Button(arsng,text="Exit",bg='#f7f1e3', fg='black', command=arsng.destroy)
    quitButtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    arsng.mainloop()
addBook()  
Reg_book()