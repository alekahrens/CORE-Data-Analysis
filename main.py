import logging

import tkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename as file
import pandas as pd
from tkinter.ttk import Combobox
import houseCOREBreakdown as breakDown


def grading(root, file):
    house = cb.get()
    house = house[2:-2]
    clear_frame()
    frameHomeChap = Frame(root, height=350)
    frameHomeChap.pack(side=TOP, fill=X)
    root.geometry('1000x725')
    root.title(house + ' CORE Report Grade')
    mainPage = Button(root, text='Home', fg='blue', command=lambda: home(root))
    mainPage.place(x=20,y=680)

    fail = Label(root, text="Fail", background='red')
    fail.place(x=100, y=680)
    passed = Label(root, text="Pass", background='green')
    passed.place(x=130, y=680)
    partial = Label(root, text="Partial Credit", background='yellow')
    partial.place(x=170, y=680)
    noData = Label(root, text="No Data", highlightbackground = "black")
    noData.place(x=250, y=680)
    breakDown.points(root, house, file)



def houseSelection(root, file):
    clear_frame()
    global chapters
    chapters = pd.read_excel(file,usecols="A", )
    list = chapters.values
    list = list[:]
    frameHomeChap = Frame(root, height=350)
    frameHomeChap.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Clarkson University CORE Analysis')

    openImg = Image.open("../CORE-Data-Analysis/FSL.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=150, y=0)

    global cb

    cb = Combobox(root, values=list, width=30, state='readonly')
    cb.place(x=150, y=200)

    back = Button(root, text='Back', fg='blue', command=lambda: home(root))
    back.place(x=200, y=250)

    submit = Button(root, text="Submit", fg='blue', command=lambda: grading(root, file))
    submit.place(x=265, y=250)


def home(root):
    clear_frame()
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Clarkson University CORE Data Analysis')
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file="../CORE-Data-Analysis/clarkson.png"))

    openImg = Image.open("../CORE-Data-Analysis/FSL.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=145, y=0)

    houseSearch = Button(root, text='House Search', fg='blue', command=lambda:houseSelection(root, filename))
    houseSearch.place(x=200, y=250)


    bio = Label(text='Created by Alek Ahrens of Phi Kappa Sigma Fall 2020')
    bio.place(x=100,y=320)

def data():
    global filename
    filename = file()

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

if __name__ == '__main__':
    logging.basicConfig(
        filename='testing.log', level=logging.DEBUG)
    try:
        root = tk.Tk()
        root.resizable(False,False)
        data()
        home(root)
        root.mainloop()
    # pylint: disable=broad-except
    except Exception as err:
        logging.error(err)
