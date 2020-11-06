import xlrd
import numpy as np
import matplotlib.pyplot as plt
import time
file_location = "C:/Users/minha/OneDrive/Desktop/Stock/output.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

i = 1

while(i==1):

    x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.ncols)]
    y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.ncols)]
    yerr_pos = [first_sheet.cell_value(i, 2) for i in range(first_sheet.ncols)]
    yerr_neg = [first_sheet.cell_value(i, 3) for i in range(first_sheet.ncols)]

    yerr = [yerr_neg, yerr_pos]

    plt.errorbar(x,y,yerr,fmt='r^')

    plt.axis([0,5,0,5])
    plt.show()
    time.sleep(60)