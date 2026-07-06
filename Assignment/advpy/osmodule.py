import os
#print(dir(os))
print(os.getcwd())  # returns the current working directory
#print(os.chdir('C:\\Users\\len 25in\\Documents\\A1\\Assignment'))  # changes the current working directory to the specified path
#print(os.listdir())  # returns a list of files and directories in the current working directory
#['.git', '.gitignore', 'Assignment', 
# 'data types', 'exception_handleing.py',
# 'FileHandleing', 'for _loop.py', 
# 'Funtions.py', 'if_else.py', 
# 'Numpy and Pandas', 'oop', 'Project', 
# 'README.md','sql']
print(os.name)
print(os.path.abspath('_'))# returns the absolute path of the current working directory
print(os.path.relpath('C:\\Users\\len 25in\\Documents\\A1\\_'))


