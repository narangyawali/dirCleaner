
ram = "nara.yan"
print("-----------------")



music=["mp3", "mp4"]
docs=["txt","pdf"]
img=["png","jpg"]
ext=""
for i in range(3):
	ext = ext + fileName[-3 +i]
print(ext)
if ext in music:
        print(f"ext {ext} goes in music")
elif ext in docs:
    	print(f"ext {ext} goes in music")
elif ext in img:
        print(f"ext {ext} goes in music")
else:
    print("no match found you can append it ")