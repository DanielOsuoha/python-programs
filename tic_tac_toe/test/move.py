import os

destination = os.path.join(os.getcwd(), 'tic_tac_toe/test/test1')
if not os.path.exists(destination):
    os.makedirs(destination)

#construct source and destination paths

src_file = os.path.join(os.getcwd(), 'tic_tac_toe/test/sample_data/readme.md')
dest_file = os.path.join(destination, 'readme.md')
print(dest_file, src_file, destination)
os.rename(src_file, dest_file)
