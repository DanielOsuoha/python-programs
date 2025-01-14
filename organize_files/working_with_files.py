import os

def file_exists():
    if os.path.exists('test.txt'):
        os.remove('test.txt')
    else:
        print("The path does not exist")
    
def check_modification(file):
    import datetime
    timestamp = os.path.getmtime(file)
    print(datetime.datetime.fromtimestamp(timestamp))
    
# check_modification('organize.py')


def check_size_type(file):
    if os.path.isfile(file):
        print("The object passed is a file")
        print('The size of the file:', os.path.getsize(file))
    else:
        print("The object is not a file")

def count_files_directories(path):
    count_files = 0
    count_directories = 0
    for name in os.listdir(path):
        filename = os.path.join(path, name)
        if os.path.isdir(filename):
            count_directories += 1
        else:
            count_files += 1
    return count_files, count_directories

print(count_files_directories('../../'))
