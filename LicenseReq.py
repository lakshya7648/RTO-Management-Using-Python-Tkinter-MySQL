from tkinter import *
from PIL import Image, ImageTk
import LRequestWindow as lrw
import DLRequestWindow as dlrw
import AdminDashboard as ad

# ----Main function-----
def backfun(root):
    root.destroy()
    ad.main(loginusername)

def opLearnerWindow(root):
    root.destroy()
    # Toplevel(lrw.main())
    lrw.main(loginusername)

def opDlWindow(root):
    root.destroy()
    dlrw.main(loginusername)

def main(uname=""):
    global loginusername
    loginusername = uname
    root = Tk()
    root.state("zoomed")
    root.minsize(1200, 900)
    root.title("License Request Window")


# --------- Top Part----------------
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    TopFrame = Frame(root)
    TopFrame.place(x=0, y=0, width=w, height=100)

    img = Image.open("rtoimage.png")
    rimg = img.resize((100, 100))
    img1 = ImageTk.PhotoImage(rimg)

    PhotoLabel = Label(TopFrame, image=img1)
    PhotoLabel.place(x=0, y=0, width=100, height=100)

    topLabel = Label(TopFrame, text="License Request Window", padx=20, pady=40, font=("seogeui 25 bold"), bg="blue",
                     fg="white")
    topLabel.place(x=100, y=0, width=w - 100, height=100)
# ---------Top Part Ends--------------------
# ------------Main Board--------------------
    MainBoard = Frame(root, bg="#A6B4F7")
    MainBoard.place(x=0, y=100, width=w, height=h - 100)

    image = Image.open("brto.jpg")
    resize_image = image.resize((w, MainBoard.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)

    lbl = Label(MainBoard, image=img)
    lbl.place(x=0, y=0, width=w, height=MainBoard.winfo_screenheight())
# ---------Main Board Ends ------------------
   # -------Learner Request----------

    lreqf = Frame(MainBoard, bg="white")
    lreqf.place(x=100, y=70, width=400, height=400)
    lreqimg = ImageTk.PhotoImage(Image.open("Screenshot (124).png").resize((400, 399)))
    lreqbtn = Button(lreqf, image=lreqimg, relief=GROOVE, command=lambda:opLearnerWindow(root))
    lreqbtn.place(x=0, y=0)

    # -----------------------------
    # -------NewDL Request----------

    dlreqf = Frame(MainBoard, bg="#A75757")
    dlreqf.place(x=880, y=70, width=400, height=400)
    dlreqimg = ImageTk.PhotoImage(Image.open("Screenshot (125).png").resize((400, 400)))
    dlreqbtn = Button(dlreqf, image=dlreqimg, relief=GROOVE, command=lambda:opDlWindow(root))
    dlreqbtn.place(x=0, y=0)
    # -----------------------------

    back = Button(MainBoard, text="<---", bg="white", fg="red", font=("consolas 20 bold"), activebackground="red",
                  activeforeground="white", borderwidth=2, relief=SOLID, takefocus="red", command=lambda: backfun(root))
    back.place(x=0, y=0, width=160, height=50)

    root.mainloop()


# --------main() ends--------------
if __name__ == "__main__":
    main()