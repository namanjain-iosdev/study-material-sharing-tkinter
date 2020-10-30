from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def subjects():
    main_screen = Tk()
    main_screen.config(bg="#ffe6c8")
    main_screen.geometry('1080x1080')
    main_screen.minsize(400, 300)
    main_screen.title("Study Material")
    l1 = Label(main_screen, text="Study Material", bg="#8c8272",fg="white", font=('Times New Roman', 18))
    l1.pack(fill=X,side=TOP)
    f1 = Frame(main_screen,bg="white")
    f1.pack(side=TOP)
    l1 = Label(f1, text="Study Material", bg="#8c8272",fg="white", font=('Times New Roman', 18))
    l1.grid(row=0,column=0)
    main_screen.mainloop()
subjects()