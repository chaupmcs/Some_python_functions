import os


print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path +  "\n"))

print("This file parent path")
print(os.path.abspath(os.path.join(   os.path.dirname(full_path)  , os.pardir))  + "\n" )

print("This file list file")
list_files = os.listdir("D:\\Visualization_5.4\\data\\hourly")
print(list_files)
for element in list_files: print(element)






######### RESULT

# C:\Users>python C:\Users\CPU10902-local\Desktop\Some_PY_CODE\work_with_directory
# .py
# Path at terminal when executing this file
# C:\Users

# This file path, relative to os.getcwd()
# C:\Users\CPU10902-local\Desktop\Some_PY_CODE\work_with_directory.py

# This file full path (following symlinks)
# C:\Users\CPU10902-local\Desktop\Some_PY_CODE\work_with_directory.py

# This file directory and name
# C:\Users\CPU10902-local\Desktop\Some_PY_CODE --> work_with_directory.py

# This file directory only
# C:\Users\CPU10902-local\Desktop\Some_PY_CODE
# This file parent path
# C:\Users\CPU10902-local\Desktop

# This file list file
# ['a.csv', 'all.csv', 'all_data_hour_.csv']
# a.csv
# all.csv
# all_data_hour_.csv

# C:\Users>

