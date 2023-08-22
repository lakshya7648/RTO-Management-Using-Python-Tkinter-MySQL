from tkinter import *
from tkinter import messagebox

import say
import say as s
import services as ser
#import RC_printing as printer
import datetime
import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
import services as ser
from tkinter import messagebox
import pymysql as sql
import say as s
import rc as r
from PIL import Image,ImageTk









def fetch():
    global ll
    ll= ah.get()
    print(ll)
    conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
    qry = "select Aadhar_num from status where RC_status='{0}'".format('APPROVE')
    cur = conn.cursor()
    c = cur.execute(qry)
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

    conn.commit()
    conn.close()

    if c1 == 1:
        main()
    else:
        messagebox.showerror("error", "Documnet not Found!!")
        say.speak("sorry!!Document Approval Pending!!")
        choice_screen.destroy()
        ser.options()



def cancel1(root):
    s.speak("A FILE has been downloaded for the customer as RC document please wait opening")
    messagebox.showinfo("information", "OPENING THE FILE !!Ensure That you have Printed The Generated RC_Document Before Closing it !!")
    choice_screen.destroy()
    root.destroy()

    import subprocess
    path = "RC_download.pdf"
    subprocess.Popen([path], shell="True")

    ser.options()



class InvoiceGenerator:
    def __init__(self,root):
        self.root = root
        self.root.title("RC_document GENeration by RTO")
        self.root.geometry("1700x1000")

        self.frame = Frame(self.root, bg="lightgreen")
        self.frame.place(x=0, y=0, width=1700, height=700)


        # get the details from the table RC_master
        global Fullname, father, dob, aadhar , fuel, mob, address, city, state,pin,vehicle,engine,chasis,manufacturer,colour,vehicleclass,seat,lstgot,lstin
        '''lst = ['Full Name', "Father's Name", 'Date-Of-Birth', 'Aadhar No.', 'Registration Number', 'Fuel type',
               'Address', 'City', 'State', 'Pin', 'Vehicle Type', 'Engine Number', 'Chasis Number', 'Manufacturer Name',
               'Colour', 'Vehicle Class', 'Seating Capacity', 'Issue Date', 'Expiray Date']'''


        lstin=[]
        lstgot = []


        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select * from rc where aadhaar_number='{0}'".format(ll)
        print(qry)
        cur = conn.cursor()
        cur.execute(qry)
        global data
        data = cur.fetchone()
        conn.close()

        lstgot = []
        for i in range(0, 20):
            plus = data[i]
            lstgot.append(plus)

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
        c = canvas.Canvas("RC_download.pdf", pagesize=(200, 250), bottomup=0)
        c.setFillColorRGB(0.8, 0.5, 0.7)

        # background watermark
        img_file = "Images\\png_20230215_193432_0000.png"
        x1 = 10
        y1 = 55
        c.drawImage(img_file, x1, y1, width=180, height=180, preserveAspectRatio=False)

        c.line(20, 22, 180, 22)  # above 1 line
        c.line(5, 45, 195, 45)  # above 2 line
        # c.line(55, 120, 185, 120)
        c.line(35, 45, 35, 220)  # left margin line
        # c.line(115, 108, 115, 220)
        # c.line(135, 108, 135, 220)
        # c.line(160, 108, 160, 220)
        c.line(15, 220, 185, 220)  # bottom line

        # left Emblem
        img_file = "Images\\india-clipart-emblem-17 (3).png"
        x1 = 5
        y1 = 10
        c.drawImage(img_file, x1, y1, width=25, height=30, preserveAspectRatio=False)

        # right emblem
        img_file = "Images\\india-clipart-emblem-17 (3).png"
        x1 = 170
        y1 = 10
        c.drawImage(img_file, x1, y1, width=25, height=30, preserveAspectRatio=False)

        # signature emblem
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
        c.drawCentredString(100, 30, "Registration Document Issued by Government")
        c.drawCentredString(100, 35, data[8] + ", India")
        c.setFont("Times-Bold", 3)
        c.drawString(10, 230, "This is system generated RC_Document!")
        # c.drawRightString(180, 228, self.aus.get())
        td = datetime.datetime.today().strftime("%d-%m-%Y")
        tdt = datetime.datetime.today().strftime("%H:%M:%S %p")
        print(td, tdt)
        c.drawString(10, 235, td)
        c.drawString(10, 240, tdt)
        c.drawRightString(180, 235, "RTO Authority Signature")

        lst=['Registration No.','Aadhar No.','Name','Father Name','Date-Of-Birth','Mob No.','Address','State','City','Pin Code','Manufacturer Name','Vehicle Class','Engine no.','Chasis no.','Fuel type','Seating Capacity','Issue Date','Expiry Date','Colour','Vehicle Type']
        c.setFont("Times-Bold", 7)
        #c.setFillColorRGB(0.8, 0, 0)
        c.setFillColorRGB(0.9, 0, 0)
        y=55
        p=55
        for i in range(1,20):# loop to generate serial numbers and lines and headings
            c.drawCentredString(20, int(y), str(i)+".")
            #c.line(5, int(y+1),195, int(y+1))
            c.drawString(40, int(y), (lst[i-1]+"-").ljust(10))
            y=y+8

        c.setFillColorRGB(0.0,0.0,0.0)
        c.setFont("Courier", 6)
        for j in range(1,20):
            if j==5 or j==17 or j==18:

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



