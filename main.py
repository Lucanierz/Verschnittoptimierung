import filehandler
import algorithmus
import userinput
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
import tkmacosx as tkm

root = tk.Tk()

root.geometry("800x500")
root.resizable(False, False)
root.title("Verschnittoptimierung")

content = ttk.Frame(root)

kvhvar = tk.BooleanVar(value=False)
bshvar = tk.BooleanVar(value=False)
fiftyvar = tk.BooleanVar(value=False)
fourtyvar = tk.BooleanVar(value=False)

lenghts = ttk.Entry(content, width= 50)


kvh = ttk.Checkbutton(content, text="KVH", variable=kvhvar, onvalue=True, width = 8)
bsh = ttk.Checkbutton(content, text="BSH", variable=bshvar, onvalue=True, width = 8)

fifty = ttk.Checkbutton(content, text="40x40", variable=fiftyvar, onvalue=True, width = 8)
fourty = ttk.Checkbutton(content, text="50x50", variable=fourtyvar, onvalue=True, width = 8)

def callread():
    filehandler.readin(kvhvar, fourtyvar, fiftyvar, bshvar)
def newwin():
    #newwindow = tk.Toplevel(root)
    lagertext = "".join(map(str, filehandler.readin(kvhvar, fourtyvar, fiftyvar, bshvar)))

    #coollabel = tk.Label(newwindow, text=lagertext)
    #coollabel.config(font=("Courier", 20))

    newwindow = tk.Toplevel(root)

    mytext = tk.StringVar(value=lagertext)

    myframe = ttk.Frame(newwindow)
    myentry = ttk.Entry(myframe, textvariable=mytext, state='readonly')
    myentry.config(font=("Courier", 20))
    myscroll = ttk.Scrollbar(myframe, orient='horizontal', command=myentry.xview)
    myentry.config(xscrollcommand=myscroll.set)

    myframe.grid()
    myentry.grid(row=1, sticky='ew')
    myscroll.grid(row=2, sticky='ew')
    print(lagertext)
    root.mainloop()

readbtn = ttk.Button(content, text="Lager einlesen", command=callread)
showbtn = ttk.Button(content, text="Lager zeigen", command=newwin)



content.grid(column=0, row=0)
kvh.grid(row = 0, column= 1)
bsh.grid(row = 0, column= 2)
fifty.grid(row=1, column=1)
fourty.grid(row=1, column=2)
lenghts.grid(row = 5, column = 1, columnspan = 2)
readbtn.grid(column=1, row=7)
showbtn.grid(column=2, row=7)



root.mainloop()


lager = filehandler.readin()

eingabe = userinput.Eingabe()

verschnitt = algorithmus.Optimierung(lager, eingabe)
algorithmus.getminverschnitt(lager, eingabe, verschnitt)
