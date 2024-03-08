import subprocess
import os
def save(stuffToStore, title, filer):
    f = open('C:\\Users\\Reynolds\\Documents\\PYaveSaveFiles\\save\\' + os.path.dirname(os.path.realpath(filer)).replace("\\", "À").replace(":", "Æ") + "ß" + title + '.sv', 'w')
    f.write(stuffToStore)
    f.close()

def share(stuffToStore, title):
    f = open('C:\\Users\\Reynolds\\Documents\\PYaveSaveFiles\\' + title + '.sv', 'w')
    f.write(stuffToStore)
    f.close()
