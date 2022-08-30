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
bookTable = "books"
    
#List To store all Book IDs
allB_id = [] 

def issue():
    
    global issue_button,frame_label,label1,inf1,inf2,quitBtn,arsng,my_canvas,status
    
    bid = inf1.get()
    issueto = inf2.get()

    issue_button.destroy()
    frame_label.destroy()
    label1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBid = "select bid from "+bookTable
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
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allB_id and status == True:
            cur.execute(issueSql)
            connection.commit()
            cur.execute(updateStatus)
            connection.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            arsng.destroy()
        else:
            allB_id.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            arsng.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    allBid.clear()
    
def issueBook(): 
    
    global issue_button,frame_label,label1,inf1,inf2,quitBtn,arsng,my_canvas,status
    
    arsng = Tk()
    arsng.title("Library")
    arsng.minsize(width=400,height=400)
    arsng.geometry("600x500")
    
    my_canvas = Canvas(arsng)
    my_canvas.config(bg="#698B69")
    my_canvas.pack(expand=True,fill=BOTH)

    frame_heading = Frame(arsng,bg="#FFBB00",bd=2)
    frame_heading.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(frame_heading, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    frame_label = Frame(arsng,bg='black')
    frame_label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    label1 = Label(frame_label,text="Book ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(frame_label)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    label2 = Label(frame_label,text="Issued To : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(frame_label)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issue_button = Button(arsng,text="Issue",command=issue)
    issue_button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(arsng,text="Exit", command=arsng.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    arsng.mainloop()
issueBook()
issue()