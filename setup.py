import os
from os import path
from win10toast import ToastNotifier
toast = ToastNotifier()
directory = os.environ['USERPROFILE'] + "\\Documents\\Paradox Interactive\\Hearts of Iron IV\\" 
try:
    os.listdir(directory)
except:
    directory = os.environ['USERPROFILE'] + "\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\"
if os.path.isfile(directory+"\\settings.txt"):
    setting_file = (directory+"\\settings.txt")
    with open(setting_file, 'r') as file :
        filedata = file.read()
        filedata = filedata.replace('save_as_binary=yes', 'save_as_binary=no')
    with open(directory+"\\settings.txt", 'w') as file:
        file.write(filedata)
    toast.show_toast("Hoi4 Setup","Setting Applied!",duration=5)
else:
    toast.show_toast("Hoi4 Setup","Setup failed, you have to do this by yourself. open \\Documents\\Paradox Interactive\\Hearts of Iron IV\\ and open settings.txt, change \'save_as_binary=yes\' to \'save_as_binary=no\'",duration=20)