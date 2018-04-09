#Module for the gui

import tkinter as gui
import plotData as pd


def pressButton():
    file_location = E1.get()
    if not pd.validateFile(file_location):
        print("File name not accepted.\nInput valid file path.\nPlease add file extension '.xlsx' ")
        return
    pd.plotData(file_location)

window = gui.Tk()
frame = gui.Frame(window)
frame.pack()
#window.geometry("300x100")


#Text entry
E1 = gui.Entry(frame, bd =5)
fileBrowser = gui.Button(frame, text="Load File", command = pressButton )

#place shit
#E1.place(x=51, y=0)
#fileBrowser.place(x=0, y=0)

E1.pack(side = gui.LEFT)
fileBrowser.pack(side = gui.LEFT)

window.mainloop()
