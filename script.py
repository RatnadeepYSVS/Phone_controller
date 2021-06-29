from threading import Thread
from subprocess import *
from time import sleep
from gtts import gTTS
from playsound import playsound
from os import *
#If U are on windows run the script in git bash 
def speak(text):
    gTTS(text=text,lang='en').save('speak.mp3')
    playsound('speak.mp3')
    remove('speak.mp3')
def caller():
    while True:
        check_cmd='adb shell dumpsys telephony.registry | grep "mCallState\|mCallIncomingNumber"'
        call_pid=Popen(check_cmd,shell=True,stdin=PIPE,stdout=PIPE)
        good,bad=call_pid.communicate()
        data=good.decode().split()[1]
        filt_data=data.split('=')[-1]
        if filt_data!='':
            speak(f'Incoming call from {filt_data[3:]}')
            sleep(2)
incoming_call_thread=Thread(target=caller)
incoming_call_thread.start()
while True:
    print('Options:-\n1 to call someone\n2.backup ur images to laptop\n3.lock ur phone')
    k=int(input('enter option '))
    if k==1:
        phone_num=input('enter mobile number ')
        cmd=f'adb shell am start -a android.intent.action.CALL -d tel:+91{phone_num}'
        Popen(cmd,stdin=PIPE,stdout=PIPE,shell=True)
    elif k==2:
        print('backing up photos -----')
        fol_path=input('enter folder path')
        cmd=f'adb pull /sdcard/DCIM/Camera {fol_path}'
        Popen(cmd,shell=True,stdin=PIPE,stdout=PIPE)
    elif k==3:
        cmd='adb shell input keyevent 26'
        Popen(cmd,shell=True,stdin=PIPE,stdout=PIPE)
