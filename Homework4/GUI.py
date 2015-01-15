from tkinter import *
from tkinter.messagebox import *
import string

#radio button to decide if we want 0x or 0b in front of numbers

root = Tk()
root.title('Dumb Binary Conversions')
titles = ['Binary to Decimal', 'Decimal to Binary', 'Hex to Decimal', 'Decimal to Hex'] 
output = ['Fancy Ouput', 'Not Fancy Ouput']

def fancyPrint():
    print("%s to decimal: %s" % (lastEntered[0], int(btd, 2)))
    print("%s to binary: %s" % (lastEntered[1], bin(int(dtb))))
    print("%s to decimal: %s" % (lastEntered[2], int(htd, 16)))
    print("%s to hex: %s\n" % (lastEntered[3], hex(int(dth))))
    
def boringPrint():
    print(int(btd, 2))
    print(bin(int(dtb)))
    print(int(htd, 16))
    print(hex(int(dth)))

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

def makeRadio(root):
    global radio
    radio = IntVar()
    radio.set(0)
    count = 0
    for str in output:
        r = Radiobutton(root, text = str, padx = 20, variable = radio, value = count).pack(anchor = W)
        count += 1
    
def compute():
    global lastEntered, btd, htd, dtb, dth
    lastEntered = []
    
    btd = entities[0].get()
    dtb = entities[1].get()
    htd = entities[2].get()
    dth = entities[3].get()
    
    for str in (btd, htd, dtb, dth):
        for char in str:
            if char not in string.ascii_letters + string.digits:
                showinfo('Input Error', 'Only enter digits and ascii letters')
                return;
    
    if '0b' in btd:
        showinfo('Input Error in binary to decimal', 'You do not need to explicitly include 0b in binary to decimal')
        return
    elif any([int(i) < 0 or int(i) > 1 for i in btd]):
        showinfo('Input Error in binary to decimal ', 'Numbers must be between 0 and 1 inclusive')
        return   
    
    
    if any([not i.isdigit() for i in dtb]):
        showinfo('Input Error in decimal to binary', 'Only enter digits')
        return;
    
    goodChars = '0123456789ABCEFabcdef'
    if '0x' in htd:
        showinfo('Input Error in hex to decimal', 'You do not need to explicitly include 0x in hex to decimal')
        return
    elif any([i not in goodChars for i in htd]):
        showinfo('Input Error in hex to decimal', 'Input must only contains the characters ' + goodChars)
        return
    
    if any([not i.isdigit() for i in dth]):
        showinfo('Input Error in decimal to hex', 'Only enter digits')
        return;
    
    lastEntered.clear()
    lastEntered.append(btd)
    lastEntered.append(dtb)
    lastEntered.append(htd)
    lastEntered.append(dth)
    
    choice = radio.get()
    if choice == 0:
        fancyPrint()
    else:
        boringPrint()
    
def reset():
    entities[0].delete(0, END)
    entities[0].insert(0, 11111111)
    entities[1].delete(0, END)
    entities[1].insert(0, 255)
    entities[2].delete(0, END)
    entities[2].insert(0, 'ff')
    entities[3].delete(0, END)
    entities[3].insert(0, 255)

entities = makeEntities(root)
reset()
makeRadio(root)

b1 = Button(root, text = 'Compute', command = compute)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text = 'Reset', command = reset)
b2.pack(side = LEFT, padx = 5, pady = 5)
b3 = Button(root, text = 'Quit', command = sys.exit)
b3.pack(side = LEFT, padx = 5, pady = 5)

root.mainloop()