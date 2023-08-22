from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import datetime
from PIL import Image, ImageTk
import createOp as c
import LicenseReq as lr
import RCReq
import Renew
import pymysql as sql
import main1 as adi
import say
loginusername = ""

def createopwindow(root):
    root.destroy()
    # Toplevel(c.main())
    c.main(loginusername)


def oplrwindow(root):
    root.destroy()
    # Toplevel(lr.main())
    lr.main(loginusername)


def oprenew(root):
    root.destroy()
    Renew.main(loginusername)


def openrc(root):
    root.destroy()
    RCReq.main(loginusername)



def Logout():
    global loginusername
    loginusername=""
    messagebox.showinfo("information", "Are you sure you want to LOG OUT ?")
    say.speak("You Logged Out Successfully,have a good day ahead,THANk YOU")
    quit()
    adi.main_screen()


def main(uname=""):
    print(uname)
    global loginusername
    loginusername = uname
    user_name = ""
    con = sql.connect(host='localhost', user='root', password='', database='minor_project')
    cur = con.cursor()

    if loginusername == "":
        showinfo(title="Alert", message="Please Login First")
        quit()
        #  adding the back window again
    else:
        cur.execute("select name from admin_login where username='{0}'".format(loginusername))
        user_name= cur.fetchone()[0]

    root = Tk()
    root.state("zoomed")
    root.title("Admin Dashboard - E - R.T.O")

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

    topLabel = Label(TopFrame, text="Admin Dashboard", padx=20, pady=40, font=("seogeui 25 bold"), bg="blue", fg="white")
    topLabel.place(x=100,y=0, width=w-100, height=100)

    MainBoard = Frame(root, bg="#A6B4F7")
    MainBoard.place(x=0, y=100, width=w, height=h-100)

    image = Image.open("brto.jpg")
    resize_image = image.resize((w, MainBoard.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)


    lbl = Label(MainBoard, image=img)
    lbl.place(x=0, y=0, width=w, height=MainBoard.winfo_screenheight())

    # license = Button(MainBoard,text="License", bg="white", fg="blue",highlightcolor="blue", highlightbackground="blue", borderwidth=2, font=("seogeui 22 bold"), highlightthickness=0, activebackground="blue", activeforeground="white")
    # license.place(x=200, y=80, width=400, height=120)

    info = Label(MainBoard, text=f"Hello, {user_name}\n{datetime.datetime.today().date()}\n{datetime.datetime.today().time()}", bg="white", font=("comicsansms 12 bold"), borderwidth=2, relief=SOLID)
    info.place(x=0, y=0, width=200, height=100)

    licf = Frame(MainBoard)
    licf.place(x=100, y=100, width=250, height=300)
    img2 = Image.open("licphoto1.jpg")
    rimage=img2.resize((250, 200))
    image1 = ImageTk.PhotoImage(rimage)
    imagelbl = Label(licf, image=image1)
    imagelbl.place(x=0, y=0)
    license = Button(licf,text="License", bg="white", fg="blue",highlightcolor="blue", highlightbackground="blue", borderwidth=2, font=("seogeui 22 bold"), highlightthickness=0, activebackground="blue", activeforeground="white", command=lambda:oplrwindow(root))
    license.place(x=0, y=200, width=250, height=100)

    rcf = Frame(MainBoard)
    rcf.place(x=400, y=100, width=250, height=300)
    rcimg = Image.open("rcimage.png")
    rcres = rcimg.resize((250, 200))
    rcimg1 = ImageTk.PhotoImage(rcres)
    rclbl = Label(rcf, image=rcimg1)
    rclbl.place(x=0, y=0)
    rc = Button(rcf, text="RC", bg="white", fg="blue", highlightcolor="blue", highlightbackground="blue",
                     borderwidth=2, font=("seogeui 22 bold"), highlightthickness=0, activebackground="blue",
                     activeforeground="white", command=lambda:openrc(root))
    rc.place(x=0, y=200, width=250, height=100)


    copf = Frame(MainBoard)
    copf.place(x=700, y = 100, width = 250, height = 300)
    copimg = Image.open("operatorimg.png")
    copres = copimg.resize((250, 200))
    copimg1 = ImageTk.PhotoImage(copres)
    coplbl = Label(copf, image=copimg1)
    coplbl.place(x=0, y=0)
    createOperators = Button(copf, text="Create\nOperators", bg="white", fg="blue", highlightcolor="blue", highlightbackground="blue",
                     borderwidth=2, font=("seogeui 22 bold"), highlightthickness=0, activebackground="blue",
                     activeforeground="white", command=lambda: createopwindow(root))
    createOperators.place(x=0, y=200, width=250, height=100)

    rf = Frame(MainBoard)
    rf.place(x=1000, y=100, width=250, height=300)
    rfimg = Image.open("renewimg.png")
    rfres = rfimg.resize((250, 200))
    rfimg1 = ImageTk.PhotoImage(rfres)
    rflbl = Label(rf, image=rfimg1)
    rflbl.place(x=0, y=0)
    renew = Button(rf, text="Renew", bg="white", fg="blue", highlightcolor="blue", highlightbackground="blue",
                     borderwidth=2, font=("seogeui 22 bold"), highlightthickness=0, activebackground="blue",
                     activeforeground="white", command=lambda : oprenew(root))
    renew.place(x=0, y=200, width=250, height=100)

    logout = Button(MainBoard, text="<-Log Out", fg="red", bg='white', activebackground="red", activeforeground="white", font=('comicsansms 14 bold'), command=lambda : Logout())
    logout.place(x=root.winfo_screenwidth()-150, y=0, width=150, height=50)
    root.mainloop()

if __name__ == "__main__":
    main()