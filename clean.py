import os
#Source = os.chdir(os.path.join(os.path.expanduser("~"), "Experiment"))


def reqdir():
    rcfile = os.path.join(os.path.expanduser("~"), ".dircleanrc")
    file = open(rcfile, "r")
    fileContent = str(file.read())
    thisDict = eval(fileContent)
    for key in thisDict:
        # print(key)
        if not os.path.isdir(key):
            os.mkdir(key)
    return thisDict


def move(file, source, dest):
    os.rename(os.path.join("", file), os.path.join(dest, file))


def check(fileName):
    ext = ""
    ext = fileName[len(fileName)-4:len(fileName)]
    if ext[0] == '.':
        ext = ext[1:len(ext)]
    thisDict = reqdir()
    for key in thisDict:
        if ext in thisDict[key]:
            move(fileName, os.getcwd(), key)
            print(f" {fileName} goes in {key} ")
            return
            
print("---------------")
print(os.getcwd())

dirs = os.listdir()
print(dirs)
print("---------------")

for dir in dirs:
    if os.path.isfile(dir):
        check(dir)
