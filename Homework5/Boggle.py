from tkinter.filedialog import askopenfilename
from tkinter.tix import Tk

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
                break
            words.append(line)
            
root = Tk()           
dice = [['A','E','A','N','E','G'],['W','N','G','E','E','H'],['A','H','S','P','C','O'], ['L','N','H','N','R','Z'],['A','S','P','F','F','K'],['T','S','T','I','Y','D'],['O','B','J','O','A','B'],['O','W','T','O','A','T'],['I','O','T','M','U','C'],['E','R','T','T','Y','L'],['R','Y','V','D','E','L'],['T','O','E','S','S','I'],['L','R','E','I','X','D'],['T','E','R','W','H','V'],['E','I','U','N','E','S'],['N','U','I','H','M','Qu']]
openFile()
root.mainloop()