from tkinter import *
from tkinter.messagebox import showinfo
import random
from PIL import Image, ImageTk
import pymysql as sql
import datetime
import DLRenewWindow as dlrw

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
    lst[14].set(valuelist[15])
    lst[15].set(valuelist[16])
    lst[16].set(valuelist[17])

def generateLic(root, lst, valuelist, generate):
    global randomNum, cdate, exdate
    # num = getRandomNumber()
    # randomNum = str(num)
    # if (valuelist[9].lower() == 'kanpur'):
    #     randomNum = 'UP78' + randomNum
    # elif (valuelist[9].lower() == 'unnao'):
    #     randomNum = 'UP77' + randomNum
    # elif (valuelist[9].lower() == 'lucknow'):
    #     randomNum = 'UP32' + randomNum
    # elif (valuelist[9].lower() == 'varanasi'):
    #     randomNum = 'UP65' + randomNum
    # elif (valuelist[9].lower() == 'mathura'):
    #     randomNum = 'UP85' + randomNum
    # else:
    #     randomNum = 'UPIN' + randomNum
    # lst[14].set(str(randomNum))
    # cdate = datetime.datetime.today().date()
    # exdate = datetime.datetime.today().strftime(f"{int(datetime.datetime.today().strftime('%Y')) + 15}-%m-%d")
    cdate=datetime.datetime.today().date()
    exdate=valuelist[17].strftime(f"{int(valuelist[17].strftime('%Y')) + 5}-%m-%d")
    # print(cdate, type(cdate))
    # print(exdate, type(exdate))
    lst[15].set(cdate)
    lst[16].set(exdate)
    generate.configure(state="disabled")

def approveLic(root, aadno):
    print(aadno)
    print(randomNum)
    lst = getCon()
    cur = lst[1]
    # cur.execute(f"update license set dl_no = '{randomNum}' where aadhar_number='{aadno}'")
    cur.execute(f"update license set dl_issuedate = date '{cdate}' where aadhar_number='{aadno}'")
    cur.execute(f"update license set dl_expdate = date '{exdate}' where aadhar_number='{aadno}'")
    cur.execute(f"update renewstatus set dl_ren_status = 'APPROVE' where aadhaar_number='{aadno}'")

    showinfo(title="Message", message="License Renewed")
    lst[0].commit()
    root.destroy()
    dlrw.main(loginusername)

def main(aadno="", uname=""):
    global loginusername
    loginusername = uname
    dlst = getCon()
    cur = dlst[1]
    root = Tk()
    root.title("View Request Window")
    root.state("zoomed")
    root.minsize(1200, 900)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()

    backF = Frame(root)
    backF.place(x=0, y=0, width=w, height=h)
    backimg = ImageTk.PhotoImage(Image.open("backgroundImg.jpg").resize((w, h)))
    imglbl = Label(backF, image=backimg)
    imglbl.place(x=0, y=0)

    # one image as a background has to be added !!
    viewframe = Frame(backF, bg="white", relief=RAISED)  # parent has to be changed from root to background
    viewframe.place(x=300, y=15, width=700, height=h - 80)

    # tuple of columns
    lrn = ('Aadhaar Number', 'Full Name', "Father's Name", 'Date of Birth', 'Gender', 'Mobile Number', 'Blood Group',
           'Address', 'Pincode', 'City', 'State', 'Vehicle Type', 'License Type', 'Test Result', 'DL Number',
           'DL Issue Date', 'DL Expiry Date')

    toplbl = Label(viewframe, text="Details", font="flextitling 22 bold", bg="white", fg="black")
    toplbl.place(x=300, y=0)
    for i in range(len(lrn)):
        lbl = Label(viewframe, text=lrn[i], bg="white", fg='black', font="SeogeUI 13 bold")
        lbl.place(x=10, y=35 + i * 35, width=300, height=30)

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
    dlno = StringVar()
    dlissue = StringVar()
    dlexp = StringVar()

    # Database working---
    valuelist = []
    s = cur.execute(f"select * from license where aadhar_number='{aadno}'")
    if s == 1:
        valuelist = cur.fetchone()
    else:
        showinfo(title="Message", message="Aadhar Number doesn't exist!!")
    print(valuelist)
    # -------------------


    lst = [aadhar, name, fname, dob, gender, phone, bgroup, address, pincode, city, state, vtype, ltype, test, dlno,
           dlissue, dlexp]

    adno = Entry(viewframe, textvariable=aadhar, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    adno.place(x=320, y=35, width=300, height=30)
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
    dlno = Entry(viewframe, textvariable=dlno, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                state="normal")
    dlno.place(x=320, y=525, width=300, height=30)
    dlissue = Entry(viewframe, textvariable=dlissue, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                   state="normal")
    dlissue.place(x=320, y=560, width=300, height=30)
    dlexp = Entry(viewframe, textvariable=dlexp, font="seogeui 13", borderwidth=2, bg="white", relief=SOLID,
                 state="normal")
    dlexp.place(x=320, y=595, width=300, height=30)

    # -----------------------------------------------------
    # -----adding buttons-------

    generate = Button(viewframe, text="Generate", bg="white", fg="black", activeforeground="white",
                      activebackground="black", font="seogeui 14 bold", command=lambda: generateLic(root, lst, valuelist, generate))
    generate.place(x=130, y=635, width=200, height=40)

    approve = Button(viewframe, text="Approve", bg="white", fg="black", activeforeground="white",
                     activebackground="black", font="seogeui 14 bold", command=lambda: approveLic(root, aadno))
    approve.place(x=380, y=635, width=200, height=40)

    setValues(lst, valuelist)
    # ------------------------
    root.mainloop()


if __name__ == "__main__":
    main()