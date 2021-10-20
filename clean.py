
import os

#dir = os.
dir = "~/naran/Downloads"

def readdir(directory):
    for base, dirs, files in os.walk(directory):
    	print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1

    print(f"{base} ma {totalDir}directories {totalFiles} files")

readdir(dir)