from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import say
import licence as lic
import rc
import aw
import statusOP as swin
import midWindow as ren


def log_out():
    messagebox.showinfo("information", "Are you sure you want to LOG OUT ?")
    choice_screen.destroy()
    say.speak("You Logged Out Successfully,have a good day ahead,THANk YOU")

def licence_win():
    say.speak("Opening License related services")
    print("License Services Called")
    choice_screen.destroy()
    lic.lw()

def RC_win():
    say.speak("Opening Vehicle Registration related services")
    print("RC services Called")
    choice_screen.destroy()
    rc.rcw()
    print("it works")

#ctrl+r for replace

def status_win():
    say.speak("Opening License or RC Status Window")
    choice_screen.destroy()
    swin.main()
    print("it works")
    options()


def analysis_win():
    say.speak("Opening Data Analysis Window")
    print("RC services Called")
    choice_screen.destroy()
    aw.options()
    print("it works")

def renewal_win():
    say.speak("Opening Renewal Window")
    choice_screen.destroy()
    ren.main()
    options()
    print("it works")


def options():
    global choice_screen, screen_w, screen_h, x, y
    choice_screen = Tk()  # create a GUI window
    #choice_screen["bg"] = 'lightgreen'
    choice_screen.title("RTO- Services ")  # set the title of GUI window
    screen_w = choice_screen.winfo_screenwidth()
    screen_h = choice_screen.winfo_screenheight()

    #choice_screen.geometry("%dx%d+%d+%d" % (w, h, x, y))
    #choice_screen.geometry("1700x1000")


    #MainBoard=Frame(choice_screen,bg="#A6B4F7")
   # MainBoard.place(x=0,y=20,width=2000,height=1900)

    #image code
    image=Image.open("Images\\american_highway.jpg")
    resize_image=image.resize((choice_screen.winfo_screenwidth(),choice_screen.winfo_screenheight()))
    img=ImageTk.PhotoImage(resize_image)
    choice_screen.geometry("1700x1000")
    lbl=Label(choice_screen,image=img)
    lbl.place(x=0,y=0)




    Label(text="🛺< SERVICES for ⲯ﹍︿﹍ 𝚂𝚊𝚏𝚎 𝚁𝙸𝙳𝙴 ﹍ⲯ﹍︿﹍☼ Always!!>🚍", fg="red", bg="lightyellow", width="200", height="3",
          font=("Segoe Script", 34,"bold")).pack()# broadway

    #licence Button
    button1 = Button(choice_screen,cursor="hand2",text="👉LICENSE Services", command=lambda: licence_win(), width="30",height="3",font=("Comic Sans MS", 17, "bold"),
                     bg="teal", fg="white",borderwidth=2,bd="5",highlightcolor="black",highlightthickness="4",activebackground="#b4cf65")
    button1.place(x="200", y="300")

    # RC Button
    button1 = Button(choice_screen,cursor="hand2", text="👉VEHICLE 'R.C'  Services", command=lambda: RC_win(), width="30", height="3",
                     font=("Comic Sans MS", 17, "bold"),
                     fg="white", bg="teal",borderwidth=2,bd="5",highlightcolor="black",highlightthickness="4",activebackground="#b4cf65")
    button1.place(x="840", y="300")

    # Status Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Status OF RC or Lisence Window", command=lambda: status_win(), width="30", height="3",
                     font=("Comic Sans MS", 17, "bold"),
                     fg="white", bg="teal",activebackground="#b4cf65",borderwidth=2,bd="5",highlightcolor="black",highlightthickness="4")
    button1.place(x="35", y="450")

    # Renewal Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Renewal Window", command=lambda: renewal_win(), width="30", height="3",
                     font=("Comic Sans MS", 17, "bold"),
                     fg="white", bg="teal",borderwidth=2,bd="5",activebackground="#b4cf65",highlightcolor="black",highlightthickness="4")
    button1.place(x="550", y="450")

    # Any EXTRA Information Button
    button1 = Button(choice_screen,cursor="hand2", text="👉Analysis Window", command=lambda: analysis_win(), width="30", height="3",
                     font=("Comic Sans MS", 17, "bold"),
                     fg="white", bg="teal",borderwidth=2,bd="5",activebackground="#b4cf65",highlightcolor="black",highlightthickness="4")
    button1.place(x="1060", y="450")

    button3 = Button(choice_screen,cursor="hand2", text="LOG OUT", command=lambda: log_out(), width="30", height="1",
                     font=("Comic sans ms", 15, "bold"),
                     bg="brown", fg="white",borderwidth=2,bd="5",activebackground="#b4cf65",highlightcolor="black",highlightthickness="4")
    button3.place(x="580", y="600")








    choice_screen.mainloop()  # start the GUI

if __name__=="__main__":
    options()
