import subprocess
def save(stuffToStore, title):
    f = open(title + '.sv', 'w')
    f.write(stuffToStore)
    f.close()
    #subprocess.check_call(["attrib","+H",title + ".sv"])

def load(title):
    f = open(title + '.sv', 'r')
    contents = f.read()
    f.close()
    return(contents)