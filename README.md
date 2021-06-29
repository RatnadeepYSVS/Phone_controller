# Phone_controller
  This Script allows u to control ur phone from ur laptop.  
  You can make calls store backup of ur mobile photos and lock ur phone from ur laptop.   
  This bot also gives voice alert for incoming calls.  
# Requirements
  ## IMP:- This Script Only works on android devices   
  #### For Laptop    
  To acheive this u need to have adb installed in your pc  
  adb-Android Device Bridge is CLI Tool which allows you to control ur mobile from ur pc  
  [ADB Docs](https://developer.android.com/studio/command-line/adb)   
  [ADB Installation](https://www.youtube.com/watch?v=26GI3z6tI3E&t=80s&ab_channel=Ssj6)
  #### For Mobile(Only Android)
  ### Imp points
  ##### 1.You are not rooting ur phone.Gaining access with adb is safe.
  ##### 2.Connect to a pc that u know it would be best if it's ur personal laptop cause the connected pc can access ur phone's data.    
  ##### 3. To gain access u need to turn on developer options in ur phone.  
  ### Steps for turning ON developer options 
  1 Go to ur settings and go to about phone    
  2 Then go to Software Information    
  3 Then U will see an option called build number and tap it 7 times  
  Then it will ask u your phone passcode enter it    
  ### Connecting ur phone with laptop via ADB
  After going to the developer options turn usb debugging on(we will be using usb only once to setup) in your mobile    
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
   In place of device if it is showing offline restart ur mobile and enable .     
   Your setup is done.   
   u can also play with the adb environment  
   make sure to checkout the docs for more info.
 # Working 
   clone the repo by `git clone https://github.com/RatnadeepYSVS/Phone_controller.git`  
   and navigate to it by `cd Phone_controller`  
   before running the python script run setup.bat file to pip install required modules      
   then run cmd `python script.py`  
   Improvements and PR's Accepted (: 
   
  

  
  
  
  
