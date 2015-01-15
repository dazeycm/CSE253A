from tkinter import *

#radio button to decide if we want 0x or 0b in front of numbers

root = Tk()
root.title('Dumb Binary Conversions')
titles = ['Binary to Decimal', 'Decimal to Binary', 'Hex to Decimal', 'Decimal to Hex'] 
output = ['Fancy Ouput', 'Not Fancy Ouput']

def makeEntities(root):
    entities = []
    for i in range(len(titles)):
        row = Frame(root)
        label = Label(row, width = 20, text = titles[i], anchor = 'w')
        entry = Entry(row)
        label.grid(row = 0, column = 0)
        entry.grid(row = 0, column = 1)
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        entities.append(entry)
    return entities
        
entities = makeEntities(root)

def makeRadio(root):
    radios = []
    for str in output:
        r = Radiobutton(root, text = str, padx = 20, variable = radio, value = str).pack(anchor = W)
        radios.append(r)
        
def compute():
    print("Nothing")
    
def reset():
    print("Nothing 2")

radio = IntVar()
radio.set(0)

radios = makeRadio(root)

b1 = Button(root, text = 'Compute', command = compute)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text = 'Reset', command = reset)
b2.pack(side = LEFT, padx = 5, pady = 5)
b3 = Button(root, text = 'Quit', command = sys.exit)
b3.pack(side = LEFT, padx = 5, pady = 5)
root.mainloop()