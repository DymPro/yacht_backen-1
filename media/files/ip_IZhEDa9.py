import os

path = "/home/tano/Desktop/for-koko/public/assets/video"

files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(f"assets/video/{file}")

print(files)
