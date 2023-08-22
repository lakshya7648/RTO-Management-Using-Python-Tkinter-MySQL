import datetime
from tkinter import *
from tkinter.messagebox import showinfo
import random
from PIL import Image, ImageTk
import pymysql as sql
import datetime as dt
import LRequestWindow as lrw

randomNum = ""
cdate = ''
exdate=''

def getRandomNumber():
    num = random.randrange(100000, 999999)
    return num

def getCon():
    con = sql.connect(host="localhost", user="root", password="", database="minor_project")
    cur = con.cursor()
    lst = [con, cur]
    return lst

def setValues(lst, valuelist):
    lst[0].set(valuelist[0])
    lst[1].set(valuelist[1])
    lst[2].set(valuelist[2])
    lst[3].set(valuelist[3])
    lst[4].set(valuelist[4])
    lst[5].set(valuelist[5])
    lst[6].set(valuelist[6])
    lst[7].set(valuelist[7])
    lst[8].set(valuelist[8])
    lst[9].set(valuelist[9])
    lst[10].set(valuelist[10])
    lst[11].set(valuelist[11])
    lst[12].set(valuelist[18])
    lst[13].set(valuelist[19])



def generateLic(root, lst, valuelist, generate):
    global randomNum, cdate, exdate
    num = getRandomNumber()
    randomNum = str(num)
    if(valuelist[9].lower() == 'kanpur'):
        randomNum = 'UP78'+randomNum
    elif(valuelist[9].lower() == 'unnao'):
        randomNum='UP77'+randomNum
    elif (valuelist[9].lower() == 'lucknow'):
        randomNum = 'UP32' + randomNum
    elif (valuelist[9].lower() == 'varanasi'):
        randomNum = 'UP65' + randomNum
    elif (valuelist[9].lower() == 'mathura'):
        randomNum = 'UP85' + randomNum
    else:
        randomNum='UPIN'+randomNum
    lst[14].set(str(randomNum))
    cdate=datetime.datetime.today().date()
    exdate=datetime.datetime.today().strftime(f"{int(datetime.datetime.today().strftime('%Y'))+15}-%m-%d")

    lst[15].set(cdate)
    lst[16].set(exdate)
    generate.configure(state="disabled")

def approveLic(root, adno):
    print(adno)
    print(randomNum)
    lst = getCon()
    cur=lst[1]
    cur.execute(f"update license set ll_no = '{randomNum}' where aadhar_number='{adno}'")
    cur.execute(f"update license set ll_issuedate = date '{cdate}' where aadhar_number='{adno}'")
    cur.execute(f"update license set ll_expdate = date '{exdate}' where aadhar_number='{adno}'")
    cur.execute(f"update status set ll_status = 'APPROVE' where aadhar_num='{adno}'")

    showinfo(title="Message", message="License Approved")
    lst[0].commit()
    root.destroy()
    lrw.main(loginusername)


def main(aadno="", uname=""):
    global loginusername
    loginusername=uname
    dlst = getCon()
    cur = dlst[1]

    root = Tk()
    root.title("View Request Window")
    root.state("zoomed")
    root.minsize(1200, 900)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()

    backF = Frame(root)
    backF.place(x=0,y=0, width=w, height=h)
    backimg = ImageTk.PhotoImage(Image.open("backgroundImg.jpg").resize((w, h)))
    imglbl = Label(backF, image=backimg)
    imglbl.place(x=0,y=0)

    # one image as a background has to be added !!
    viewframe = Frame(backF, bg="white", relief=RAISED)  # parent has to be changed from root to background
    viewframe.place(x=300, y=15, width=700, height=h - 80)

    # tuple of columns
    lrn = ('Aadhaar Number', 'Full Name', "Father's Name", 'Date of Birth', 'Gender', 'Mobile Number','Blood Group', 'Address', 'Pincode', 'City', 'State', 'Vehicle Type', 'License Type', 'Test Result', 'LL Number', 'LL Issue Date', 'LL Expiry Date')

    toplbl = Label(viewframe, text="Details", font="flextitling 22 bold", bg="white", fg="black")
    toplbl.place(x=300, y=0)
    for i in range(len(lrn)):
        lbl = Label(viewframe, text=lrn[i], bg="white",fg='black', font="SeogeUI 13 bold")
        lbl.place(x=10, y=35+i*35, width=300, height=30)

