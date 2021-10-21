import os
#Source = os.chdir(os.path.join(os.path.expanduser("~"), "Experiment"))
Source = ""
music = ["mp3", "mp4"]
docs = ["txt", "pdf"]
img = ["png", "jpg"]

def move(file, source, dest):
    os.rename(os.path.join("", file), os.path.join(dest, file))


def check(fileName):
    ext = ""
    ext = fileName[len(fileName)-3:len(fileName)]
    # for i in range(3):
    #     	ext = ext + fileName[-3 + i]
    print(ext)
    if ext in music:
        	print(type(fileName))
            
        	move( fileName, os.getcwd() ,  "Music")
        	print(f"ext {ext} goes in music")
    elif ext in docs:
        	move( fileName, os.getcwd(), "Documents")
        	print(f"ext {ext} goes in docs")
    elif ext in img:
        	move( fileName, os.getcwd(),"Pictures")
        	print(f"ext {ext} goes in picture")
    else:
    		print("no match found you can append it ")



totalFiles =0
total =0
#os.chdir(os.path.join(os.path.expanduser("~"), "Experiment"))
# print(os.getcwd())
print("---------------")
print(os.getcwd())

dirs= os.listdir()
print(dirs)
for all in dirs:
    total += 1
for dir in dirs:
    if os.path.isfile(dir):
        totalFiles += 1
        check(dir)
        print(totalFiles)




