#!/usr/bin/env python3

fole = input("File? ")
fyle = fole + ".dck"

with open(fyle) as file_object:
    lines = file_object.readlines()

deck = []

for line in lines:
    b1 = line.find("[")
    b2 = line.find("]")

    nl = line.replace(line[b1:b2 + 1], "")

    deck.append(nl)
    
    
leg = fole + ".txt"

deck[-1] = ""
deck[-2] = ""

with open(leg, "w") as file_object:
    for thing in deck:
        file_object.write(thing)

        
print("Done!")
