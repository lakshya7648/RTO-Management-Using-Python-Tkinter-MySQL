from tkinter import *
from tkinter import messagebox
import say as s
from PIL import Image,ImageTk
import pymysql as sql
import services as ser
import AdminDashboard as lak

def admin_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if username1 == "" or password1 == "":
        messagebox.showerror("Error", "Fill All The Required Fields")
        root2.destroy()
        s.speak("Please ! RE-LOGIN again carefully !!")
    else:
        # choice_screen.destroy()
        print('Login Details Got')
        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        cur = conn.cursor()
        qry = "select * from ADMIN_LOGIN where USERNAME='{0}' and PASSWORD='{1}'".format(username1, password1)
        print(qry)
        c = cur.execute(qry)  # it gives affected rows
        print(c)
        if c == 1:
            g = cur.fetchone()[0]
            print("Welcome", g)
            s.speak("Welcome sir,")
            s.speak(g)
            root2.destroy()
            choice_screen.destroy()
            lak.main(username1)# call lakshya entry function

        else:
            print("Invalid password")
            s.speak("wrong!!Try again!!")
            root2.destroy()

        conn.close()
        print(username1 + " " + password1)


def admin():
    global root2, unam_entry, password_entry
    global username_verify, password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    root2 = Toplevel(choice_screen)
    w2 = 350
    h2 = 250
    #root2.geometry("%dx%d+%d+%d" % (w2, h2, x, y))
    #root2.geometry("1700x1000")
    root2.config(bg="lightgreen")
    root2.title("Regional Transport Office-Operator Login")

    # image code
    image = Image.open("Images\\admin_login.jpg")
    resize_image = image.resize((root2.winfo_screenwidth(), root2.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    root2.geometry("1700x1000")
    lbl = Label(root2, image=img)
    lbl.place(x=0, y=0)

    # Login Title
    title = Label(root2, text="▂▄▅▆ ΛDMIП ▆▅▄▂ Login Page🔑", font=("Georgia", 45, "bold"), pady="5", bg="#082552",
                  fg="#67F5FF").pack(pady="50")
    login_frame = Frame(root2, width="380", height="340", bg="#3C87AF")
    login_frame.place(x="570", y="150")

    Label(root2, width="15", padx="5", pady="5", text="Enter Username* 👇", bg="#3C87AF", fg="red",
          font=("Calibri", 20, 'bold')).pack()
    # Label(root2, text="", bg="lightblue").pack()
    u_entry1 = Entry(root2,cursor="hand2", textvariable=username_verify, width=26, borderwidth=3, font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    u_entry1.pack()
    Label(root2, text="", bg="#3C87AF").pack()
    Label(root2, width="15", padx="5", pady="5", text="Enter Password* 👇", bg="#3C87AF", fg="red",
          font=("Calibri", 20, 'bold')).pack()
    # Label(root2, text="", bg="lightblue").pack()
    p_entry1 = Entry(root2,cursor="hand2", textvariable=password_verify, show="*", width=26, borderwidth=3,
                     font=("Calibri", 15, "italic"),highlightcolor="black",highlightthickness="4")
    p_entry1.pack()
    Label(root2, text="", bg="#3C87AF").pack()
    button1 = Button(root2,cursor="hand2", text="Login", command=lambda: admin_verify(), width="15", font=("Arial", 15, "bold"),
                     bg="lightgray", fg="black").pack()
    root2.mainloop()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if username1 == "" or password1== "":
        messagebox.showerror("Error", "Fill All The Required Fields")
        root2.destroy()
        s.speak("Please ! RE-LOGIN again carefully !!")
    else:
        #choice_screen.destroy()
        print('Login Details Got')
        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        cur=conn.cursor()
        qry = "select * from OPERATOR_LOGIN where USERNAME='{0}' and PASSWORD='{1}'".format(username1, password1)
        print(qry)
        c = cur.execute(qry)  # it gives affected rows
        print(c)
        if c == 1:
            g=cur.fetchone()[0]
            print("Welcome",g)  # fetch one gives first row and the [0] gives the index value=0 at that row
            s.speak("Welcome sir,")
            s.speak(g)
            root2.destroy()
            choice_screen.destroy()
            ser.options()

        else:
            print("Invalid password")
            s.speak("wrong!!Try again!!")
            root2.destroy()

        conn.close()
        print(username1 + " " + password1)



def operator():
    global root2,unam_entry,password_entry
    global username_verify,password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    root2=Toplevel(choice_screen)
    w2=350
    h2=250
    #root2.geometry("%dx%d+%d+%d" %(w2,h2,x,y))
    #root2.geometry("1700x1000")
    root2.config(bg="lightgreen")
    root2.title("Regional Transport Office-Operator Login")

    #image code
    image=Image.open("Images\\operator_login.jpg")
    resize_image=image.resize((root2.winfo_screenwidth(),root2.winfo_screenheight()))
    img=ImageTk.PhotoImage(resize_image)
    root2.geometry("1700x1000")
    lbl=Label(root2,image=img)
    lbl.place(x=0,y=0)




    # Login Title
    title = Label(root2,text="ⓄⓅⒺⓇⒶⓉⓄⓇ Login Page🔑", font=("Georgia", 45, "bold"), pady="5", bg="black", fg="lightyellow").pack(pady="50")
    login_frame = Frame(root2, width="380", height="340", bg="black")
    login_frame.place(x="570", y="300")

    labl1=Label(root2, width="15", padx="5", pady="5", text="Enter Username* 👇", bg="black", fg="red",font=("Calibri", 20, 'bold'))
    labl1.place(x="640",y="350")
    #Label(root2, text="", bg="lightblue").pack()
    u_entry1 = Entry(root2,cursor="hand2", textvariable=username_verify, width=26, borderwidth=3,font=("Calibri", 15, "italic"),highlightcolor="blue",highlightthickness="4")
    u_entry1.place(x="620",y="400")
    labl2=Label(root2, text="", bg="black").place(x="600",y="400")
    lbl3=Label(root2, width="15", padx="5", pady="5", text="Enter Password* 👇", bg="black", fg="red",font=("Calibri", 20, 'bold')).place(x="640",y="450")
    #Label(root2, text="", bg="lightblue").pack()
    p_entry1 = Entry(root2,cursor="hand2", textvariable=password_verify,show="*",width=26, borderwidth=3,font=("Calibri", 15, "italic"),highlightcolor="blue",highlightthickness="4")
    p_entry1.place(x="620",y="500")
    lbl4=Label(root2, text="", bg="black").pack()
    button1 = Button(root2,cursor="hand2", text="Login",command=lambda: login_verify(), width="15", font=("Arial", 15, "bold"), bg="lightblue", fg="red",bd="5").place(x="660",y="560")

    root2.mainloop()






def main_screen():
    global choice_screen,screen_w,screen_h,x,y
    choice_screen = Tk()  # create a GUI window
    choice_screen["bg"] = 'lightgreen'
    choice_screen.title("Electronic Regional Transport Office System")  # set the title of GUI window
    screen_w=choice_screen.winfo_screenwidth()
    screen_h=choice_screen.winfo_screenheight()
    w=350
    h=200
    x=screen_w/2.7
    y=screen_h/2.7
    #choice_screen.geometry("%dx%d+%d+%d" %(w,h,x,y))
    #choice_screen.geometry("1700x1000")
    # image code
    image = Image.open("Images\\intro.jpg")
    resize_image = image.resize((choice_screen.winfo_screenwidth(), choice_screen.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    choice_screen.geometry("1700x1000")
    lbl = Label(choice_screen, image=img)
    lbl.place(x=0, y=0)

    # create a Role label
    Label(text="🏍ῳɛƖƈơɱɛ ɬơ ▞▞▞▖🛺🅴-🆁🆃🅾🚍▝▞▞▞!", fg="red",bg="lightyellow", width="250", height="4", font=("Monotype Corsiva", 48)).pack()
    Label(text="Please Choose your Role....", fg="red",bg="lightyellow", font=("Arial", 25)).pack()
    Label(text="").pack()

    # create Admin Button
    Button(text="👉Admin Login",cursor="hand2", fg="blue2",bg="lightblue", height="3", width="30", font=("Verdana", 23,'bold'),command=lambda:admin(),bd="5").pack()
    Label(text="").pack()

    # create a User button
    Button(text="👉Operator Login",cursor="hand2", fg="blue2",bg="lightblue", height="3", width="30", font=("Verdana", 23,"bold"),command=lambda:operator(),bd="5").pack()


    choice_screen.mainloop()  # start the GUI



if __name__=="__main__":
    main_screen()  # call the main_account_screen() function
