from threading import Thread
from subprocess import *
from time import sleep
from gtts import gTTS
from playsound import playsound
from datetime import *
from os import *
from prettytable import PrettyTable
#In windows run the script in git bash 
missed_call_list=set()
incoming_call=''
call_log=set()
def speak(text):
    gTTS(text=text,lang='en').save('speak.mp3')
    playsound('speak.mp3')
    remove('speak.mp3')
def caller():
    while True:
        check_cmd='adb shell dumpsys telephony.registry | grep "mCallState\|mCallIncomingNumber"'
        call_pid=Popen(check_cmd,shell=True,stdin=PIPE,stdout=PIPE)
        good,bad=call_pid.communicate()
        data=good.decode().split()
        phone=data[1]
        phone_call=phone.split('=')[-1]
        accepted=False
        call_state=data[0].split('=')[-1]
        if phone_call:
            incoming_call=phone_call
            call_log.add(incoming_call+f' IN {datetime.now().hour}:{str(datetime.now().minute).zfill(2)}')
            speak(f'Incoming call from {phone_call[3:]}')
            sleep(1)
        if not accepted and phone_call:
            missed_call_list.add(phone_call)
        if int(call_state)==2:
            accepted=True
            try:
                missed_call_list.discard(incoming_call)
                incoming_call=''
            except UnboundLocalError:
                pass
        sleep(1)

incoming_call_thread=Thread(target=caller)#Declaring the thread
incoming_call_thread.start()#Starting the thread
while True:
    print('Options:-\n1 to call someone\n2.backup ur images to laptop\n3.get missed call or calls u have cut stats\n4.get call log\n5.lock ur phone')
    k=int(input('enter option '))
    if k==1:
        phone_num=input('enter mobile number with country code ')
        cmd=f'adb shell am start -a android.intent.action.CALL -d tel:{phone_num}'
        if phone_num in missed_call_list:
            missed_call_list.discard(phone_num)
        call_log.add(phone_num+f' OUT {datetime.now().hour}:{str(datetime.now().minute).zfill(2)}')
        Popen(cmd,stdin=PIPE,stdout=PIPE,shell=True)
    elif k==2:
        fol_path=input('enter folder path')
        cmd=f'adb pull /sdcard/DCIM/Camera {fol_path}'
        Popen(cmd,shell=True,stdin=PIPE,stdout=PIPE)
    elif k==3:
        if len(missed_call_list):
            print(f'Calls U ended up or missed')
            missed_call_table=PrettyTable(["Phone Numbers"])
            for i in list(missed_call_list):
                missed_call_table.add_row([i])
            print(missed_call_table)
        else:
            print("You didn't miss or cut any call")
    elif k==4:
        print('Your call log from this laptop')
        if len(call_log):
            call_log_table=PrettyTable(["Phone Number","Stats","Time"])
            mapper=list(map(lambda x:x.split(),call_log))
            mapper.sort(key=lambda x:x[2],reverse=True)
            for i in mapper:
                call_log_table.add_row(i)
            print(call_log_table)
    elif k==5:
        cmd='adb shell input keyevent 26'
        Popen(cmd,shell=True,stdin=PIPE,stdout=PIPE)