# import datetime
# val = int(datetime.datetime.today().strftime("%Y"))+15
# print(val)
# print(datetime.datetime.today().strftime(f"{val}-%m-%d"))

from tkinter import *

root = Tk()
root.state("zoomed")
root.minsize(1200, 900)
f1 = Frame(root)
f1.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())

lbl = Label(f1, text="lbl", bg="red", fg="white")
lbl.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())


def backB(root, f2, f1):
    f2.destroy()

def openFun(root, f1):
    f2 = Frame(f1)
    f2.place(x=0, y=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())

    lbl = Label(text="In Frame 2", bg="blue", fg='white')
    lbl.place(x = 0, y =0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())

    backButton = Button(f2, text="<--", bg="white", fg="red", command=lambda :backB(root, f2, f1))
    backButton.place(x=0, y=0, width=200, height=80)


Open = Button(f1, text="Open", bg="white", fg="black", command=lambda : openFun(root, f1))
Open.place(x = 100, y = 100, width=200, height = 100)
root.mainloop()

