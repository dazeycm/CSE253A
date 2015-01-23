import shutil
import os.path

def rename(srcDir, origExt, newExt):
    
    for file in os.listdir(srcDir):
        if file.endswith(origExt):
            curFile = os.path.join(srcDir, file)
            file = file.rsplit(sep = '.', maxsplit = 1)[0]
            file += newExt
            newFile = os.path.join(srcDir, file)
            shutil.copy(curFile, newFile)
            

#test code        
#rename(r'C:\Users\dazeycm\Desktop', '.txt', '.dat')
    