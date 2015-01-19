from tkinter.filedialog import askopenfilename
from tkinter import *
import random

def createFileOptions():
    options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = r'C:\Users\Craig\Desktop\english'
    options['title'] = 'Open source file'
    return options

def openFile():
    global words
    words = []
    options = createFileOptions()
    name = askopenfilename(**options)
    if name != '':
        inputFile = open(name)
        for line in inputFile:
            if ' ' in line:
                print('Invalid dictionary')
                return False
            words.append(line)
    if not all([words[i] <= words[i + 1] for i in range(len(words) - 1)]):
        print('Invalid dictionary')
        return False
    return True
            
def fileCheck():
    flag = openFile()
    while not flag:
        print('failure')
        flag = openFile()
    print('success')
    
def makeButtons():
    findFileButton = Button(row1, text = 'Find File', command = fileCheck)
    findFileButton.grid(row = 0, column = 0)
    startButton = Button(row1, text = 'Start Game', command = playGame)
    startButton.grid(row = 0, column = 1)
    endButton = Button(row1, text = 'End Game', command = quitGame)
    endButton.grid(row = 0, column = 2)
    quitButton = Button(row1, text = 'Quit', command = sys.exit)
    quitButton.grid(row = 0, column = 3)
    
def playGame():
    showBoard()
    
def quitGame():
    for letterLabel in letterLabels:
        letterLabel.set('')
        

def showBoard():
    global letterLabels
    letterLabels = []
    get16RandDice()
    for i in range(16):
        txt = StringVar()
        txt.set(letters[i])
        die = Label(row2, width = 2, textvariable = txt)
        die.grid(row = i // 4, column = i % 4)
        letterLabels.append(txt)
    
def get16RandDice():
    global letters 
    letters = []
    count = 0
    for die in dice:
        rand = random.randint(0, 5)
        letters.append(die[rand])
    

root = Tk()  
root.geometry('225x150')
row1 = Frame(root)
row2 = Frame(root)
score = 0
makeButtons()
 
dice = [['A','E','A','N','E','G'],['W','N','G','E','E','H'],['A','H','S','P','C','O'], ['L','N','H','N','R','Z'],['A','S','P','F','F','K'],['T','S','T','I','Y','D'],['O','B','J','O','A','B'],['O','W','T','O','A','T'],['I','O','T','M','U','C'],['E','R','T','T','Y','L'],['R','Y','V','D','E','L'],['T','O','E','S','S','I'],['L','R','E','I','X','D'],['T','E','R','W','H','V'],['E','I','U','N','E','S'],['N','U','I','H','M','Qu']]

row1.pack()
row2.pack()
root.mainloop()






