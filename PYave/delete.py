import os
def saved(title, filer):
    os.remove('C:\\Users\\Reynolds\\Documents\\PYaveSaveFiles\\save\\' + os.path.dirname(os.path.realpath(filer)).replace("\\", "À").replace(":", "Æ") + "ß" + title + '.sv')

def shared(title):
    os.remove('C:\\Users\\Reynolds\\Documents\\PYaveSaveFiles\\' + title + '.sv')

