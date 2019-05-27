from shutil import copyfile
import os
import platform

if platform.system() != 'Windows':
    print("Only Windows is supported")
    exit(1)

print("Copying vscode settings.json")
try:
    copyfile(os.getenv("APPDATA") + "\\Code\\User\\settings.json", os.getcwd() + "\\settings.json")
except IOError:
    print("Error copying vscode settings.json")