# Database working---
    valuelist = []
    s=cur.execute(f"select * from license where aadhar_number='{aadno}'")
    if s == 1:
        valuelist = cur.fetchone()
    else:
        showinfo(title="Message", message="Aadhar Number doesn't exist!!")
    print(valuelist)
# -------------------


    # creating entries -------
    aadhar = StringVar()
    name = StringVar()
    fname = StringVar()
    dob = StringVar()
    gender = StringVar()
    phone = StringVar()
    bgroup = StringVar()
    address = StringVar()
    pincode = StringVar()
    city = StringVar()
    state = StringVar()
    vtype = StringVar()
    ltype = StringVar()
    test = StringVar()
    llno = StringVar()
    llissue = StringVar()
    llexp = StringVar()

    lst = [aadhar, name, fname, dob, gender, bgroup, phone, address, state, city, pincode, vtype, ltype, test, llno, llissue, llexp]
    

    adno = Entry(viewframe, textvariable=aadhar, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID, state = "readonly")
    adno.place(x = 320, y=35, width = 300, height=30)
    nm = Entry(viewframe, textvariable=name, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    nm.place(x=320, y=70, width=300, height=30)
    father = Entry(viewframe, textvariable=fname, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    father.place(x=320, y=105, width=300, height=30)
    dateob = Entry(viewframe, textvariable=dob, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    dateob.place(x=320, y=140, width=300, height=30)
    gen = Entry(viewframe, textvariable=gender, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    gen.place(x=320, y=175, width=300, height=30)
    ph = Entry(viewframe, textvariable=phone, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    ph.place(x=320, y=210, width=300, height=30)
    bgrp = Entry(viewframe, textvariable=bgroup, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    bgrp.place(x=320, y=245, width=300, height=30)
    ad = Entry(viewframe, textvariable=address, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    ad.place(x=320, y=280, width=300, height=30)
    pinc = Entry(viewframe, textvariable=pincode, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    pinc.place(x=320, y=315, width=300, height=30)
    cty = Entry(viewframe, textvariable=city, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    cty.place(x=320, y=350, width=300, height=30)
    st = Entry(viewframe, textvariable=state, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    st.place(x=320, y=385, width=300, height=30)
    vt = Entry(viewframe, textvariable=vtype, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    vt.place(x=320, y=420, width=300, height=30)
    lt = Entry(viewframe, textvariable=ltype, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    lt.place(x=320, y=455, width=300, height=30)
    t = Entry(viewframe, textvariable=test, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    t.place(x=320, y=490, width=300, height=30)
    lno = Entry(viewframe, textvariable=llno, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    lno.place(x=320, y=525, width=300, height=30)
    lissue = Entry(viewframe, textvariable=llissue, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    lissue.place(x=320, y=560, width=300, height=30)
    lexp = Entry(viewframe, textvariable=llexp, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    lexp.place(x=320, y=595, width=300, height=30)

# -----------------------------------------------------
    # -----adding buttons-------
    generate = Button(viewframe, text="Generate", bg="white", fg="black", activeforeground="white", activebackground="black", font="seogeui 14 bold",command=lambda:generateLic(root, lst, valuelist, generate))
    generate.place(x=130, y=635, width=200, height=40)

    approve = Button(viewframe, text="Approve", bg="white", fg="black", activeforeground="white",
                      activebackground="black", font="seogeui 14 bold", command=lambda:approveLic(root, aadno))
    approve.place(x=380, y=635, width=200, height=40)

    setValues(lst, valuelist)
    # ------------------------
    root.mainloop()

if __name__ == "__main__":
    main()