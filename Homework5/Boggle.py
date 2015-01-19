from tkinter.filedialog import askopenfilename
from tkinter import *

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
    findFileButton = Button(root, text = 'Find File', command = fileCheck)
    findFileButton.grid(row = 0, column = 0)
    startButton = Button(root, text = 'Start Game', command = playGame)
    startButton.grid(row = 0, column = 1)
    endButton =  Button(root, text = 'End Game', command = quitGame)
    endButton.grid(row = 0, column = 2)
    quitButton = Button(root, text = 'Quit', command = sys.exit)
    quitButton.grid(row = 0, column = 3)
    
def playGame():
    sys.exit()
    
def quitGame():
    sys.exit()


root = Tk()       
root.geometry('300x300')
makeButtons()
    
dice = [['A','E','A','N','E','G'],['W','N','G','E','E','H'],['A','H','S','P','C','O'], ['L','N','H','N','R','Z'],['A','S','P','F','F','K'],['T','S','T','I','Y','D'],['O','B','J','O','A','B'],['O','W','T','O','A','T'],['I','O','T','M','U','C'],['E','R','T','T','Y','L'],['R','Y','V','D','E','L'],['T','O','E','S','S','I'],['L','R','E','I','X','D'],['T','E','R','W','H','V'],['E','I','U','N','E','S'],['N','U','I','H','M','Qu']]

root.mainloop()






