import graph as gr
from tkinter import *
from tkinter import messagebox
import say
import services
from PIL import Image,ImageTk

def license_win():
    say.speak("fetching statics..")
    gr.licenseanalysis()

def city_win():
    say.speak("fetching statics..")
    gr.cityanalysis()

def test_win():
    say.speak("fetching statics...")
    gr.testanalysis()

def vehicleclass_win():
    say.speak("fetching statics...")
    gr.vehicleanalysis()

def fuel_win():
    say.speak("fetching statics...")
    gr.fuelanalysis()

def out():
    choice_screen.destroy()
    services.options()


def options():
    global choice_screen, screen_w, screen_h, x, y
    choice_screen = Tk()  # create a GUI window
    choice_screen["bg"] = 'lightgreen'
    choice_screen.title("RTO- Data Analysis ")  # set the title of GUI window
    #choice_screen.geometry("%dx%d+%d+%d" % (w, h, x, y))
    choice_screen.geometry("1700x1000")

    # image code
    image = Image.open("Images\\analysis.jpg")
    resize_image = image.resize((choice_screen.winfo_screenwidth(), choice_screen.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)
    choice_screen.geometry("1700x1000")
    lbl = Label(choice_screen, image=img)
    lbl.place(x=0, y=0)


    Label(text="🛺📊<< DATA Analysis Report >>📊🚍", fg="white", bg="black", width="200", height="2",
          font=("Georgia", 50,"italic")).pack()

    #licence Button
    button1 = Button(choice_screen, cursor="hand2", text="👉CITY BASED ANALYSIS ON LICENSE ISSUED", command=lambda: city_win(), width="42",height="3",font=("Comic Sans MS", 15, "bold"),
                     bg="gray", fg="white", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="200", y="200")


    button1 = Button(choice_screen,cursor="hand2", text="👉FUEL BASED ANALYSIS", command=lambda: fuel_win(), width="42", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="gray", fg="white", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="840", y="200")


    button1 = Button(choice_screen,cursor="hand2", text="👉RTO TEST ANYLYSIS", command=lambda: test_win(), width="42", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="gray", fg="white", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="200", y="350")


    button1 = Button(choice_screen,cursor="hand2", text="👉VECHILE CLASS ANYLYSIS", command=lambda: vehicleclass_win(), width="42", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="gray", fg="white", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="840", y="350")


    button1 = Button(choice_screen,cursor="hand2", text="👉LICENSE APPLICATION TYPE ANALYSIS", command=lambda: license_win(), width="42", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="gray", fg="white", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button1.place(x="200", y="500")


    button3 = Button(choice_screen,cursor="hand2", text="Back TO Services", command=lambda: out(), width="42", height="3",
                     font=("Comic Sans MS", 15, "bold"),
                     bg="brown", fg="white", borderwidth=2, bd="5", activebackground="#b4cf65", highlightcolor="black",
                     highlightthickness="4")
    button3.place(x="840", y="500")









    choice_screen.mainloop()  # start the GUI

if __name__=="__main__":
    options()


