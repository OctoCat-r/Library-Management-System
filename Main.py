from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

# Adding database name and password here
Pass = "Aman@1012"
Database="aman"

connection = pymysql.connect(host="localhost",user="root",password=Pass,database=Database)
cur = connection.cursor()

arsng = Tk()
arsng.title("Library Management System")
arsng.minsize(width=400,height=400)
arsng.geometry("900x600")


my_canvas = Canvas(arsng)

# Adding a background image
def resized(e):
    global bg1, background_image, img
    bg1 =Image.open("/Users/amanjain/Downloads/bbook.jpeg")

    
    background_image = bg1.resize((e.width,e.height),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    
    my_canvas.create_image(0, 0 , image = img, anchor = "nw")    



my_canvas.config(bg="#EEE685")
my_canvas.pack(expand=True,fill='both')

frame_heading = Frame(arsng)
frame_heading.place(relx=0.02,rely=0.15,relwidth=0.45,relheight=0.16)

label_heading = Label(frame_heading, text="Welcome to ARSNG Library", fg='black', font=('Courier',25), relief=RAISED)
label_heading.place(relx=0,rely=0, relwidth=1, relheight=1)

frame_quote = Frame(arsng)
frame_quote.place(relx=0.51,rely=0.22, relwidth=0.30,relheight=0.20)

label_quote = Label(frame_quote, text="If everyone is moving\n forward together,\n thn success will \n take care of itself..",bg='#D1D1D1',fg='black', font=('Comic Sans MS', 20))
label_quote.place(relx=0, rely=0, relwidth=1, relheight=1)


# Adding button

buttn1 = Button(arsng,text="Add Book Details", font=('Helvetica'),relief=RAISED, command=addBook)
buttn1.place(relx=0.07,rely=0.35, relwidth=0.35,relheight=0.1)

    
buttn2 = Button(arsng,text="Delete Book", command=delete)
buttn2.place(relx=0.07,rely=0.46, relwidth=0.35,relheight=0.1)
    
buttn3 = Button(arsng,text="View Book List",bg='black', fg='black', command=Viewbooks)
buttn3.place(relx=0.07,rely=0.57, relwidth=0.35,relheight=0.1)
    
buttn4 = Button(arsng,text="Issue Book to Student",bg='black', fg='black', command=issueBook)
buttn4.place(relx=0.07,rely=0.68, relwidth=0.35,relheight=0.1)
    
buttn5 = Button(arsng,text="Return Book",bg='black', fg='black', command=returnBook)
buttn5.place(relx=0.07,rely=0.79, relwidth=0.35,relheight=0.1)

arsng.bind('<Configure>', resized)
arsng.mainloop()