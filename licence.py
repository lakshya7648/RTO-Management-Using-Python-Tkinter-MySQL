from tkinter import *
from tkinter import messagebox
import say
import services as ser
import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
import services as ser
from tkinter import messagebox
import say as s
import pymysql as sql
import datetime
from PIL import Image,ImageTk


def rect_win():
    pass

def cancel1(root):
    s.speak("A FILE has been downloaded for the customer as RC document")
    messagebox.showinfo("information", "Ensure That you have Printed The Generated RC_Document!!")
    choice_screen.destroy()
    root.destroy()
    ser.options()

def fetch():
    global ll
    ll= ah.get()
    print(ll)
    conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
    cur = conn.cursor()

    qry13 = "select DL_status from status where Aadhar_num='{0}'".format(ll)
    ck=cur.execute(qry13)
    data3 = cur.fetchall()
    for row in data3:
        for col in row:
            if col=='APPROVE':
                qry1 = "update license set License_type='Permanent License' where Aadhar_number='{0}'".format(ll)
                cur.execute(qry1)

                


    print(data3)







    #qry="select * from status where Aadhar_num='{0}'and DL_status='{1}' or LL_status='{2}'".format(ll,'APPROVED','APPROVED')
    qry = "select Aadhar_num from status where DL_status='{0}' or LL_status='{1}'".format('APPROVE','APPROVE')
    cur = conn.cursor()
    c=cur.execute(qry)
    #print(c)
    c1=0
    data2 = cur.fetchall()
    for row in data2:
        for col in row:
            if ll==col:
                print("THis to Print")
                c1=1
                break
            else:
                print("not allowed")
        #print(row)
    conn.commit()
    conn.close()

    if c1==1:
        main()
    else:
        messagebox.showerror("error", "Documnet not Found!!")
        say.speak("sorry!!Document Approval Pending!!")
        choice_screen.destroy()
        ser.options()



def cancel1(root):
    s.speak("A FILE has been downloaded for the customer as License document please wait opening")
    messagebox.showinfo("information", "OPENING THE FILE !!Ensure That you have Printed The Generated License_Document Before Closing it !!")
    choice_screen.destroy()
    root.destroy()

    import subprocess
    path = "DL_download.pdf"
    subprocess.Popen([path], shell="True")

    ser.options()



class InvoiceGenerator:
    def __init__(self,root):
        self.root = root
        self.root.title("DL_document GENeration by RTO")
        self.root.geometry("1700x1000")
        self.frame = Frame(self.root, bg="lightblue")
        self.frame.place(x=0, y=0, width=1700, height=700)


        # get the details from the table LC_master
        global Fullname,father,dob,aadhar,gender,mob,address,city,state,vehicle,blood,result,pin,lictype,lstgot,lstin,dlno,dlid,lled
        '''lst = ['Full Name', "Father's Name", 'Date-Of-Birth', 'Aadhar No.', 'Registration Number', 'Fuel type',
               'Address', 'City', 'State', 'Pin', 'Vehicle Type', 'Engine Number', 'Chasis Number', 'Manufacturer Name',
               'Colour', 'Vehicle Class', 'Seating Capacity', 'Issue Date', 'Expiray Date']'''

        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select * from license where Aadhar_number='{0}'".format(ll)
        print(qry)
        cur = conn.cursor()
        cur.execute(qry)
        global data
        data = cur.fetchone()
        conn.close()

        lstgot=[]
        for i in range(0,20):
            plus = data[i]
            lstgot.append(plus)
            #if i==12 or i==13 or i==14 or i==19:
            #if data[i]==None:
               # continue
            #else:
                #plus=data[i]
                #lstgot.append(plus)


        '''Fullname = "ADITYA SHARMA"
        father = "Kamal Narain Sharma"
        dob = "20-16-1947"
        aadhar ="515426121"
        #fuel =
        #mob =
        address ="133/1616"
        city ="Kanpur"
        #state =
        lstin=[]'''
        #lstgot = [Fullname, father, dob, aadhar, address, city]
        print(lstgot)
        print(ll)




        '''pin=
        vehicle=
        engine =
        chasis=
        manufacturer=
        colour=
        vehicleclass=
        seat='''

        # ====submit details
        Button(self.frame, text="CLICK TO GENERATE PDF..(one click only)", command=self.generate_invoice(), font=("times new roman", 24),
               fg="white", cursor="hand2", bg="#B00857").place(x=300, y=300, width=700, height=150)


        button1 = Button(root, text="DONE!",cursor="hand2", command=lambda: cancel1(root), width="30", height="1",
                         font=("Comic Sans MS", 15, "bold"),
                         bg="red", fg="white",bd="5")
        button1.place(x="800", y="650")




