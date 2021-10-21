import os
#Source = os.chdir(os.path.join(os.path.expanduser("~"), "Experiment"))
music = ["mp3", "mp4"]
docs = ["txt", "pdf",'pptx']
img = ["png", "jpg"]

def move(file, source, dest):
    os.rename(os.path.join("", file), os.path.join(dest, file))


def check(fileName):
    ext = ""
    ext = fileName[len(fileName)-4:len(fileName)]
    if ext[0]=='.':
        ext = ext[1:len(ext)]
    print(ext)
    if ext in music:            
        	move( fileName, os.getcwd() ,  "Music")
        	print(f"ext {fileName} goes in music")
    elif ext in docs:
        	move( fileName, os.getcwd(), "Documents")
        	print(f"ext {fileName} goes in docs")
    elif ext in img:
        	move( fileName, os.getcwd(),"Pictures")
        	print(f"ext {fileName} goes in picture")
    else:
    		print("no match found you can append it ")




print("---------------")
print(os.getcwd())

dirs= os.listdir()
print(dirs)

for dir in dirs:
    if os.path.isfile(dir):
        check(dir)





