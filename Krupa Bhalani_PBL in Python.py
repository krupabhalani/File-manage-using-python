import os
import shutil

try:
    path = input("Enter Path: ")
    names = os.listdir(path)
    folder_name = ['PDF','PPT','VIDEO','IMAGE','PYTHON','DOCS']
    for x in range(0,len(folder_name)):
        if not os.path.exists(path + '/' + folder_name[x]):
            os.makedirs(path + '/' + folder_name[x])
    for files in names:
        if files.endswith(".png") or files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".jfif") and not os.path.exists(path + '/IMAGE/' + files):
            shutil.move(path + '/' + files, path + '/IMAGE/' + files)
        if files.endswith(".pdf") and not os.path.exists(path + '/PDF/' + files):
            shutil.move(path + '/' + files, path + '/PDF/' + files)
        if files.endswith(".py") or files.endswith(".ipynb") and not os.path.exists(path + '/PYTHON/' + files):
            shutil.move(path + '/' + files, path + '/PYTHON/' + files)
        if files.endswith(".ppt") or files.endswith(".pptx") and not os.path.exists(path + '/PPT/' + files):
            shutil.move(path + '/' + files, path + '/PPT/' + files)
        if files.endswith(".doc") or files.endswith(".docx") and not os.path.exists(path + '/DOCS/' + files):
            shutil.move(path + '/' + files, path + '/DOCS/' + files)
        if files.endswith(".mp4") and not os.path.exists(path + '/VIDEO/' + files):
            shutil.move(path + '/' + files, path + '/VIDEO/' + files)
    print("It's Done !! Hurray...")

except:
    print("Error Error...")