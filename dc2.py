from tkinter import *
from tkinter import filedialog

interface = Tk()

interface.title("XMage Decklist Converter")

frame = Frame(interface, padx = 25, pady = 25)

def openfile():
    name = filedialog.askopenfilename()
    with open(name) as file_object:
        lines = file_object.readlines()

    deckt = []

    for line in lines:
        b1 = line.find("[")
        b2 = line.find("]")

        nl = line.replace(line[b1:b2 + 1], "")

        deck.append(nl)
    
        
    leg = name[:-4] + ".txt"

    deck[-1] = ""
    deck[-2] = ""

    with open(leg, "w") as file_object:
        for thing in deck:
            file_object.write(thing)

    #Show Decklist

    frame2 = Frame(interface, padx = 25, pady = 25)

    deck = Label(frame2, text = leg + " created!")
    deck.pack()
    frame2.pack()
    
    return "Done"

button = Button(frame, text="Convert!", command=openfile)  
button.pack()

credit = Label(frame, text = "Created by Will Hall")
credit.pack()

frame.pack()

interface.mainloop()
