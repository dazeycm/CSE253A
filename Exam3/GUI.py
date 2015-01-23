from tkinter import *
from tkinter.filedialog import askopenfilename
from statistics import *

def createFileOptions():
    options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = r'C:\Users\Craig\Desktop'
    options['title'] = 'Open source file'
    return options

def openFile():
    global nums
    nums = []
    options = createFileOptions()
    name = askopenfilename(**options)
    try:
        inputFile = open(name)
        for line in inputFile:
            line = line.split()
            for i in line:
                nums.append(i)
        nums = [int(i) for i in nums]
        meanTxt.set('Mean: %.3f' % mean(nums))
        stDevTxt.set('Stdev: %.3f' % stdev(nums))
    except Exception:
        print("Error parsing text file")
        return False
    return True

def makeLabelsandButtons():
    global meanTxt, stDevTxt
    button1 = Button(root, text = 'Open file', command = openFile)
    button1.grid(row = 0, column = 1)
    button2 = Button(root, text = 'Quit', command = sys.exit)
    button2.grid(row = 1, column = 1)
    
    meanTxt = StringVar()
    meanTxt.set('Mean: ' )
    stDevTxt = StringVar()
    stDevTxt.set('Stdev: ')
    mean = Label(root, width = 15, textvariable = meanTxt)
    mean.grid(row = 0, column = 0)
    stdDev = Label(root, width = 15, textvariable = stDevTxt)
    stdDev.grid(row = 1, column = 0)
    fileprocess = Label(root, width = 10, text = 'File processor')
    fileprocess.grid(row = 2, column = 0)

root = Tk()
makeLabelsandButtons()

root.mainloop()