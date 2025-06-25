import os
input("Notice: This script uses ImageMagick. If you do not have ImageMagick installed, the program will not function.\nPress enter to continue")
try:
    files = os.listdir("downloads")
    i = 0
    while i < len(files):
        if files[i][-4:] != ".tga":
            files.remove(files[i])
        else:
            files[i] = files[i][:-4]
            i+=1
    print("")
    for i in files:
        print(f"\rAdding {i}...")
        os.system(f"magick downloads/{i}.tga -resize 400% -quality 100% icons/{i}.jpg")
    os.system("cd ..")
    print("Icons added.")
except:
    print('The "downloads" or "icons" directory does not exist.')