# ==== Invoice Generation Function
    def generate_invoice(self):
        c = canvas.Canvas("DL_download.pdf", pagesize=(200, 250), bottomup=0)
        c.setFillColorRGB(0.8, 0.5, 0.7)

        # background watermark
        img_file = "Images\\png_20230215_193432_0000.png"
        x1 = 10
        y1 = 55
        c.drawImage(img_file, x1, y1, width=180, height=180, preserveAspectRatio=False)



        c.line(20, 22, 180, 22)#above 1 line
        c.line(5, 45, 195, 45)# above 2 line
        #c.line(55, 120, 185, 120)
        c.line(35, 45, 35,220)# left margin line
        #c.line(115, 108, 115, 220)
        #c.line(135, 108, 135, 220)
        #c.line(160, 108, 160, 220)
        c.line(15, 220, 185, 220)# bottom line

        #left Emblem
        img_file = "Images\\india-clipart-emblem-17 (3).png"
        x1 = 5
        y1 = 10
        c.drawImage(img_file, x1, y1, width=25, height=30, preserveAspectRatio=False)

        #right emblem
        img_file = "Images\\india-clipart-emblem-17 (3).png"
        x1 = 170
        y1 = 10
        c.drawImage(img_file, x1, y1, width=25, height=30, preserveAspectRatio=False)

        #signature emblem
        img_fileb = "Images\\india-clipart-emblem-17 (3) - Copy.png"
        x1 = 160
        y1 = 222
        c.drawImage(img_fileb, x1, y1, width=10, height=10, preserveAspectRatio=False)

        c.translate(10, 40)
        c.scale(1, -1)
        # c.drawImage(self.file_name, 0, 0, width=50, height=30)

        c.scale(1, -1)
        c.translate(-10, -40)

        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 20, "REGIONAL TRANSPORT OFFICE")

        c.setFont("Times-Bold", 5)
        c.setFillColorRGB(0, 0, 0.9)
        typ=data[18]
        print(typ)
        c.drawCentredString(100, 30, typ+" Issued by Government")
        c.drawCentredString(100, 35, data[9] + ", India")
        c.setFont("Times-Bold", 3)
        c.drawString(10, 230, "This is system generated RC_Document!")
        # c.drawRightString(180, 228, self.aus.get())
        td= datetime.datetime.today().strftime("%d-%m-%Y")
        tdt= datetime.datetime.today().strftime("%H:%M:%S %p")
        print(td,tdt)
        c.drawString(10,235,td)
        c.drawString(10,240,tdt)
        c.drawRightString(180, 235, "RTO Authority Signature")

        lst=['Aadhar Number','Full Name',"Father's Name",'D.O.B','Gender','Blood Group','Mobile No.','Address','State','City','Pincode','Vehicle Type','LL_no','LL_issueDate','LL_expiryDate','DL_no.','DL_issue date','DL_expiry date','Lisence Type']
        c.setFont("Times-Bold", 7)
        #c.setFillColorRGB(0.8, 0, 0)
        c.setFillColorRGB(0.9, 0, 0)
        y=55
        p=55
        for i in range(1,20):# loop to generate serial numbers and lines and headings
            c.drawCentredString(20, int(y), str(i)+".")
            #c.line(5, int(y+1),195, int(y+1))
            c.drawString(40, int(y), (lst[i-1]+"-").ljust(10))
            #c.drawString(40, int(y), (lst[i - 1] + "-  "))
            y=y+8

        c.setFillColorRGB(0.0,0.0,0.0)
        c.setFont("Courier", 6)
        for j in range(1,20):
            #c.drawString(130, int(p), (lstgot[j-1]).ljust(10))
            if j==4 or j==14 or j==15 or j==17 or j==18:

                if data[j - 1] == None:
                    c.drawString(130, int(p), 'None')
                    p = p + 8
                else:
                    t=lstgot[j - 1]
                    print(t)
                    tt=t.strftime('%d/%m/%Y')
                    print(tt)
                    c.drawString(130, int(p), tt)
                    p = p + 8

            elif data[j-1]==None:
                c.drawString(130, int(p), 'None')
                p = p + 8
            else:
                c.drawString(130, int(p), (lstgot[j - 1]))
                p = p + 8





        '''c.drawCentredString(20, 65, '1-')
        c.drawCentredString(20, 75, '2-')
        c.drawCentredString(20, 85, '3-')'''







        c.showPage()
        c.save()












