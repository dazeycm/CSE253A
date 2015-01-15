from tkinter import *

root = Tk()
root.title('Dumb Binary Conversions')
titles = ['Binary to Decimal', 'Decimal to Binary', 'Hex to Decimal', 'Decimal to Hex'] 

def binaryToDecimal(num):
    total = 0
    for i in num:
        print(i)
        

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

def compute():
    print("Nothing")
    
def reset():
    print("Nothing 2")

b1 = Button(root, text = 'Compute', command = compute)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text = 'Reset', command = reset)
b2.pack(side = LEFT, padx = 5, pady = 5)
b3 = Button(root, text = 'Quit', command = sys.exit)
b3.pack(side = LEFT, padx = 5, pady = 5)
root.mainloop()