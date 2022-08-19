import subprocess
import os
def load(title, filer):
    f = open('C:\\Users\\Reynolds\\Documents\\PYaveSaveFiles\\save\\' + os.path.dirname(os.path.realpath(filer)).replace("\\", "À").replace(":", "Æ") + "ß" + title + '.sv', 'r')
    contents = f.read()
    f.close()
    return(contents)

def get(title):
    f = open('C:\\Users\\Reynolds\\Documents\\PYaveSaveFiles\\' + title + '.sv', 'r')
    contents = f.read()
    f.close()
    return(contents)

