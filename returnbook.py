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
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


allB_id = [] #List To store all Book IDs

def returnn():
    
    global submit_button,frame_label,label1,bookInfo1,quit_button,arsng,my_canvas,status
    
    bid = bookInfo1.get()

    extractBid = "select bid from "+issueTable
    try:
        cur.execute(extractBid)
        connection.commit()
        for i in cur:
            allB_id.append(i[0])
        
        if bid in allB_id:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            connection.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
  
    print(bid in allB_id)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
    try:
        if bid in allB_id and status == True:
            cur.execute(issueSql)
            connection.commit()
            cur.execute(updateStatus)
            connection.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allB_id.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            arsng.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allB_id.clear()
    arsng.destroy()
    
def returnBook(): 
    
    global bookInfo1,submit_button,quit_button,my_canvas,connection,cur,arsng,frame_label, label1
    
    arsng = Tk()
    arsng.title("Library")
    arsng.minsize(width=400,height=400)
    arsng.geometry("600x500")

    
    my_canvas = Canvas(arsng)
    
    my_canvas.config(bg="#698B69")
    my_canvas.pack(expand=True,fill=BOTH)
        
    frame_heading = Frame(arsng,bg="#FFBB00",bd=2)
    frame_heading.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    Label_heading = Label(frame_heading, text="Return Book", bg='black', fg='white', font=('Courier',15))
    Label_heading.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frame_label = Frame(arsng,bg='black')
    frame_label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    label1 = Label(frame_label,text="Book ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(frame_label)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    submit_button = Button(arsng,text="Return",command=returnn)
    submit_button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quit_button = Button(arsng,text="Exit", command=arsng.destroy)
    quit_button.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    arsng.mainloop()
returnBook()
returnn()