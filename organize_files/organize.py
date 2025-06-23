import os
import shutil

def organize_files(files, path):
    for file in files:
        if os.path.isfile(file):
            filename, extension = os.path.splitext(file)
            extension = extension[1:] 
            destination_dir = os.path.join(path, extension)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                shutil.move(file, os.path.join(destination_dir, os.path.basename(file)))

path = input("Enter path: ")
files = os.listdir(path)
print(files)
organize_files(files, path)
