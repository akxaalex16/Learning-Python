from pathlib import Path

# absolute path; a path starting from root of the hard disk
# example: c:\Program Files\Microsoft

# relative path; a path starting from the current directory
# returns True if that path exists:
# path = Path("package")
# print(path.exists())

# to make directory:
# path = Path("emails")
# print(path.mkdir())

# to reomve directory
# path = Path("emails")
# print(path.rmdir())

# path = Path()
# print(path.glob('*.*'))
# '*.*' to get all files and all directories in current path
# '*.py' to search for all py files in current directory
# it gives an object so we can loop through it
path =Path()
for file in path.glob('*.py'):
    print(file)

