import subprocess
def load(title):
    f = open(title + '.sv', 'r')
    contents = f.read()
    f.close()
    return(contents)