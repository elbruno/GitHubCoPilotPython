import os

# list all the files that contain the word "work" in the current directory
# and all subdirectories
for root, dirs, files in os.walk("."):
    for file in files:
        if "work" in file:
            print(os.path.join(root, file))


import os

# list all the files bigger than 4MB
for file in os.listdir():
    if os.path.getsize(file) > 4000000:
        print(file)