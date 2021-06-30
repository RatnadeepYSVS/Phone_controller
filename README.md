# Phone_controller
  This script allows you to control your phone from your laptop.  
  You can make calls, backup your photos and lock your phone from your laptop.      
  You can also recieve calllogs.  
  You can see all incoming calls.But outgoing calls are only seen when a call is made from ur laptop.  
  You can also see missed calls.      
  This script also gives you voice alert for incoming calls.  
# Requirements
  ## IMP:- This Script Only works on android devices   
  #### For Laptop    
  To achieve this you need to have ADB installed on your pc  
  ADB-Android Device Bridge is a CLI tool that allows you to control your mobile from your PC  
  [ADB Docs](https://developer.android.com/studio/command-line/adb)   
  [ADB Installation](https://www.youtube.com/watch?v=26GI3z6tI3E&t=80s&ab_channel=Ssj6)
  #### For Mobile(Only Android)
  ### Imp points
  ##### 1. No need to root your phone as gaining access with ADB is safe.
  ##### 2. Connect only to the PCs you recognize, as the connected PC will be able to access your phone data.
  ##### 3. Turn on developer options in your phone to gain access. 
  ### Steps for turning ON developer options 
  1 Go to ur **settings** and go to **about phone**    
  2 Then go to **Software Information**    
  3 Then U will see an option called **build number and tap it 7 times**  
  Then it will ask u your phone passcode enter it    
  Then you will see developer options right below **about phone**  
  ### Connecting ur phone to laptop via ADB
  After going to the developer options, turn on the USB debugging option (we will be using usb only once to setup) in your mobile    
  connect ur phone with usb to laptop and open cmd prompt    
  run the cmd `adb devices`    
  it will show list of devices(which is only one)    
  then run cmd `adb tcpip 5555` and turn off usb-debugging      
  then open developer options and enable the option wireless-debugging make sure to check the checkbox prompt there  
  IMP:-Your PC and phone must be connected to the same wifi network  
  know ur phone ip then run cmd `adb connect yourphoneip`  
  You are almost set now.  
  To test just type adb devices     
  it will show u an o/p like this    
  `list of devices attached`    
  `192.168.X.X:5555  device`    
   In place of device if it is showing offline, restart ur mobile and enable .     
   Your setup is done.   
   u can also play with the adb environment  
   make sure to checkout the docs for more info.
 # Working 
   clone the repo by `git clone https://github.com/RatnadeepYSVS/Phone_controller.git`  
   and navigate to it by `cd Phone_controller`  
   before running the python script run setup.bat file to pip install required modules      
   then run cmd `python script.py`  
# Updates & Feedback
   More features will be added in upcoming days  
   Improvements and PR's Accepted (: 
   
  

  
  
  
  
