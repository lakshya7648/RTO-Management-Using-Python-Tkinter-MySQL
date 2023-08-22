from tkinter import *
from PIL import Image, ImageTk
import fillRCRenew as rcren
import fillLicRenew as lcren

def openLic(root):
    root.destroy()
    lcren.main()
    main()

def openRC(root):
    root.destroy()
    rcren.main()
    main()

def main():
    root = Tk()
    root.state("zoomed")
    root.title("Open Window")

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    TopFrame = Frame(root)
    TopFrame.place(x=0, y=0, width=w, height=100)

    img = Image.open("rtoimage.png")
    rimg = img.resize((100, 100))
    img1 = ImageTk.PhotoImage(rimg)

    PhotoLabel = Label(TopFrame, image=img1)
    PhotoLabel.place(x=0, y=0, width=100, height=100)

    topLabel = Label(TopFrame, text="Open Window", padx=20, pady=40, font=("seogeui 25 bold"), bg="green",
                     fg="white")
    topLabel.place(x=100, y=0, width=w - 100, height=100)

    # MainBoard-----------
    MainBoard = Frame(root, bg="#A6B4F7")
    MainBoard.place(x=0, y=100, width=w, height=h - 100)

    image = Image.open("BackRTO.jpg")
    resize_image = image.resize((w, MainBoard.winfo_screenheight()))
    img = ImageTk.PhotoImage(resize_image)

    lbl = Label(MainBoard, image=img)
    lbl.place(x=0, y=0, width=w, height=MainBoard.winfo_screenheight())

    # --------------------
    oplc = Button(MainBoard, text="Open License Renewal Window", bg="green", fg="white", activebackground="white", activeforeground="green", font=('comissansms 20 bold'),command=lambda:openLic(root))
    oplc.place(x=200, y=100, width=500, height=100)
    oprc = Button(MainBoard, text="Open RC Renewal Window", bg="green", fg="white", activebackground="white",
                  activeforeground="green", font=('comissansms 20 bold'), command=lambda: openRC(root))
    oprc.place(x=200, y=300, width=500, height=100)
    root.mainloop()

if __name__ == "__main__":
    main()