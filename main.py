import os
import csv
import time
from os import path
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import date

def createfile():                                                   # General data / other than mee seva
    global todaysDAte
    todaysDAte = time.strftime("%d-%m-%y")
    dire = "/home/premchand/report/" + todaysDAte
    if not os.path.exists(dire):
        os.makedirs(dire)
        file = open(dire + "/report.csv", "a")
        fildes = ["Date","Area of Service", "Service", "Amount", "Charges"]
        write = csv.writer(file)
        write.writerow(fildes)
        file.close()

def main():                                                         # Main function to start the program
    todaysDAte = time.strftime("%d-%m-%y")
    dire = "/home/premchand/report/" + todaysDAte
    temp = 0
    if not path.exists(dire + "/report.csv"):
        createfile()

main()

##########################################################################################################
##########################################################################################################
##                                                                                                      ##
##                                      GUI FUNCTION START HERE                                         ##
##                                                                                                      ##
##########################################################################################################
##########################################################################################################

root = tk.Tk()
root.title("Management")
root.geometry("700x550")

# Label text for title
ttk.Label(root, text="Harsha Online and Meeseva Center",
          background="blue", foreground="yellow",
          font=("Times New Roman", 18,"bold")).grid(column=1,row=1)
# Lable
ttk.Label(root, text="Select the Service :",
          font=("Times New Roman", 15)).grid(row=5, padx=10, pady=25)

options = [
    "Mee Seva",
    "Aadhar",
    "Ticket Booking",
    "Other"
]

menu = tk.StringVar(root)
menu.set(options[0])  # Default Value
a = tk.OptionMenu(root, menu, *options)
a.config(width=27)
a.grid(column=1, row=5)

# Sub services entering
ttk.Label(root, text="Enter the Service:", font=("Times New Roman", 15)).grid(column=0, row=6, padx=10, pady=25)
service = tk.StringVar()
b = tk.Entry(width=32, textvariable= service).grid(column=1, row=6)

# Cost of Entering
ttk.Label(root, text="Enter the Cost:", font=("Times New Roman", 15)).grid(column=0, row=7, padx=10, pady=25)
cost = tk.IntVar()
c = tk.Entry(width=32, textvariable= cost).grid(column=1, row=7)

# Charges of Entering
ttk.Label(root, text="Enter the Charges:", font=("Times New Roman", 15)).grid(column=0, row=8, padx=10, pady=25)
charges = tk.IntVar()
d = tk.Entry(width=32, textvariable= charges).grid(column=1, row=8)


def add():

    datee = date.today()
    aos = menu.get()
    z = service.get()
    cost1 = cost.get()
    charges1 = charges.get()
    todaysDAte = time.strftime("%d-%m-%y")
    dire = "/home/premchand/report/" + todaysDAte
    f = open(dire +"/report.csv","a")
    write = csv.writer(f)
    data = [datee,aos,z,cost1,charges1]
    write.writerow(data)
    f.close()
    ttk.Label(root, text="Added Successfully", foreground="orange",  # Printing Success Message
              font=("Helvetica", 15, "bold italic")).grid(column=0, row=12)


def cals():
    #emp_remove()
    todaysDAte = time.strftime("%d-%m-%y")
    dire = "/home/premchand/report/" + todaysDAte
    x = pd.read_csv(dire + "/report.csv")
    y = x.fillna("0")
    y.to_csv(dire+"/modifiedReport.csv", index=False)
    print("done")
    with open(dire + "/modifiedReport.csv") as f:
        headers = next(f)
        total = 0
        chargess = 0
        for row in csv.reader(f):
            total += float(row[3])
            chargess += float(row[4])
        print("Spending :", total)
        print("Profit :", chargess)

    ttk.Label(root, text="Cost : "+str(total),foreground="orange",                   #Printing Total Income
              font=("Helvetica", 15, "bold italic")).grid(column=0, row=11)

    ttk.Label(root, text="Profit : "+str(chargess), foreground="green",                   #Printing Total Profit
              font=("Helvetica", 15, "bold italic")).grid(column=1, row=11)


button = tk.Button(root, text="ADD", width=10, command=add).grid(column=0, row=10, padx=10, pady=25)

button1 = tk.Button(root, text="CALCULATE", width=10, command=cals).grid(column=1,row=10,padx=10,pady=25)

button2 = tk.Button(root, text="EXIT", width=10, command=root.destroy).grid(column=2,row=12,padx=10,pady=25)

root.mainloop()

