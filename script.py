from threading import Thread
from subprocess import *
from time import sleep
from gtts import gTTS
from playsound import playsound
from datetime import *
from os import *
from prettytable import PrettyTable
#In windows run the script in git bash 
call_log=set()
def speak(text):
    gTTS(text=text,lang='en').save('speak.mp3')
    playsound('speak.mp3')
    remove('speak.mp3')
def caller():
    call_string=''
    while True:
        check_cmd='adb shell dumpsys telephony.registry | grep "mCallState\|mCallIncomingNumber"'
        call_pid=Popen(check_cmd,shell=True,stdin=PIPE,stdout=PIPE)
        good,bad=call_pid.communicate()
        data=good.decode().split()
        phone=data[1]
        phone_call=phone.split('=')[-1]
        call_state=data[0].split('=')[-1]
        if phone_call:
            call_string=phone_call+f' IN {datetime.now().hour}:{str(datetime.now().minute).zfill(2)}  '
            speak(f'Incoming call from {phone_call[3:]}')
        if int(call_state)==2:
            if call_string:
                k=call_string.split()
                if len(k)==3:
                    k.append('RETRIEVED')
                call_string=" ".join(k)
        if call_string:
            call_log.add(call_string)
        sleep(1)

incoming_call_thread=Thread(target=caller)#Declaring the thread
incoming_call_thread.start()#Starting the thread
while True:
    print('Options:-\n1 to call someone\n2.backup ur images to laptop\n3.get call log\n5.lock ur phone')
    k=int(input('enter option '))
    if k==1:
        phone_num=input('enter mobile number with country code ')
        cmd=f'adb shell am start -a android.intent.action.CALL -d tel:{phone_num}'
        call_log.add(phone_num+f' OUT {datetime.now().hour}:{str(datetime.now().minute).zfill(2)}'+' CALLED')
        print(call_log)
        Popen(cmd,stdin=PIPE,stdout=PIPE,shell=True)
    elif k==2:
        fol_path=input('enter folder path')
        cmd=f'adb pull /sdcard/DCIM/Camera {fol_path}'
        Popen(cmd,shell=True,stdin=PIPE,stdout=PIPE)
    elif k==3:
        print('Your call log from this laptop')
        if len(call_log)!=0:
            try:
                call_log_table=PrettyTable(["Phone Number","State","Time","Stats"])
                mapper=list(map(lambda x:x.split(),call_log))
                mapper.sort(key=lambda x:x[2],reverse=True)
                for i in mapper:
                    if len(i)==3:
                        i.append('MISSED')
                    call_log_table.add_row(i)
                print(call_log_table)
            except:
                print('error')
        else:
            print('no calls upto now')
    elif k==4:
        cmd='adb shell input keyevent 26'
        Popen(cmd,shell=True,stdin=PIPE,stdout=PIPE)