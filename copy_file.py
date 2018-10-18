import re
import shutil

path_file = '/home/the_file.txt'
destination = '/home/dest_folder'


with open(path_file, 'r') as f:
    x = f.readlines()


for s in x:
    path = re.sub('.*?/', '/', s, 1).strip()
    shutil.copy2(path, destination)
