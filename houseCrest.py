import tkinter
import tkinter as tk
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def crest(root, house):
    if house == 0:
        title = Label(root, text = "Alpha Chi Rho Core Report", font=('Arial', 15))
        title.place(x = 400, y = 0)
        openImg = Image.open("../CORE-Data-Analysis/Alpha_Chi_Rho_Crest.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 1:
        title = Label(root, text = "Delta Upsilon Core Report", font=('Arial', 15))
        title.place(x = 400, y = 0)
        openImg = Image.open("../CORE-Data-Analysis/DeltaUpsilon.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 2:
        title = Label(root, text="Delta Zeta Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/delta-zeta.jpg")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 3:
        title = Label(root, text="Kappa Delta Chi Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/The_Crest_of_Kappa_Delta_Chi_sorority.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 4:
        title = Label(root, text="Phi Kappa Sigma Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Phi-Kappa-Sigma-crest-247x300.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 5:
        title = Label(root, text="Phi Sigma Sigma Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Phi_Sigma_Sigma_crest.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 6:
        title = Label(root, text="Sigma Chi Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Sigma_Chi_Crest.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 7:
        title = Label(root, text="Sigma Phi Epsilon Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/SigEpCrest.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 8:
        title = Label(root, text="Tau Epsilon Phi Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Tau Epsilon Phi.jfif")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 9:
        title = Label(root, text="Tau Kappa Epsilon Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Tau_Kappa_Epsilon_Coat_of_Arms.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 10:
        title = Label(root, text="Theta Phi Alpha Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Theta_Phi_Alpha_crest.png")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)
    elif house == 11:
        title = Label(root, text="Zeta Nu Core Report", font=('Arial', 15))
        title.place(x=400, y=0)
        openImg = Image.open("../CORE-Data-Analysis/Zeta Nu.jfif")
        importImg = ImageTk.PhotoImage(openImg)
        img = tkinter.Label(image=importImg)
        img.image = importImg
        img.place(x=0, y=0)