import os, shutil
 
path = input("Enter the path to the directory you want to operate on: ")
if os.path.exists(path):
    if os.path.isdir(path):
        if not os.path.exists(os.path.join(path, 'pdf')):
            os.mkdir(os.path.join(path, 'pdf'))
        if not os.path.exists(os.path.join(path, 'doc')):
            os.mkdir(os.path.join(path, 'doc'))
        
        files = os.listdir(path)
        for file in files:
            if file.endswith('.pdf'):
                #add to the pdf directory
                shutil.move(os.path.join(path, file), os.path.join(path, 'pdf'))
            if file.endswith('.doc') or file.endswith('.docx'):
                #add to the doc directory
                shutil.move(os.path.join(path, file), os.path.join(path, 'doc'))

    else:
        print("Path is not a directory")
else:
    print("Path does not exist")
        
