from tkinter import *

window = Tk()

window.title("Sleep Apnea Detection")

window.geometry('360x370')

lbl = Label(window, text="Choose a file for analysis")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")
    #analyseFile()

btn = Button(window, text="Upload", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()
