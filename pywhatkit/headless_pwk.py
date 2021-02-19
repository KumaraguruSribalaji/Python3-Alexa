"""Using the following functions too much might get your WhatsApp account hence
by using this library, you agree that the only you will be responsible for any
mishap and you will use this library at your own risk, the creators will not be
responsible for any damage."""

import requests
import re
import time
import os

def sendwhatmsg(phone_no, message, time_hour, time_min, wait_time=20, print_waitTime=True):
    '''Sends whatsapp message to a particulal number at given time
Phone number should be in string format not int
***This function will continue to work even if you turn off the computer
after scheduling the message'''
    print("This function is full of bugs and is under development, it is not guranteed to work with 100% accuracy.")
    print("You will have 10 seconds to scan the QR code after it opens, so keep your phone ready")
    valid_phone_no = re.compile(r"[+]\d{12}")
    numbers = re.findall(valid_phone_no, phone_no)
    phone_no = phone_no.replace("+","")
    #code missing from phone_no
    timehr = time_hour

    if time_hour not in range(0,25) or time_min not in range(0,60):
        print("Invalid time format")
    
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm
    
    
    lefttm = lefttm - 30
    imgurl = requests.get(f"http://headless-pywhatkit.herokuapp.com/send?num={phone_no}&message={message}&delay={lefttm}").text
    ssid = imgurl.split(".com/")[1].split(".png")[0]
    while True:
      status = requests.get(f"http://headless-pywhatkit.herokuapp.com/session-status?id={ssid}").text
      try:
          status = eval(status)[ssid]
      except:
          pass
      if status == "scan_qr":
        data = requests.get(imgurl).content

        with open("img.png","wb") as img:
          img.write(data)
        print("Plese scan the QR code")
        os.startfile("img.png")
        print(f"After {lefttm} seconds of scanning the QR code, the message will be delivered.")
        break


