import datetime
from tkinter import *
from tkinter.messagebox import showinfo
import random
from PIL import Image, ImageTk
import pymysql as sql
import datetime as dt
import RCReq as rc

randomNum = ""
cdate = ''
exdate = ''


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
    lst[12].set(valuelist[12])
    lst[13].set(valuelist[13])
    lst[14].set(valuelist[14])
    lst[15].set(valuelist[15])
    lst[16].set(valuelist[16])
    lst[17].set(valuelist[17])
    lst[18].set(valuelist[18])
    lst[19].set(valuelist[19])


def generateRC(root, lst, valuelist, generate):
    global randomNum, cdate, exdate
    # num = getRandomNumber()
    # randomNum = str(num)
    # lst[0].set(str(randomNum))
    cdate = datetime.datetime.today().date()
    exdate = valuelist[17].strftime(f"{int(valuelist[17].strftime('%Y')) + 5}-%m-%d")

    lst[16].set(cdate)
    lst[17].set(exdate)
    generate.configure(state="disabled")


def approveRC(root, adno):
    print(adno)
    print(randomNum)
    lst = getCon()
    cur = lst[1]
    # cur.execute(f"update rc set Registration_no = '{randomNum}' where aadhaar_number='{adno}'")
    cur.execute(f"update rc set issue_date = date '{cdate}' where aadhaar_number='{adno}'")
    cur.execute(f"update rc set expiry_date = date '{exdate}' where aadhaar_number='{adno}'")
    cur.execute(f"update renewstatus set rc_ren_status = 'APPROVE' where aadhaar_number='{adno}'")

    showinfo(title="Message", message="License Approved")
    lst[0].commit()
    root.destroy()
    rc.main(loginusername)


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
    lrn = ('Registration Number','Aadhaar Number', 'Full Name', "Father's Name", 'Date of Birth', 'Mobile Number',
           'Address', 'State', 'City', 'Pincode', 'Manufacturer Name', 'Vehicle Class', 'Engine No', 'Chasis No',
           'Fuel Type', 'Seating Capacity', 'Issue Date', 'Expiry Date', 'Color', 'Vehicle Type')

    toplbl = Label(viewframe, text="Details", font="flextitling 22 bold", bg="white", fg="black")
    toplbl.place(x=300, y=0)
    for i in range(len(lrn)):
        lbl = Label(viewframe, text=lrn[i], bg="white", fg='black', font="seogeui 13 bold bold")
        lbl.place(x=10, y=35 + i * 30, width=300, height=30)

    # Database working---
    valuelist = []
    s = cur.execute(f"select * from rc where aadhaar_number='{aadno}'")
    if s == 1:
        valuelist = cur.fetchone()
    else:
        showinfo(title="Message", message="Aadhar Number doesn't exist!!")
    print(valuelist)
    # -------------------

    # creating entries -------
    regno = StringVar()
    aadhar = StringVar()
    name = StringVar()
    fname = StringVar()
    dob = StringVar()
    phone = StringVar()
    address = StringVar()
    city  = StringVar()
    state = StringVar()
    pincode = StringVar()
    mnfname = StringVar()
    vclass = StringVar()
    engineno = StringVar()
    chasisno = StringVar()
    fueltype = StringVar()
    seatingcap = StringVar()
    issuedate = StringVar()
    expirydate = StringVar()
    color = StringVar()
    vtype = StringVar()

    lst = [regno, aadhar, name, fname, dob, phone, address, city, state, pincode, mnfname, vclass, engineno, chasisno,
           fueltype, seatingcap, issuedate, expirydate, color, vtype]
    reg = Entry(viewframe, textvariable=regno, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                state="readonly")
    reg.place(x=320, y=35, width=300, height=30)
    adno = Entry(viewframe, textvariable=aadhar, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    adno.place(x=320, y=65, width=300, height=30)
    nm = Entry(viewframe, textvariable=name, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
               state="readonly")
    nm.place(x=320, y=95, width=300, height=30)
    father = Entry(viewframe, textvariable=fname, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                   state="readonly")
    father.place(x=320, y=125, width=300, height=30)
    dateob = Entry(viewframe, textvariable=dob, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                   state="readonly")
    dateob.place(x=320, y=155, width=300, height=30)
    ph = Entry(viewframe, textvariable=phone, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                state="readonly")
    ph.place(x=320, y=185, width=300, height=30)
    ad = Entry(viewframe, textvariable=address, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
               state="readonly")
    ad.place(x=320, y=215, width=300, height=30)
    cty = Entry(viewframe, textvariable=city, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    cty.place(x=320, y=245, width=300, height=30)
    st = Entry(viewframe, textvariable=state, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
               state="readonly")
    st.place(x=320, y=275, width=300, height=30)
    pinc = Entry(viewframe, textvariable=pincode, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    pinc.place(x=320, y=305, width=300, height=30)
    mn = Entry(viewframe, textvariable=mnfname, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                state="readonly")
    mn.place(x=320, y=335, width=300, height=30)
    vcl = Entry(viewframe, textvariable=vclass, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
               state="readonly")
    vcl.place(x=320, y=365, width=300, height=30)
    engno = Entry(viewframe, textvariable=engineno, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
               state="readonly")
    engno.place(x=320, y=395, width=300, height=30)
    chno = Entry(viewframe, textvariable=chasisno, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
               state="readonly")
    chno.place(x=320, y=425, width=300, height=30)
    fuel = Entry(viewframe, textvariable=fueltype, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
              state="readonly")
    fuel.place(x=320, y=455, width=300, height=30)
    seat = Entry(viewframe, textvariable=seatingcap, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                state="readonly")
    seat.place(x=320, y=485, width=300, height=30)
    issue = Entry(viewframe, textvariable=issuedate, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                   state="readonly")
    issue.place(x=320, y=515, width=300, height=30)
    exp = Entry(viewframe, textvariable=expirydate, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                 state="readonly")
    exp.place(x=320, y=545, width=300, height=30)
    col = Entry(viewframe, textvariable=color, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                state="readonly")
    col.place(x=320, y=575, width=300, height=30)
    vt = Entry(viewframe, textvariable=vtype, font="seogeui 13 bold", borderwidth=2, bg="white", relief=SOLID,
                state="readonly")
    vt.place(x=320, y=605, width=300, height=30)

    # -----------------------------------------------------
    # -----adding buttons-------
    generate = Button(viewframe, text="Generate", bg="white", fg="black", activeforeground="white",
                      activebackground="black", font="seogeui 14 bold",
                      command=lambda: generateRC(root, lst, valuelist, generate))
    generate.place(x=130, y=640, width=200, height=40)

    approve = Button(viewframe, text="Approve", bg="white", fg="black", activeforeground="white",
                     activebackground="black", font="seogeui 14 bold", command=lambda: approveRC(root, aadno))
    approve.place(x=380, y=640, width=200, height=40)

    setValues(lst, valuelist)
    # ------------------------
    root.mainloop()


if __name__ == "__main__":
    main()