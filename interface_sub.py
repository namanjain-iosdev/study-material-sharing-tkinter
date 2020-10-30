from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
def pythonsub():
    print("python subject")
def cppsub():
    print("cpp subject")
def dsasub():
    print("dsa subject")
def mathssub():
    print("maths subject")
def subjects():
    main_screen = Tk()
    main_screen.config(bg="#7D3C98")
    main_screen.geometry('600x400')
    main_screen.minsize(400, 300)
    main_screen.title("Study Material")
    l1 = Label(main_screen, text="Study Material", bg="#212F3D",fg="white", font=('Times New Roman', 18),relief=SUNKEN,padx="150",pady="20")
    l1.pack(side=TOP,padx="30",pady="20")
    f1 = Frame(main_screen,bg="#808B96")
    f1.pack(side=TOP)

    #variables of subject images
    python_sub_pic = PhotoImage(file=r'images' + os.path.sep + 'python_sub_pic.png')
    cpp_sub_pic = PhotoImage(file=r'images' + os.path.sep + 'cpp_sub_pic.png')
    dsa_sub_pic = PhotoImage(file=r'images' + os.path.sep + 'dsa_sub_pic.png')
    
    #making buttons of subjects
    btn_sub_1 = Button(f1, text="python",fg="black",command=pythonsub,image=python_sub_pic)
    btn_sub_1.grid(row=0,column=0,padx=(30,0),pady=(50,30))
    btn_sub_2 = Button(f1, text="cpp",fg="black",command=cppsub,image=cpp_sub_pic)
    btn_sub_2.grid(row=0,column=1,padx=(30,0),pady=(50,30))
    btn_sub_3 = Button(f1, text="dsa",fg="black",command=dsasub,image=dsa_sub_pic)
    btn_sub_3.grid(row=0,column=2,padx="30",pady=(50,30))
    #naming all the images of subjects
    sub_lable1 = Label(f1,text="python",fg="black", font=('Times New Roman', 18))
    sub_lable1.grid(row=1,column=0)
    sub_lable2 = Label(f1,text="cpp",fg="black", font=('Times New Roman', 18))
    sub_lable2.grid(row=1,column=1)
    sub_lable3 = Label(f1,text="dsa",fg="black", font=('Times New Roman', 18))
    sub_lable3.grid(row=1,column=2)

    main_screen.mainloop()
subjects()