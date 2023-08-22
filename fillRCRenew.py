from tkinter import *
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk
import pymysql as sql

sqlst = []

def getCon():
    con = sql.connect(host='localhost', user='root', password='', database='minor_project')
    cur = con.cursor()
    con.get_autocommit()
    return [cur, con]

def viewDetails(aadhaar, mobno, fname):
    global sqlst
    sqlst = getCon()
    cur=sqlst[0]
    s1 = cur.execute(f"select Registration_No, Aadhaar_number, name , Mobile_num from rc where Aadhaar_number = '{aadhaar.get()}'")
    lst = cur.fetchone()
    print(lst)
    if s1 == 1:
        if lst[0] == None:
            showinfo(title="Message", message="Can't Apply No DL Exist")
        else:
            mobno.set(lst[3])
            fname.set(lst[2])
    else:
        showinfo(title="Message", message="Aadhaar Number doesn't exist")



def submitDet(aadhaar, mobno, fname):
    cur=sqlst[0]
    con=sqlst[1]
    print(aadhaar.get(), mobno.get(), fname.get())

    s = cur.execute(f"insert into renewstatus values('{aadhaar.get()}', Null, 'PENDING')")
    con.commit()
    s=cur.execute(f"update rc set mobile_num = '{mobno.get()}' where aadhaar_number='{aadhaar.get()}'")
    print(s)
    con.commit()
    s=cur.execute(f"update rc set name = '{fname.get()}' where aadhaar_number='{aadhaar.get()}'")
    con.commit()
    showinfo(title="Message", message="Request Sent")


def main():
    root = Tk()
    root.title("RC Renew Window")
    root.state("zoomed")
    root.minsize(1200, 900)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    TopFrame = Frame(root)
    TopFrame.place(x=0, y=0, width=w, height=100)

    img = Image.open("rtoimage.png")
    rimg = img.resize((100, 100))
    img1 = ImageTk.PhotoImage(rimg)

    PhotoLabel = Label(TopFrame, image=img1)
    PhotoLabel.place(x=0, y=0, width=100, height=100)

    topLabel = Label(TopFrame, text="RC Renew Window", padx=20, pady=40, font=("seogeui 25 bold"), bg="green",
                     fg="white")
    topLabel.place(x=100, y=0, width=w - 100, height=100)

    #MainBoard-----------
    MainBoard = Frame(root, bg="#A6B4F7")
    MainBoard.place(x=0, y=100, width=w, height=h - 100)

    image = Image.open("BackRTO.jpg")
    resize_image = image.resize((w, MainBoard.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)

    lbl = Label(MainBoard, image=img)
    lbl.place(x=0, y=0, width=w, height=MainBoard.winfo_screenheight())

    #--------------------
    #Adding status frame
    statusFrame = Frame(MainBoard, bg="white")
    statusFrame.place(x=100, y=50, width=1000, height=500)

    adno = Label(statusFrame, text="Aadhaar Number", bg="white", fg="black", font=("seogeui 22 bold"), padx=10, pady=10)
    adno.place(x=100, y=20,width=500, height=40)


    aadhaar = StringVar()
    mobno = StringVar()
    fname = StringVar()
    # owner = StringVar()

    aadno_entry = Entry(statusFrame, textvariable=aadhaar, bg="white", fg="black", font=("seogeui 18"), borderwidth=2, relief=SOLID)
    aadno_entry.place(x=500, y=20, width=300, height=40)

    view = Button(statusFrame, text="View", bg="green", fg="white", font=("consolas 16 bold italic"),borderwidth=2, relief=SOLID, command=lambda : viewDetails(aadhaar, mobno, fname), activebackground='white', activeforeground='green')
    view.place(x=500, y=100, width=100, height=50)
    #-------------------
    #status options-----
    mno = Label(statusFrame, text="Mobile Number : ", bg='white', fg='black', font="comicsansms 15 bold")
    mno.place(x=200, y=180, width=300, height=40)
    fn = Label(statusFrame, text="Full Name : ", bg='white', fg='black', font="comicsansms 15 bold")
    fn.place(x=200, y=230, width=300, height=40)
    # own = Label(statusFrame, text="Owner Name : ", bg='white', fg='black', font="comicsansms 15 bold")
    # own.place(x=200, y=280, width=300, height=40)


    ls = Entry(statusFrame, textvariable=mobno, bg='white', fg='black', font="comicsansms 15 bold", relief=SOLID)
    ls.place(x=500, y=180, width=300, height=40)
    dls = Entry(statusFrame, textvariable=fname, bg='white', fg='black', font="comicsansms 15 bold", relief=SOLID)
    dls.place(x=500, y=230, width=300, height=40)
    # o = Entry(statusFrame, textvariable=owner, bg='white', fg='black', font="comicsansms 15 bold", relief=SOLID)
    # o.place(x=500, y=280, width=300, height=40)

    submit = Button(statusFrame, text="Submit", bg="green", fg="white", font=("consolas 16 bold italic"), borderwidth=2,relief=SOLID, command=lambda: submitDet(aadhaar, mobno, fname), activebackground='white',
    activeforeground='green')
    submit.place(x=500, y=280, width=100, height=50)
    #-------------------
    root.mainloop()

if __name__ == "__main__":
    main()