# ==== creating main function
def main():

    # ==== create tkinter window
    root = Tk()
    # === creating object for class InvoiceGenerator
    obj = InvoiceGenerator(root)
    # ==== start the gui

    root.mainloop()






# addd print Document file???


def disp_win():
    root = Toplevel(choice_screen)
    # choice_screen.destroy()
    #root.geometry("1700x1000")
    root.config(bg="lightgreen")

    # image code
    l=root
    image = Image.open("Images\\rto.jpg")
    resize_image = image.resize((l.winfo_screenwidth(), l.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    l.geometry("1700x1000")
    lbl = Label(l, image=img)
    lbl.place(x=0, y=0)

    root.title("New DRIVING LICENSE")
    title = Label(root, text="🏍 Preview And Download LICENSE Document 🏍", font=("Georgia", 45, "bold"), pady="5",
                  bg="black",
                  fg="white").pack(pady="50")

    global ah
    ah = StringVar()
    say.speak("Require Adhharcard number of Applicant")
    label_1 = Label(root, text="Aadhar Number*👇", width=30, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_1.place(x=500, y=250)
    entry_1 = Entry(root, cursor="hand2", textvar=ah, width=30, borderwidth=7, font=("Calibri", 20, "bold"),highlightcolor="red",highlightthickness="4")
    entry_1.place(x=500, y=300)
    button1 = Button(root, cursor="hand2", text="Show Details", command=lambda: fetch(), width="20", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="brown", fg="white", bd="5")
    button1.place(x="600", y="400")

    root.mainloop()



def details():
    messagebox.showinfo("information", "Please Wait !!!Loading Data From The Database....")
    lln=ll.get()
    print(lln)

    conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
    qry = "select * from license where Aadhar_number='{0}'".format(lln)
    cur = conn.cursor()
    cur.execute(qry)
    data=cur.fetchone()

    print(data)


    conn.close()

    # get details from database and state=readonly




    root = Toplevel(choice_screen)
    root.geometry("1700x1000")
    root.config(bg="lightyellow")
    root.title("VERIFICATION PAGE")
    title = Label(root, text="🚍 'REGIONAL TRANSPORT OFFICE' Customer Verification Page", font=("Georgia", 30, "bold"), pady="5",
                  bg="green",
                  fg="yellow").pack(pady="50")

    Fullname = StringVar()
    father = StringVar()
    dob = StringVar()
    aadhar = StringVar()
    gender = StringVar()
    mob = StringVar()
    address = StringVar()
    city = StringVar()
    state = StringVar()
    vehicle = StringVar()
    blood = StringVar()
    result = StringVar()
    pin = StringVar()
    lictype=StringVar()

    # TO SET VALUES AS READONLY
    a = data[1]
    Fullname.set(a)
    a = data[2]
    father.set(a)
    a = data[3]
    dob.set(a)
    a = data[0]
    aadhar.set(a)
    a = data[4]
    gender .set(a)
    a = data[6]
    mob .set(a)
    a = data[7]
    address.set(a)
    a = data[9]
    city .set(a)
    a = data[8]
    state .set(a)
    a = data[11]
    vehicle .set(a)
    a = data[5]
    blood .set(a)
    a = data[19]
    result .set(a)
    a = data[10]
    pin .set(a)
    a = data[18]
    lictype .set(a)

    label_1 = Label(root, text="FullName👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_1.place(x=80, y=160)

    entry_1 = Entry(root,cursor="hand2", textvar=Fullname, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_1.place(x=320, y=160)


    label_2 = Label(root, text="Father's Name👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_2.place(x=68, y=210)

    entry_2 = Entry(root,cursor="hand2", textvar=father, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_2.place(x=320, y=210)

    label_3 = Label(root, text="Gender👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_3.place(x=70, y=260)

    '''entry_3 = Entry(root, textvar=gender, width=26, borderwidth=3, font=("Calibri", 15, "italic"), state="readonly",highlightcolor="black",highlightthickness="4")
    entry_3.place(x=320, y=260)'''

    Radiobutton(root,cursor="hand2", text="Male", padx=20, variable=gender, value=1,font=("Calibri", 15, 'italic'), bg="lightyellow",state="disabled").place(x=320, y=260)
    Radiobutton(root,cursor="hand2", text="Female", padx=20, variable=gender, value=2,font=("Calibri", 15, 'italic'),bg="lightyellow",state="disabled").place(x=415, y=260)
    Radiobutton(root,cursor="hand2", text="Others", padx=20, variable=gender, value=3,font=("Calibri", 15, 'italic'), bg="lightyellow",state="disabled").place(x=520, y=260)

    gender.set(1)# to disable and set a particular text # use this....imp...

    label_4 = Label(root, text="Vehicle type👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_4.place(x=70, y=310)

    list1 = ['Light Motor Vehicle', 'Medium Goods Vehicle', 'Medium Passenger Motor Vehicle', 'Heavy Goods Vehicle',
             'Heavy Passenger Vehicle', 'AutoRikshaw/Van', 'Tractor', 'MotorCycle', 'Electronic Vehicle'];

    droplist = OptionMenu(root, vehicle, *list1)
    droplist.config(width=26,cursor="hand2", borderwidth=3, font=("Calibri", 15, "italic"),state="disabled")
    #vehicle.set('None')
    droplist.place(x=320, y=310)

    label_5 = Label(root, text="Aadhar Number*👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_5.place(x=65, y=360)
    entry_5 = Entry(root,cursor="hand2", textvar=aadhar, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_5.place(x=320, y=360)

    label_6 = Label(root, text="D.O.B(yyyy-mm-dd)👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_6.place(x=50, y=410)
    entry_6 = Entry(root,cursor="hand2", textvar=dob, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_6.place(x=320, y=410)

    label_7 = Label(root, text="Mob no👉", width=20, bg="lightyellow", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_7.place(x=70, y=460)
    entry_7 = Entry(root,cursor="hand2", textvar=mob, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_7.place(x=320, y=460)

    # +50 IN Y

    label_8 = Label(root, text="Address👉", width=20, bg="lightyellow", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_8.place(x=780, y=160)
    entry_8 = Entry(root,cursor="hand2", textvar=address, width=30, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_8.place(x=1000, y=160)

    label_8 = Label(root, text="City👉", width=20, bg="lightyellow", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_8.place(x=800, y=240)
    entry_8 = Entry(root,cursor="hand2", textvar=city, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_8.place(x=1000, y=240)

    label_9 = Label(root, text="State👉", width=20, bg="lightyellow", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_9.place(x=800, y=300)
    entry_9 = Entry(root,cursor="hand2", textvar=state, width=26, borderwidth=3, font=("Calibri", 15, "italic"), state="readonly",highlightcolor="black",highlightthickness="4")
    entry_9.place(x=1000, y=300)
    state.set("UTTAR PRADESH")

    label_10 = Label(root, text="Blood Group 👉", width=20, bg="lightyellow", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_10.place(x=750, y=350)
    entry_10 = Entry(root,cursor="hand2", textvar=blood, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_10.place(x=1000, y=350)

    '''label_11 = Label(root, text="Blood Group 👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_11.place(x=800, y=360)
    entry_11 = Entry(root, textvar=blood, width=26, borderwidth=3, font=("Calibri", 15, "italic"))
    entry_11.place(x=1000, y=360)'''

    label_12 = Label(root, text="Test Result👉", width=20, bg="lightyellow", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_12.place(x=750, y=410)
    entry_12 = Entry(root,cursor="hand2", textvar=result, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_12.place(x=1000, y=410)

    label_13 = Label(root, text="PIN CODE👉", width=20, bg="lightyellow", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_13.place(x=750, y=460)
    entry_13 = Entry(root,cursor="hand2", textvar=pin, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_13.place(x=1000, y=460)

    label_14 = Label(root, text="License type👉", width=20, bg="lightyellow", fg="red", font=("Calibri", 20, 'bold'))
    label_14.place(x=750, y=460)
    list2 = ['Permanent License', 'Learning License'];

    droplist = OptionMenu(root, lictype, *list2)
    droplist.config(width=26,cursor="hand2", borderwidth=3, font=("Calibri", 15, "italic"), state="disabled",highlightcolor="black",highlightthickness="4")
    lictype.set('Permanent License')
    droplist.place(x=1000, y=460)

    button2 = Button(root,cursor="hand2", text="Apply For Generation", command=lambda: ok(), width="30", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="red", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button2.place(x="550", y="650")




    root.mainloop()

def ok():
    conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
    cur = conn.cursor()
    # updation in the Updation table to be done
    lln=ll.get()
    print(lln)

    # EXTRA PART STARTS
    qryt = "select Aadhar_num from status"
    cur.execute(qryt)
    datat = cur.fetchall()
    c1 = 0
    for row in datat:
        for col in row:
            if lln == col:
                print("THis to Update")
                c1 = 1
                break
        # print(row)
    if c1 == 1:
        qry12 = "update status set DL_status='PENDING' where Aadhar_num='{0}'".format(lln)
        cur.execute(qry12)
        # EXTRA PART ENDS


    #qry="update status set DL_status='PENDING' where Aadhar_num='{0}'".format(lln)
    '''qry1="update license set License_type='Permanent License' where Aadhar_number='{0}'".format(lln)

    #cur.execute(qry)
    cur.execute(qry1)'''

    conn.commit()
    conn.close()
    print("DATA SEND FOR REQUEST.. Successfully")
    messagebox.showinfo("information", "REQUEST SEND Successfully!!")
    say.speak(" RTO will reply to APPLICANT in 7 days, a message has been send")
    choice_screen.destroy()
    ser.options()


def data():
    res=result.get()
    veh=vehicle.get()
    fthr=father.get()
    ahr=aadhar.get()
    gen=gender.get()
    nam=Fullname.get()
    birth=dob.get()
    mb=mob.get()
    add=address.get()
    cty=city.get()
    sta=state.get()
    bld=blood.get()
    pn=pin.get()
    lcty=lictype.get()
    print(lcty)

    print("client name=", nam)
    print("father name=", fthr)
    print("vehicle type=", veh)
    print("Result=",res)
    print("aadhar=",ahr)
    if gen== '1':
        k="Male"
    elif gen== '2':
        k="Female"
    else:
        k="Others"
    print("gender=",k)

    conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
    qry = "insert into license values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}',{12},{13},{14},{15},{16},{17},'{18}','{19}')".format(ahr,nam,fthr,birth,k,bld,mb,add,sta,cty,pn,veh, 'null' ,'null','null','null','null','null',lcty,res)
    #qry = "insert into license values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{}','{}','{}','{}','{}','{}','{12}','{13}')".format(ahr, nam, fthr, birth, k, bld, mb, add, sta, cty, pn, veh,lcty,res)
    cur = conn.cursor()
    cur.execute(qry)
    # updation in the Updation table to be done

    # EXTRA PART STARTS
    qryt = "select Aadhar_num from status"
    cur.execute(qryt)
    datat = cur.fetchall()
    c1 = 0
    for row in datat:
        for col in row:
            if ahr == col:
                print("THis to Update")
                c1 = 1
                break
        # print(row)
    if c1 == 1:
        qry1 = "update status set LL_status='PENDING' where Aadhar_num='{0}'".format(ahr)
        cur.execute(qry1)
        conn.commit()
        conn.close()
    else:
        qry1 = "insert into status values('{0}','{1}',{2},{3})".format(ahr, 'PENDING', 'null', 'null')
        cur.execute(qry1)
        conn.commit()
        conn.close()
    # EXTRA PART ENDS



    '''qry1 = "insert into status values('{0}','{1}',{2},{3})".format(ahr, 'PENDING','null','null')
    cur.execute(qry1)
    conn.commit()
    conn.close()'''



    print("DATA ENTERED.. Successfully AND STATUS CHANGED")


    messagebox.showinfo("information", "REQUEST SEND Successfully!!")
    # popup for successful registration???
    say.speak(" RTO will reply to APPLICANT in 7 days, a message has been send")
    root.destroy()
    choice_screen.destroy()
    ser.options()




def clear():
    root.destroy()
    learner_win()
    '''Fullname.set("")
    father.set("")
    dob.set("")
    aadhar.set(0)
    vehicle.set('NONE')
    gender.set(0)
    mob.set(0)
    address.set("")
    city.set("")
    state.set("")
    vehicle.set("")
    blood.set("")
    result.set("")
    pin.set(0)'''




def cancel():
    root.destroy()
    choice_screen.destroy()
    ser.options()
    # call another import for generation or telling???

def newdl_win():
    say.speak("REQUIRE AdhharCard  NUMBER OF APPLICANT..")
    root = Toplevel(choice_screen)
    #root.geometry("1700x1000")
    root.config(bg="lightgreen")
    # image code
    image = Image.open("Images\\rto.jpg")
    resize_image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    root.geometry("1700x1000")
    lbl = Label(root, image=img)
    lbl.place(x=0, y=0)

    root.title("New DRIVING LICENSE")
    title = Label(root, text="🏍 Request For DRIVING LICENSE 🏍", font=("Georgia", 45, "bold"), pady="5",
                  bg="black",
                  fg="white",width="100",height="1").pack(pady="50")
    global ll
    ll =StringVar()
    label_1 = Label(root, text="Aadhar Number*👇", width=30, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_1.place(x=500, y=250)
    entry_1 = Entry(root,cursor="hand2", textvar=ll, width=30, borderwidth=7, font=("Calibri", 20, "bold"),highlightcolor="red",highlightthickness="4")
    entry_1.place(x=500, y=300)
    button1 = Button(root,cursor="hand2", text="Show Details", command=lambda: details(), width="20", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="brown", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="600", y="400")



    root.mainloop()






def learner_win():
    say.speak("REQUIRE DETAILS OF APPLICANT..")
    global root
    root = Toplevel(choice_screen)

    w2 = 350
    h2 = 250
    #root.geometry("%dx%d+%d+%d" % (w2, h2, x, y))
    #root.geometry("1700x1000")
    root.config(bg="lightgreen")

    # image code
    image = Image.open("Images\\license.jpg")
    resize_image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    root.geometry("1700x1000")
    lbl = Label(root, image=img)
    lbl.place(x=0, y=0)


    root.title("Application Form For Learner License......")
    # Login Title
    title = Label(root, text="Application Form For LEARNER LICENSE", font=("Georgia", 45, "bold"), pady="5", bg="black",
                  fg="red").pack(pady="50")
    login_frame = Frame(root, width="1500", height="1000", bg="lightblue")
    login_frame.place(x="10", y="150")

    global Fullname,father,dob,aadhar,gender,mob,address,city,state,vehicle,blood,result,pin,lictype


    Fullname = StringVar()
    father= StringVar()
    dob= StringVar()
    aadhar= StringVar()
    gender= StringVar()
    mob= StringVar()
    address= StringVar()
    city= StringVar()
    state= StringVar()
    vehicle= StringVar()
    blood= StringVar()
    result=StringVar()
    pin= StringVar()
    lictype=StringVar()



    Email = StringVar()
    var = IntVar()
    c = StringVar()
    var1 = IntVar()


    label_1 = Label(root, text="FullName👉", width=20,bg="lightblue",fg="red",font=("Calibri", 20, 'bold'))
    label_1.place(x=80, y=160)

    entry_1 = Entry(root,cursor="hand2", textvar=Fullname, width=26, borderwidth=3,font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_1.place(x=320, y=160)

    label_2 = Label(root, text="Father's Name👉",width=20,bg="lightblue",fg="red",font=("Calibri", 20, 'bold'))
    label_2.place(x=68, y=210)

    entry_2 = Entry(root,cursor="hand2", textvar=father, width=26, borderwidth=3,font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_2.place(x=320, y=210)


    label_3 = Label(root, text="Gender👉",width=20,bg="lightblue",fg="red",font=("Calibri", 20, 'bold'))
    label_3.place(x=70, y=260)

    Radiobutton(root,cursor="hand2", text="Male", padx=5, variable=gender,value=1,font=("Calibri", 15, 'italic'),bg="lightblue",highlightcolor="black",highlightthickness="4").place(x=320, y=260)
    Radiobutton(root,cursor="hand2", text="Female", padx=20, variable=gender,value=2,font=("Calibri", 15, 'italic'),bg="lightblue",highlightcolor="black",highlightthickness="4").place(x=417, y=260)
    Radiobutton(root,cursor="hand2", text="Others", padx=20, variable=gender,value=3,font=("Calibri", 15, 'italic'),bg="lightblue",highlightcolor="black",highlightthickness="4").place(x=520, y=260)

    label_4 = Label(root, text="Vehicle type👉",width=20,bg="lightblue",fg="red",font=("Calibri", 20, 'bold'))
    label_4.place(x=70, y=310)

    list1 = ['Light Motor Vehicle', 'Medium Goods Vehicle', 'Medium Passenger Motor Vehicle', 'Heavy Goods Vehicle', 'Heavy Passenger Vehicle', 'AutoRikshaw/Van','Tractor','MotorCycle','Electronic Vehicle'];

    droplist = OptionMenu(root, vehicle, *list1)
    droplist.config(width=26,cursor="hand2", borderwidth=3,font=("Calibri", 15, "italic"))
    vehicle.set('None')
    droplist.place(x=320, y=310)

    label_5 = Label(root, text="Aadhar Number*👉", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_5.place(x=65, y=360)
    entry_5 = Entry(root,cursor="hand2", textvar=aadhar, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_5.place(x=320, y=360)

    label_6 = Label(root, text="D.O.B(yyyy-mm-dd)👉", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_6.place(x=50, y=410)
    entry_6 = Entry(root,cursor="hand2", textvar=dob, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_6.place(x=320, y=410)

    label_7 = Label(root, text="Mob no👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_7.place(x=70, y=460)
    entry_7 = Entry(root,cursor="hand2", textvar=mob, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_7.place(x=320, y=460)

  #+50 IN Y

    label_8 = Label(root, text="Address👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_8.place(x=780, y=160)
    entry_8 = Entry(root,cursor="hand2", textvar=address, width=30, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_8.place(x=1000, y=160)

    label_8 = Label(root, text="City👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_8.place(x=800, y=240)
    entry_8 = Entry(root,cursor="hand2", textvar=city, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_8.place(x=1000, y=240)

    label_9 = Label(root, text="State👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_9.place(x=800, y=300)
    entry_9 = Entry(root,cursor="hand2", textvar=state, width=26, borderwidth=3, font=("Calibri", 15, "italic"),state="readonly",highlightcolor="black",highlightthickness="4")
    entry_9.place(x=1000, y=300)
    state.set("UTTAR PRADESH")

    label_10 = Label(root, text="Blood Group 👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_10.place(x=750, y=350)
    entry_10 = Entry(root,cursor="hand2", textvar=blood, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_10.place(x=1000, y=350)

    '''label_11 = Label(root, text="Blood Group 👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_11.place(x=800, y=360)
    entry_11 = Entry(root, textvar=blood, width=26, borderwidth=3, font=("Calibri", 15, "italic"))
    entry_11.place(x=1000, y=360)'''

    label_12 = Label(root, text="Test Result👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_12.place(x=750, y=410)
    entry_12 = Entry(root,cursor="hand2", textvar=result, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_12.place(x=1000, y=410)

    label_13 = Label(root, text="PIN CODE👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_13.place(x=750, y=460)
    entry_13 = Entry(root,cursor="hand2", textvar=pin, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_13.place(x=1000, y=460)

    label_14 = Label(root,cursor="hand2", text="License type👉", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_14.place(x=750, y=510)
    list2 = ['Permanent License', 'Learning License'];

    droplist = OptionMenu(root, lictype, *list2)
    droplist.config(width=26,cursor="hand2", borderwidth=3, font=("Calibri", 15, "italic"),state="disabled",highlightcolor="black",highlightthickness="4")
    lictype.set('Learning License')
    droplist.place(x=1000, y=510)



    button1 = Button(root,cursor="hand2", text="Submit?", command=lambda: data(), width="30", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="brown", fg="white",bd="5")
    button1.place(x="80", y="650")

    button2 = Button(root,cursor="hand2", text="Cancel!!!", command=lambda: cancel(), width="30", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="red", fg="white",bd="5")
    button2.place(x="550", y="650")

    button3 = Button(root,cursor="hand2", text="Clear All", command=lambda: clear(), width="30", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="orange", fg="white",bd="5")
    button3.place(x="1000", y="645")

    '''label_4 = Label(root, text="Programming", width=20, font=("bold", 10),bg="lightblue",fg="red")
    label_4.place(x=85, y=360)
    var2 = IntVar()
    Checkbutton(root, text="java", variable=var1).place(x=235, y=360)

    Checkbutton(root, text="python", variable=var2).place(x=290, y=360)'''



    root.mainloop()


def lw():

    global choice_screen, screen_w, screen_h, x, y
    choice_screen = Tk()  # create a GUI window
    choice_screen["bg"] = 'lightgreen'
    choice_screen.title("RTO- licence ")  # set the title of GUI window
    screen_w = choice_screen.winfo_screenwidth()
    screen_h = choice_screen.winfo_screenheight()
    w = 350
    h = 200
    x = screen_w / 2.7
    y = screen_h / 2.7
    #choice_screen.geometry("%dx%d+%d+%d" % (w, h, x, y))
    choice_screen.geometry("1700x1000")

    # image code
    image = Image.open("Images\\license.jpg")
    resize_image = image.resize((choice_screen.winfo_screenwidth(), choice_screen.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    choice_screen.geometry("1700x1000")
    lbl = Label(choice_screen, image=img)
    lbl.place(x=0, y=0)

    title =Label(choice_screen,text="🛺License Dashboard", fg="white", bg="black", width="200",
          height="1",
          font=("Forte", 75, "italic")).pack()

    # learner Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Apply For Learner License", command=lambda: learner_win(), width="40", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="200", y="300")

    # new Dl Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Apply For New License", command=lambda: newdl_win(), width="40", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="840", y="300")

    # Rectification Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Preview Document", command=lambda: disp_win(), width="40",height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="200", y="450")

    # SHow Details Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Request for Changes in License", command=lambda: rect_win(), width="40", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="840", y="450")

    choice_screen.mainloop()  # start the GUI

if __name__=="__main__":
    lw()
