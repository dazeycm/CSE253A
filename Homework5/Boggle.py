from tkinter.filedialog import askopenfilename
from tkinter import *
import random
from tkinter.messagebox import showinfo
from test.test_itertools import minsize
from collections import Counter
import tkinter.messagebox

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
                showinfo('Whoops!', 'Invalid Dictionary')
                return False
            words.append(line[:-1].upper()) #strip new line character
    if not all([words[i] <= words[i + 1] for i in range(len(words) - 1)]):
        showinfo('Whoops!', 'Invalid Dictionary')
        return False
    return True
            
def fileCheck():
    flag = openFile()
    while not flag:
        flag = openFile()
    
def makeButtons():
    findFileButton = Button(row1, text = 'Find File', command = fileCheck)
    findFileButton.grid(row = 0, column = 0)
    startButton = Button(row1, text = 'Start Game', command = playGame)
    startButton.grid(row = 0, column = 1)
    endButton = Button(row1, text = 'End Game', command = quitGame)
    endButton.grid(row = 0, column = 2)
    quitButton = Button(row1, text = 'Quit', command = sys.exit)
    quitButton.grid(row = 0, column = 3)
    aiButton = Button(row3, text = 'AiPlay', command = aiPlay)
    aiButton.grid(row = 0, column = 3)
    
def makeEntryBox():
    global entryBox, madeBox
    entryBox = Entry(row3, justify = CENTER)
    entryBox.grid(row = 0, column = 1)
    madeBox = True
    
def finalScoreText():
    global scoreTxt
    scoreTxt = StringVar()
    scoreTxt.set('')

def aiPlay():
    global score
    variable = tkinter.messagebox.askyesno('Confirmation', 'If you have the Ai play it will reset your current game session. Are you sure you want to do this?')
    if variable == 'no':
        return
    
    score = 0
    try:
        for word in words:
            if checkWord(word, letters):
                score += calcPoints(word)
        quitGame()
    except Exception:
        showinfo('Whoops!', 'Did you forget to select a dictionary?')    

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
        
def checkWord(word, letters, tmpGameWords = []):
    if all(let in letters for let in word) and word in words and word not in tmpGameWords:
        cnt = Counter()
        cntCheck = Counter()
        for lets in word:
            cnt[lets] += 1
        for lets in letters:
            cntCheck[lets] +=1
        for let in cnt:            
            if cnt[let] <= cntCheck[let]:
                continue
            else:
                return False
        return True
    else:
        return False

def processWord(event):
    global score
    try:
        word = entryBox.get()
        word = word.upper()
        entryBox.delete(0, END)
        if checkWord(word, letters, tmpGameWords):
            tmpGameWords.append(word)
            score += calcPoints(word)
        else:
            print('Invalid Word')
    except Exception:
        showinfo('Whoops!', 'Find a dictionary file and start the game before hitting enter!')
    
def calcPoints(word):
    if len(word) <= 2:
        return 0
    elif len(word) <= 4:
        return 1
    elif len(word) == 5:
        return 2
    elif len(word) == 6:
        return 3
    elif len(word) == 7:
        return 5
    elif len(word) >= 8:
        return 11
    
def quitGame():
    global score, scoreTxt
    showinfo('Game Over', 'The final score is in the word box!')
    try:
        for letterLabel in letterLabels:
            letterLabel.set('')
        entryBox.delete(0, END)
        entryBox.insert(0, str(score))
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






