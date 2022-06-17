import subprocess
def save(stuffToStore, title):
    f = open(title + '.sv', 'w')
    f.write(stuffToStore)
    f.close()