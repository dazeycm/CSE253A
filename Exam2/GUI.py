from tkinter import *

root = Tk()
root.title('Sample')

def makeEntities(root):
    numsToAdd = []
    row = Frame(root)
    numOne = Entry(row)
    numTwo = Entry(row)
    numOne.grid(row = 0, column = 0)
    numTwo.grid(row = 0, column = 1)
    row.pack(side = TOP, fill = X, padx = 5, pady = 5)
    numOne.insert(0, 0)
    numTwo.insert(0, 0)
    numsToAdd.append(numOne)
    numsToAdd.append(numTwo)
    return numsToAdd

def process():
    print("Process called")
    numOne = int(nums[0].get())
    numTwo = int(nums[1].get())
    total = numOne + numTwo
    print("Total: %d" % total)

nums = makeEntities(root)
b1 = Button(root, text = 'Process', command = process)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text = 'Quit', command = sys.exit)
b2.pack(side = LEFT, padx = 5, pady = 5)

root.mainloop()