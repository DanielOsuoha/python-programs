import os
import shutil

def organize_files(files, path):
    for file in files:
        if os.path.isfile(file):
            # Get the file extension
            filename, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove the dot from extension
            
            # Create directory if it doesn't exist
            destination_dir = os.path.join(path, extension)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            # Move file to destination directory
            shutil.move(file, os.path.join(destination_dir, os.path.basename(file)))

# Example usage:
path = input("Enter path: ")
files = os.listdir(path)
print(files)
organize_files(files, path)
