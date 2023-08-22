from tkinter import *
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk
import pymysql as sql

def viewDetails(aadhaar, llstatus, dlstatus, rcstatus, dlrenstatus, rcrenstatus):
    con = sql.connect(host='localhost', user='root', password='', database='minor_project')
    cur = con.cursor()
    s1 = cur.execute(f"select * from status where Aadhar_num = '{aadhaar.get()}'")
    lst = cur.fetchone()

    s2 = cur.execute(f"select * from renewstatus where Aadhaar_number='{aadhaar.get()}'")
    vlst = cur.fetchone()

    if s1 == 1:
        llstatus.set(lst[1])
        dlstatus.set(lst[2])
        rcstatus.set(lst[3])
    if s2 == 1:
        dlrenstatus.set(vlst[1])
        rcrenstatus.set(vlst[2])
    if s1 == 0 and s2 == 0:
        showinfo(title="Message", message="Aadhaar Number doesn't exist")
def main():
    root = Tk()
    root.title("Status Window")
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

    topLabel = Label(TopFrame, text="Status Window", padx=20, pady=40, font=("seogeui 25 bold"), bg="green",
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
    statusFrame = Frame(MainBoard, bg="white", borderwidth=1, relief=SUNKEN)
    statusFrame.place(x=100, y=50, width=1000, height=500)

    adno = Label(statusFrame, text="Aadhaar Number", bg="white", fg="black", font=("seogeui 22 bold"), padx=10, pady=10)
    adno.place(x=100, y=20,width=500, height=40)


    aadhaar = StringVar()
    llstatus = StringVar()
    dlstatus = StringVar()
    rcstatus = StringVar()
    dlrenstatus = StringVar()
    rcrenstatus = StringVar()

    llstatus.set("None")
    dlstatus.set("None")
    rcstatus.set("None")
    dlrenstatus.set("None")
    rcrenstatus.set("None")

    aadno_entry = Entry(statusFrame, textvariable=aadhaar, bg="white", fg="black", font=("seogeui 18"), borderwidth=2, relief=SOLID)
    aadno_entry.place(x=500, y=20, width=300, height=40)

    view = Button(statusFrame, text="View", bg="green", fg="white", font=("consolas 16 bold italic"),borderwidth=2, relief=SOLID, command=lambda : viewDetails(aadhaar, llstatus, dlstatus, rcstatus, dlrenstatus, rcrenstatus), activebackground='white', activeforeground='green')
    view.place(x=500, y=100, width=100, height=50)
    #-------------------
    #status options-----
    lstatus = Label(statusFrame, text="Learner License Status : ", bg='white', fg='black', font="comicsansms 15 bold")
    lstatus.place(x=200, y=180, width=300, height=40)
    dlstat = Label(statusFrame, text="Driving License Status : ", bg='white', fg='black', font="comicsansms 15 bold")
    dlstat.place(x=200, y=230, width=300, height=40)
    rcstat = Label(statusFrame, text="RC Status : ", bg='white', fg='black', font="comicsansms 15 bold")
    rcstat.place(x=200, y=280, width=300, height=40)
    dlren = Label(statusFrame, text="DL Renew Status : ", bg='white', fg='black', font="comicsansms 15 bold")
    dlren.place(x=200, y=330, width=300, height=40)
    rcren = Label(statusFrame, text="RC Renew Status : ", bg='white', fg='black', font="comicsansms 15 bold")
    rcren.place(x=200, y=380, width=300, height=40)

    ls = Entry(statusFrame, textvariable=llstatus, bg='white', fg='black', font="comicsansms 15 bold", state="readonly", readonlybackground="white")
    ls.place(x=500, y=180, width=300, height=40)
    dls = Entry(statusFrame, textvariable=dlstatus, bg='white', fg='black', font="comicsansms 15 bold",state="readonly", readonlybackground="white")
    dls.place(x=500, y=230, width=300, height=40)
    rcs = Entry(statusFrame, textvariable=rcstatus, bg='white', fg='black', font="comicsansms 15 bold", state="readonly", readonlybackground="white")
    rcs.place(x=500, y=280, width=300, height=40)
    dlrs = Entry(statusFrame, textvariable=dlrenstatus, bg='white', fg='black', font="comicsansms 15 bold", state="readonly", readonlybackground="white")
    dlrs.place(x=500, y=330, width=300, height=40)
    rcrs = Entry(statusFrame, textvariable=rcrenstatus, bg='white', fg='black', font="comicsansms 15 bold", state="readonly", readonlybackground="white")
    rcrs.place(x=500, y=380, width=300, height=40)
    #-------------------
    root.mainloop()

if __name__ == "__main__":
    main()