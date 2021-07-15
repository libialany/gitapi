import os
def run(**args):
    print " [*] In dirlister module. "
    files = os.listdir(".")
    print(files)
    return str(files)
##Expose all of the files
