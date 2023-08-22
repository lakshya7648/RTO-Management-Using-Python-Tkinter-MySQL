from tkinter import *
# from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import AdminDashboard as ad
import pymysql as sql

loginusername=""

def openConnection():
    con = sql.connect(host="localhost", user="root", password="", database="minor_project")
    cur = con.cursor()
    lst = [con, cur]
    return lst


def insertValues(backF, fnameentry, unameentry, pnameentry):
    # pgbar= ttk.Progressbar(backF, orient="horizontal", length=300, mode='determinate')
    # pgbar['value'] = 100
    # pgbar.start()

    lst = openConnection()
    cur=lst[1]
    # print(f"'{fnameentry.get()}', '{unameentry.get()}', '{pnameentry.get()}'")
    s = cur.execute(f"insert into operator_login values('{fnameentry.get()}', '{unameentry.get()}', '{pnameentry.get()}')")
    lst[0].commit()

    # pgbar.stop()
    showinfo(title="Message",message="Operator Created")
    fnameentry.set('')
    unameentry.set('')
    pnameentry.set('')


def closewindow(root):
    root.destroy()
    # Toplevel(ad.main())
    ad.main(loginusername)


def main(uname=""):
    global loginusername
    loginusername=uname
    root = Tk()
    root.state("zoomed")
    root.title("Create Operators")
    root.minsize(1200, 900)
    showinfo(title="Alert", message="Fields asked must be filled unique and should not be left blank")
    backF = Frame(root)
    backF.place(x=0,y=0,width=root.winfo_screenwidth(), height=root.winfo_screenheight())

# -----Adding Background Image------
    img = Image.open("opback.jpg")
    rimg = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    rimg1 = ImageTk.PhotoImage(rimg)
    imglbl = Label(backF, image=rimg1)
    imglbl.place(x=0, y=0)
# -----------------------------------
    logframe = Frame(backF, bg="#5A5757")
    logframe.place(x=700, y=50,width=600, height=backF.winfo_screenheight()-150)

    fname = Label(logframe, text="FULL NAME", fg="white", bg="#5A5757", font=("SeogeUI 25 bold"))
    fname.place(x=80, y=80)
    fnameentry = StringVar()
    fentry = Entry(logframe, textvariable=fnameentry, bg="white", selectbackground="#D8C457", font=("seogeui 20 italic"))
    fentry.place(x=85, y=140, width=400, height=40)

    uname = Label(logframe, text='USERNAME', fg="white", bg="#5A5757", font=("SeogeUI 25 bold"))
    uname.place(x=80, y=220)
    unameentry = StringVar()
    uentry = Entry(logframe, textvariable=unameentry, bg="white", selectbackground="#D8C457",
                   font=("seogeui 20 italic"))
    uentry.place(x=85, y=280, width=400, height=40)

    # -----------------------------------
    pname = Label(logframe, text='PASSWORD', fg="white", bg="#5A5757", font=("SeogeUI 25 bold"))
    pname.place(x=80, y=360)
    pnameentry = StringVar()
    pentry = Entry(logframe, textvariable=pnameentry, bg="white", selectbackground="#D8C457",
                   font=("SeogeUI 20 italic"))
    pentry.place(x=85, y=420, width=400, height=40)
# ------------------------------------------------------
    create = Button(logframe, text="Create", bg="white", fg="black", font=("seogeui 25 bold"), activebackground="#464545", activeforeground="white", command=lambda: insertValues(backF, fnameentry, unameentry, pnameentry))
    create.place(x=100, y=500, width=200, height=50)

    cancel = Button(logframe, text="Cancel", bg="white", fg="black", font=("seogeui 25 bold"),
                    activebackground="#464545", activeforeground="white",
                    command=lambda: closewindow(root))
    cancel.place(x=320, y=500, width=200, height=50)
    root.mainloop()

if __name__ == "__main__":
    main()