import os

rcfile = os.path.join(os.path.expanduser("~"),".dircleanrc")
file= open(rcfile,"r")
fileContent = str( file.read())
print(fileContent)
#print(type(fileContent))

thisDict = eval(fileContent)
#print(type(thisDict))
#thisDict = json.load(fileContent)

for key in thisDict:
     #print(key)
     if not os.path.isdir(key):
         os.mkdir(key)