def disp_win():

    root = Toplevel(choice_screen)
    #choice_screen.destroy()
    #root.geometry("1700x1000")
    root.config(bg="lightgreen")
    root.title("RC_hard copy")
    # image code
    l = root
    image = Image.open("Images\\rto.jpg")
    resize_image = image.resize((l.winfo_screenwidth(), l.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    l.geometry("1700x1000")
    lbl = Label(l, image=img)
    lbl.place(x=0, y=0)

    title = Label(root, text="🏍 Preview And Download R.C Document 🏍", font=("Georgia", 45, "bold"), pady="5",
                  bg="black",
                  fg="white").pack(pady="50")
    global ah
    ah = StringVar()
    say.speak("Enter Adhharcard Number..")
    label_1 = Label(root, text="Aadhar Number*👇", width=30, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_1.place(x=500, y=250)
    entry_1 = Entry(root, cursor="hand2", textvar=ah, width=30, borderwidth=7, font=("Calibri", 20, "bold"),highlightcolor="red",highlightthickness="4")
    entry_1.place(x=500, y=300)
    button1 = Button(root, cursor="hand2", text="Show Details", command=lambda :fetch(), width="20", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="brown", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="red",
                     highlightthickness="4")
    button1.place(x="600", y="400")

    root.mainloop()

    #ask what will be the criteria of selection ?????
    #printer.main()

def data():

    # also enter details in RC_table

    #mob, address, city, state, pin, vehicle, engine, chasis, manufacturer, colour, vehicleclass, seat
    birth=dob.get()
    veh=vehicle.get()
    fthr=father.get()
    ahr=aadhar.get()
    ful=fuel.get()
    nam=Fullname.get()
    add=address.get()
    cty=city.get()
    st=state.get()
    pn=pin.get()
    eng=engine.get()
    chas=chasis.get()
    manu=manufacturer.get()
    colr=colour.get()
    vehcl=vehicleclass.get()
    sat=seat.get()
    mb=mob.get()

    print(birth)
    print(veh)
    print(fthr)
    print(ahr)
    print(nam)
    print(add)
    print(cty)
    print(st)
    print(pn)
    print(eng)
    print(chas)
    print(manu)
    print(colr)
    print(vehcl)
    print(sat)
    if ful== '1':
        k="PETROL"
    elif ful== '2':
        k="DIESEL"
    else:
        k="C.N.G"
    print(k)
    # updation in the Updation table to be done
    # enter data in Rc-Table
    conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
    cur=conn.cursor()
    qry = "insert into rc values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}',{16},{17},'{18}','{19}')".format('null',ahr,nam,fthr,birth,mb,add,st,cty,pn,manu,vehcl,eng,chas,k,sat,'null','null',colr,veh)
    cur.execute(qry)


    # updation in the Updation table to be done
    #EXTRA PART STARTS
    qryt = "select Aadhar_num from status"
    cur.execute(qryt)
    datat=cur.fetchall()
    c1 = 0
    for row in datat:
        for col in row:
            if ahr == col:
                print("THis to Update")
                c1 = 1
                break
        # print(row)
    if c1==1:
        qry1 = "update status set RC_status='PENDING' where Aadhar_num='{0}'".format(ahr)
        cur.execute(qry1)
        conn.commit()
        conn.close()
    else:
        qry1="insert into status values('{0}',{1},{2},'{3}')".format(ahr,'null','null','PENDING')
        cur.execute(qry1)
        conn.commit()
        conn.close()
    # EXTRA PART ENDS

    '''qry1 = "update status set RC_status='PENDING' where Aadhar_num='{0}'".format(ahr)
    cur.execute(qry1)
    conn.commit()
    conn.close()'''



    ok()

def cancel():
    root.destroy()
    choice_screen.destroy()
    ser.options()

def ok():
    messagebox.showinfo("information", "REQUEST SEND Successfully!!")
    s.speak(" RTO will reply to customer in 7 days, a message has been send")
    choice_screen.destroy()
    ser.options()


def rectrc_win():
    pass

def newrc_win():
    global root
    root = Toplevel(choice_screen)
    #root.geometry("1700x1000")
    root.config(bg="lightgreen")
    # image code
    l = root
    image = Image.open("Images\\taxi.jpg")
    resize_image = image.resize((l.winfo_screenwidth(), l.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    l.geometry("1700x1000")
    lbl = Label(l, image=img)
    lbl.place(x=0, y=0)

    root.title("Application Form For New R.C")
    title = Label(root, text="🏍Application For A New REGISTRATION CERTIFICATE", font=("Georgia", 35, "bold"), pady="5",
                  bg="black",
                  fg="red").pack(pady="50")

    login_frame = Frame(root, width="1500", height="1000", bg="lightblue")
    login_frame.place(x="15", y="150")
    global Fullname, father, dob, aadhar, fuel, mob, address, city, state,pin,vehicle,engine,chasis,manufacturer,colour,vehicleclass,seat

    Fullname = StringVar()
    father = StringVar()
    dob = StringVar()
    aadhar = StringVar()
    fuel = StringVar()
    mob = StringVar()
    address = StringVar()
    city = StringVar()
    state = StringVar()
    pin= StringVar()
    vehicle=StringVar()
    engine = StringVar()
    chasis= StringVar()
    manufacturer=StringVar()
    colour=StringVar()
    vehicleclass=StringVar()
    seat=StringVar()

    label_1 = Label(root, text="FullName👉", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_1.place(x=80, y=160)

    entry_1 = Entry(root,cursor="hand2", textvar=Fullname, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_1.place(x=320, y=160)

    label_2 = Label(root,cursor="hand2", text="Father's Name👉", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_2.place(x=68, y=210)

    entry_2 = Entry(root,cursor="hand2", textvar=father, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_2.place(x=320, y=210)

    label_3 = Label(root,cursor="hand2", text="Fuel Type👉", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_3.place(x=70, y=260)

    Radiobutton(root,cursor="hand2", text="Petrol", padx=5, variable=fuel, value=1, font=("Calibri", 15, 'italic'),
                bg="lightblue",state="normal").place(x=320, y=260)
    Radiobutton(root, text="Diesel",cursor="hand2", padx=20, variable=fuel, value=2, font=("Calibri", 15, 'italic'),
                bg="lightblue",state="normal").place(x=417, y=260)
    Radiobutton(root, text="CNG", padx=20,cursor="hand2", variable=fuel, value=3, font=("Calibri", 15, 'italic'),
                bg="lightblue",state="normal").place(x=520, y=260)

    label_4 = Label(root, text="Vehicle type👉", width=20,cursor="hand2", bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_4.place(x=70, y=310)

    list1 = ['Light Motor Vehicle', 'Medium Goods Vehicle', 'Medium Passenger Motor Vehicle', 'Heavy Goods Vehicle',
             'Heavy Passenger Vehicle', 'AutoRikshaw/Van', 'Tractor', 'MotorCycle', 'Electronic Vehicle'];

    droplist = OptionMenu(root, vehicle, *list1)
    droplist.config(width=26, borderwidth=3,cursor="hand2", font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    vehicle.set('None')
    droplist.place(x=320, y=310)

    label_5 = Label(root, text="Aadhar Number*👉",cursor="hand2", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_5.place(x=65, y=360)
    entry_5 = Entry(root, textvar=aadhar, width=26,cursor="hand2", borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_5.place(x=320, y=360)

    label_6 = Label(root, text="D.O.B(yyyy-mm-dd)👉",cursor="hand2", width=20, bg="lightblue", fg="red", font=("Calibri", 20, 'bold'))
    label_6.place(x=40, y=410)
    entry_6 = Entry(root, textvar=dob, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_6.place(x=320, y=410)

    label_7 = Label(root, text="Mob no👉",cursor="hand2", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_7.place(x=70, y=460)
    entry_7 = Entry(root, textvar=mob,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_7.place(x=320, y=460)

    # +50 IN Y

    label_8 = Label(root, text="Address👉",cursor="hand2", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_8.place(x=780, y=160)
    entry_8 = Entry(root, textvar=address,cursor="hand2", width=30, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_8.place(x=1000, y=160)

    label_8 = Label(root, text="City👉",cursor="hand2", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_8.place(x=800, y=240)
    entry_8 = Entry(root, textvar=city,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_8.place(x=1000, y=240)

    label_9 = Label(root, text="State👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_9.place(x=800, y=300)
    entry_9 = Entry(root, textvar=state,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"), state="readonly",highlightcolor="black",highlightthickness="4")
    entry_9.place(x=1000, y=300)
    state.set("UTTAR PRADESH")

    label_10 = Label(root, text="Engine Number*👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_10.place(x=725, y=360)
    entry_10 = Entry(root, textvar=engine,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_10.place(x=1000, y=360)

    label_11 = Label(root, text="Chasis_no*👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_11.place(x=750, y=410)
    entry_11 = Entry(root, textvar=chasis,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_11.place(x=1000, y=410)



    label_13 = Label(root, text="PIN CODE👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_13.place(x=750, y=460)
    entry_13 = Entry(root, textvar=pin,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_13.place(x=1000, y=460)

    label_14 = Label(root, text="Manufacture Name👉", width=20, bg="lightblue", fg="red",
                    font=("Calibri", 20, 'bold'))
    label_14.place(x=50, y=510)
    entry_14 = Entry(root, textvar=manufacturer,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_14.place(x=320, y=510)

    label_15 = Label(root, text="Colour👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_15.place(x=780, y=510)
    entry_15 = Entry(root, textvar=colour,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_15.place(x=1000, y=510)

    label_16 = Label(root, text="Vehicle Class👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_16.place(x=50, y=560)

    list3 = ['LIGHT DUTY', 'MEDIUM HEAVY DUTY', 'HEAVY DUTY'];

    droplist = OptionMenu(root,vehicleclass, *list3)
    droplist.config(width=26,cursor="hand2", borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    vehicleclass.set('None')
    droplist.place(x=320, y=560)

    label_17 = Label(root, text="Seating Capacity👉", width=20, bg="lightblue", fg="red",
                     font=("Calibri", 20, 'bold'))
    label_17.place(x=730, y=560)
    entry_17 = Entry(root, textvar=seat,cursor="hand2", width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    entry_17.place(x=1000, y=560)
    s.speak("Please fill the application form...")
    button2 = Button(root, text="Apply For Generation",cursor="hand2", command=lambda: data(), width="30", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="brown", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button2.place(x="300", y="650")

    button1 = Button(root, text="Cancel!!!",cursor="hand2", command=lambda: cancel(), width="30", height="1",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="red", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="800", y="650")

    root.mainloop()

def rcw():

    global choice_screen, screen_w, screen_h, x, y
    choice_screen = Tk()  # create a GUI window
    #choice_screen["bg"] = 'lightgreen'
    choice_screen.title("RTO- RC ")  # set the title of GUI window

    #choice_screen.geometry("%dx%d+%d+%d" % (w, h, x, y))
    #choice_screen.geometry("1700x1000")

    # image code
    l = choice_screen
    image = Image.open("Images\\taxi.jpg")
    resize_image = image.resize((l.winfo_screenwidth(), l.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    l.geometry("1700x1000")
    lbl = Label(l, image=img)
    lbl.place(x=0, y=0)


    title =Label(choice_screen,text="🛺Registration Certificate Dashboard", fg="white", bg="black", width="200",
          height="2",
          font=("Monotype Corsiva", 62, "bold")).pack()

    # new RC Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Apply For A New R.C", command=lambda: newrc_win(), width="40", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="500", y="250")

    # Rectification Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Preview R.C Document", command=lambda: disp_win(), width="40", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="500", y="400")

    # SHow Details Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Apply For Updation in R.C", command=lambda: rectrc_win(), width="40",
                     height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     fg="white", bg="teal", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="500", y="550")

    choice_screen.mainloop()  # start the GUI

if __name__=="__main__":
    rcw()

