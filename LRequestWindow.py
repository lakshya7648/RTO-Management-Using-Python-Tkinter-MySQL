from tkinter import *
import pymysql as sql
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk
import LicenseReq as lr
import ViewLearnerReq

def backfun(root):
    root.destroy()
    lr.main(loginusername)

def openConnection():
    con = sql.connect(host="localhost", user="root", password="", database="minor_project")
    cur = con.cursor()
    return cur


def viewDet(root, val):
    # print(val.__getattribute__("adno"))
    # print(val)
    root.destroy()
    # # Toplevel(ViewLearnerReq.main()
    ViewLearnerReq.main(val, loginusername)

def main(uname=""):
    global loginusername
    loginusername = uname
    root = Tk()
    root.title("View Requests")
    root.state("zoomed")
    root.minsize(1200, 900)
    showinfo(title="Records Fetched", message="Records of Requests Fetched")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
# -----------Top Part----------------
    TopFrame = Frame(root)
    TopFrame.place(x=0, y=0, width=w, height=100)

    img = Image.open("rtoimage.png")
    rimg = img.resize((100, 100))
    img1 = ImageTk.PhotoImage(rimg)

    PhotoLabel = Label(TopFrame, image=img1)
    PhotoLabel.place(x=0, y=0, width=100, height=100)

    topLabel = Label(TopFrame, text="Request Pending for Approval of Learner License", padx=20, pady=40, font=("seogeui 25 bold"), bg="blue",
                     fg="white")
    topLabel.place(x=100, y=0, width=w - 100, height=100)
# -------------------------------------------------------------
# -------------Main Board--------------------------
    MainBoard = Frame(root, bg="#A6B4F7")
    MainBoard.place(x=0, y=100, width=w, height=h - 100)

    image = Image.open("brto.jpg")
    resize_image = image.resize((w, MainBoard.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)

    lbl = Label(MainBoard, image=img)
    lbl.place(x=0, y=0, width=w, height=MainBoard.winfo_screenheight())
# -------------------------------------------------
    cur = openConnection()
    cur.execute("select Aadhar_number, Name, Mobile_num from license, status where license.Aadhar_number=status.Aadhar_num and status.ll_status='PENDING'")
    lst = cur.fetchall()
    head = ('Aadhar Number', 'Name', 'Mob No', 'Option')
# ------------Creating a Parent Frame for table to reside -------------
    ParentFrame = Frame(MainBoard, bg="#F0EEEE")
    ParentFrame.place(x=100, y=30, width=1000, height=500)
    for k in range(len(head)):
        var = StringVar()
        e = Entry(ParentFrame, textvariable=var, borderwidth=2, relief=SOLID, state="readonly", bg="red", fg="black", font=("seogeui 14 bold"))
        e.place(x=0 + k*250, y=0, width=250, height=30)
        var.set(head[k])

    btn = []
    for i in range(len(lst)): # rows
        for j in range(4): # columns
            if j < 3:
                var = StringVar()
                e = Entry(ParentFrame, textvariable=var, borderwidth=2, relief=SOLID, state="readonly", fg="black", font=("seogeui 13"))
                e.place(x=0 + 250*j, y=30+i*30, width=250, height=30)
                var.set(lst[i][j])
            if j == 3:
                # print(i)
                row=i;
                openbtn = btn.append(Button(ParentFrame, text="View", textvariable=lst[i][0],bg="blue", fg="white", font="SeogeUI 13 bold italic", command=lambda var = lst[i][0]:viewDet(root, var)))
                btn[i].place(x=750, y=30 + i * 30, width=250, height=30)

    back = Button(MainBoard, text="Back", bg="white", fg="red", font=("consolas 20 bold"), activebackground="red",
                  activeforeground="white", borderwidth=2, relief=SOLID, takefocus="red", command=lambda: backfun(root))
    back.place(x=650, y=540, width=160, height=50)


    root.mainloop()

if __name__ =="__main__":
    main()
