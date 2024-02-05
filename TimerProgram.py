# Hi there, Just a random python program that acts as a timer because I cannot keep track of time myself





import time         # importing the time library, I think I need this for the actual timer
from tkinter import *
from tkinter import ttk



def converter(time):
    return int(time)





def countdown(input):


    #Stuff here to turn whatever input we get into just seconds
    total_seconds = converter(input)
    
    seconds_left = total_seconds
    
    while seconds_left != 0:
        time.sleep(1)
        #Do action here for every seconds
        seconds_left -= 1
    
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    print("Done")
    
    
    
hi = input("Please give me time in seconds")
countdown(hi)
