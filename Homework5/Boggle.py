from tkinter.filedialog import askopenfilename
from tkinter import *
import random
from tkinter.messagebox import showinfo
from test.test_itertools import minsize

def createFileOptions():
    options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = r'C:\Users\Craig\Desktop'
    options['initialfile'] = r'C:\Users\Craig\Desktop\english'
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
            words.append(line[:-1].upper()) #strip new line character
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
    
def makeEntryBox():
    global entryBox, madeBox
    entryBox = Entry(row3, justify = CENTER)
    entryBox.grid(row = 0, column = 1)
    madeBox = True
    createFakeLabel()
    
def finalScoreText():
    global scoreTxt
    scoreTxt = StringVar()
    scoreTxt.set('')
    finalScoreLabel = Label(row3, width = 6, textvariable = scoreTxt)
    finalScoreLabel.grid(row = 0, column = 0)

def playGame():
    global score, tmpGameWords
    tmpGameWords = []
    score = 0
    try:
        len(words)
    except Exception:
        showinfo('Whoops!', 'You need to select a dictionary first!')
        return
        
    showBoard()
    finalScoreText()
    scoreTxt.set('')
    if not madeBox:
        makeEntryBox()
        
def checkWord(word, letters, tmpGameWords):
    if all(let in letters for let in word) and word in words and word not in tmpGameWords:
        return True
    else:
        return False

def processWord(event):
    global score
    checkWord('hello', ['hello'], ['hello'])
    #try:
    word = entryBox.get()
    word = word.upper()
    entryBox.delete(0, END)
    if checkWord(word, letters, tmpGameWords):
        print('okay')
        tmpGameWords.append(word)
    else:
        print('not okay')
    #except Exception:
    #    showinfo('Whoops!', 'Find a dictionary file and start the game before hitting enter!')
    
def quitGame():
    global score, scoreTxt
    try:
        for letterLabel in letterLabels:
            letterLabel.set('')
        print('Your score was %d' % score)
        score = 0
        scoreTxt.set('Score')
    except Exception:
        showinfo('Whoops!', "You haven't started a game yet!")
        
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
        
    return letterLabels
    
def get16RandDice():
    global letters
    letters = []
    count = 0
    for die in dice:
        rand = random.randint(0, 5)
        letters.append(die[rand])
    
#this is needed to ensure that the entry box is centered under the boggle board
def createFakeLabel():
    fakeLabel = Label(row3, width = 6)
    fakeLabel.grid(row = 0, column = 3)

root = Tk()  
root.title('Boggle!')
root.geometry('225x150')
showinfo('WELCOME!', 'To play: Find a dictionary file, press start game, enter your word in the box and press enter!')
root.bind('<Return>', processWord)

row1 = Frame(root)
row2 = Frame(root)
row3 = Frame(root)
row1.pack()
row2.pack()
row3.pack()

makeButtons()

madeBox = False 
dice = [['A','E','A','N','E','G'],['W','N','G','E','E','H'],['A','H','S','P','C','O'], ['L','N','H','N','R','Z'],['A','S','P','F','F','K'],['T','S','T','I','Y','D'],['O','B','J','O','A','B'],['O','W','T','O','A','T'],['I','O','T','M','U','C'],['E','R','T','T','Y','L'],['R','Y','V','D','E','L'],['T','O','E','S','S','I'],['L','R','E','I','X','D'],['T','E','R','W','H','V'],['E','I','U','N','E','S'],['N','U','I','H','M','Qu']]

root.mainloop()






