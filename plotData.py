'''
Info:
Works with Python3.5, untested with other versions

Incase libraries are missing, use pip install to download them

To run:
py plotData.py <filepath>.xlsx

File extension supported: xlsx
Othe file types are untested and may not work.
'''

#imports
import sys

import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def validateFile(file_location):
    #check if mofo entered a file before pressing the button
    if not file_location:
        print("File path not specified.  Exit program.")
        return False
    #find file from cmd argument
    parse = file_location.split('.')
    if len(parse) > 1:
        #file has extension
        if (parse[len(parse)-1] == "xlsx"):
            print("File extension accepted..\n")
            return True
    return False
    #exit if file path isn't provided


def plotData(file_location):
    #not sure what is happening here because IMPLICIT TYPE REFERENCE OMG SO GUUUDDD
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)

    #these are time values (frames)
    t = [sheet.cell_value(i, 0) for i in range(sheet.nrows)]
    #iterate over all columns, but this shit wont work cuz fucking COLOR IS DETERMINED BY A FUCKING STRING!!
    #To iterate over all 8 channels, make a loop:
        #loop 8 times
        #map the 8 digits to a char (which belogs to a color)

    y = [sheet.cell_value(i, 1) for i in range(sheet.nrows)]
    y2 = [sheet.cell_value(i, 2) for i in range(sheet.nrows)]

    plt.plot(t,y, 'b', linewidth=2, markersize=12)
    plt.plot(t,y2, 'g', linewidth=2, markersize=12)

    plt.axis([0,len(t),0,len(y)])
    plt.show()
'''
things to do:
- Add legend
- title
- fix damn x/y range
- add axis names
'''
