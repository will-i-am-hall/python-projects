from tkinter import *
import json
import requests
from PIL import ImageTk, Image
from io import BytesIO

root = Tk()
root.title("MTG Card Data")

ladholder = Frame(root, padx = 25, pady = 25)
ladholder.grid(row = 1, column = 0)

ladholder2 = Frame(root, padx = 25, pady = 25)
ladholder2.grid(row = 0, column = 2, rowspan = 2)

ladholder3 = Frame(root, padx = 25, pady = 25)
ladholder3.grid(row = 0, column = 0)

canva = Canvas(ladholder, width = 300, height = 400)
canva.grid(row = 0, column = 0)

nameguy = Entry(ladholder, width = 50)
nameguy.grid(row = 2, column = 0)

def clearf():
    
    for widget in ladholder2.winfo_children():
        widget.destroy()
    ladholder2.grid_forget()

    for widget in ladholder3.winfo_children():
        widget.destroy()
    ladholder3.grid_forget()
    

def pullcard():
    clearf()
    
    nameget = nameguy.get()
    nameguy.delete(0, END)
    name = "https://api.magicthegathering.io/v1/cards.json?name=\""+nameget+"\""
    puller = requests.get(name)
    thecard = puller.json()
    thecard = thecard['cards'][0]
    
    global yoorl
    global img
    global popper
    global imaged
    global dispim
    
    yoorl = thecard['imageUrl']
    img = requests.get(yoorl)
    popper = Image.open(BytesIO(img.content))
    imaged = ImageTk.PhotoImage(popper)
    dispim = canva.create_image(150, 200,image=imaged)
    canva.grid(row=1,column=0)
    
    root.title(thecard['name'] + " - MTG Card Data")
    
    name = Label(ladholder3, text = thecard['name'], font = "Arial 24 bold").grid(row=0,column = 0)
    manacost = Label(ladholder2, text = "Mana Cost: " + thecard['manaCost']).grid(row = 1, column = 1)
    cmc = Label(ladholder2, text = "CMC: " + str(int(thecard['cmc']))).grid(row = 2, column = 1)
    colors = Label(ladholder2, text = "Colors: " + str(thecard['colors'])).grid(row = 3, column = 1)    
    mtgtype = Label(ladholder2, text = "Type: " + thecard['type']).grid(row = 4, column = 1)    
    types = Label(ladholder2, text = "Types: " + str(thecard['types'])).grid(row = 5, column = 1)
    subtypes = Label(ladholder2, text = "Subtypes: " + str(thecard['subtypes'])).grid(row = 6, column = 1)
    rarity = Label(ladholder2, text = "Rarity: " + thecard['rarity']).grid(row = 7, column = 1)
    mtgset = Label(ladholder2, text = "Set Code: " + thecard['set']).grid(row = 8, column = 1)
    setname = Label(ladholder2, text = "Set: " + thecard['setName']).grid(row = 9, column = 1)
    oracletext =  Label(ladholder2, text = "Oracle Text: " + thecard['text'], wraplength = 150).grid(row = 10, column = 1)
    artist = Label(ladholder2, text = "Artist: " + thecard['artist']).grid(row = 31, column = 1)

    ladholder2.grid(row = 0, column = 1, rowspan = 2)
    ladholder3.grid(row = 0, column = 0)


loader = Button(ladholder, text = "Load", command = pullcard)
loader.grid(row = 2, column = 1)



root.mainloop()
