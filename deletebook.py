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
issueTable = "books_issued" 
bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()
    
    deletemySql = "delete from "+bookTable+" where bid = '"+bid+"'"
    delete_Issue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deletemySql)
        connection.commit()
        cur.execute(delete_Issue)
        connection.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    arsng.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,my_canvas,connection,cur,bookTable,arsng
    
    arsng = Tk()
    arsng.title("Library")
    arsng.minsize(width=400,height=400)
    arsng.geometry("600x500")

    
    my_canvas = Canvas(arsng)
    
    my_canvas.config(bg="#698B69")
    my_canvas.pack(expand=True,fill=BOTH)
        
    frame_heading = Frame(arsng,bg="#FFBB00",bd=2)
    frame_heading.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    Label_heading = Label(frame_heading, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    Label_heading.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frame_label = Frame(arsng,bg='black')
    frame_label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    label2 = Label(frame_label,text="Book ID : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(frame_label)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitButtn = Button(arsng,text="SUBMIT",command=deleteBook)
    SubmitButtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitButtn = Button(arsng,text="Exit", command=arsng.destroy)
    quitButtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    arsng.mainloop()
delete()
deleteBook()