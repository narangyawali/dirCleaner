import os

def move(file, source,dest):
    os.rename(os.path.join(source,file), os.path.join(dest,file)) 


def check(fileName):
    music=["mp3", "mp4" ]
    docs=["txt", "pdf" ]
    img=["png", "jpg" ]
    ext=""
    for i in range(3):
        	ext = ext + fileName[-3 +i]
    print(ext)
    if ext in music:
        	move(fileName,Source,Music)
        	print(f"ext {ext} goes in music")
    elif ext in docs:
    		print(f"ext {ext} goes in docs")
    elif ext in img:
        	print(f"ext {ext} goes in picture")
    else:
    		print("no match found you can append it ")



totalFiles =0
total =0
#print(os.getcwd())
Source = os.chdir(os.path.join(os.path.expanduser("~"),"Experiment"))
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




