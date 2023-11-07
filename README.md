# File-manage-using-python

Myself Krupa Bhalani and this is small project in python to learn new things.

I am here to present " AUTO FILE ORGANIZATION "

We all organize files manually but at a moment, it's quite Boring and time consuming. That's why we write Python script that automatically organises all these files.

Firstly, we need to import the required modules i.e. import OS and import shutil

IMPORT OS

The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.

IMPORT SHUTIL

The Shutil module in Python provides many functions of high-level operations on files and collections of files. It also comes under Python's standard utility modules. This module helps in automating the process of copying and removing of files and directories.

Import OS & Import Shutil are in-built modules and don't need to install them.

I have created variable called path which takes the input of the directory path which we wants to organize and then created Variable called names which consists of list of files.

Using os.listdir() : This method returns a list of all the files and folders present inside the specified directory. If no directory is specified then the list of files and folders inside the CWD(CURRENT WORKING DIRECTORY) is returned.

Again created a variable called folder_name which consists of list of Subfolder ' s name

for x in range(0,len(folder_name)): if not os.path.exists

Here os.path.exists() method in Python is used to check whether the specified path exists or not.

And

os.makedirs() : This method creates a directory recursively. It means that while creating a leaf directory if any of the intermediate level directories specified in the path is missing then the method creates them all.

Now for loop condition Using for loop we traverse through every files from names.

If files ends with particular extension And if it is not present in new directory then

shutil.move() method Recursively moves a file or directory (source) to another location (destination) and returns the destination.

Apply this for multiple extensions.

Run this code using F5

See the Output -- It shows

Hurray... It's Done!!

Let's go and check our folders...

Main Folder PBL contains Sub folders Docs, image, pdf, ppt, python, video

Successfully we have shifted files with particular extensions in particular folders.
