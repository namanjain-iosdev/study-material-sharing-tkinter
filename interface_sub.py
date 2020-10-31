from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
def pythonsub():
    materials(r'study_materials/python_material')
def cppsub():
    materials(r'study_materials/cpp_material')
def dsasub():
    materials(r'study_materials/dsa_material')

def subjects():
    main_screen = Tk()
    main_screen.config(bg="#7D3C98")
    main_screen.geometry('600x400')
    main_screen.minsize(400, 300)
    main_screen.title("Study Material")
    l1 = Label(main_screen, text="Select a Subject", bg="#212F3D",fg="white", font=('Times New Roman', 18),relief=SUNKEN,padx="150",pady="20")
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

def materials(folder_path):
    screen1 = Tk()
    screen1.config(bg="#7D3C98")
    screen1.geometry('600x400')
    screen1.minsize(400, 300)
    screen1.title("Study Material")
    global l1

    l1 = Label(screen1, text="Study Material", bg="#212F3D",fg="white", font=('Times New Roman', 18),relief=SUNKEN,padx="150",pady="20")
    l1.pack(side=TOP,padx="30",pady="20")
    f2 = Frame(screen1,bg="#808B96")
    f2.pack(side=TOP)
    
    f3 = Frame(screen1,bg="#212F3D")
    f3.pack(side=TOP,padx="30",pady="20")

    for btn in range(1,len(listDir(folder_path))):
        Button(f3,text=listDir(folder_path)[btn],command=lambda:file_open(folder_path+os.path.sep+listDir(folder_path)[btn]),height="2",width="50").pack(side=TOP)
    screen1.mainloop()
def file_open(path):
    f = open(path)
    return f
#to get the file information

def listDir(dir):
    file_name_list = []
    fileNames = os.listdir(dir)
    
    for fileName in fileNames:
        file_name_list.append(fileName)
    return file_name_list
