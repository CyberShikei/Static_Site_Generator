# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
#
#     It should first delete all the contents of the destination directory to ensure that the copy is clean.
#     It should copy all files and subdirectories, nested files, etc.
#     I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.

# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree

import os
import shutil


def copy_files(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_files(s, d)
        else:
            shutil.copy(s, d)
            print(f"Copying {s} to {d}")
