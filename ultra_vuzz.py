import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
TRIG = 16                                  
ECHO = 18                                  

GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)                   
#buzzer=7 
#GPIO.setup(buzzer,GPIO.OUT)
    
while True:

  GPIO.output(TRIG, False)        
  time.sleep(0.5)                            
  
  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 171.50        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance < 1.2: 
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(0.5) # Delay in seconds		     #Check whether the distance is within range
    print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
  else:
    #GPIO.output(buzzer,GPIO.LOW)
    #print ("No Beep")
    sleep(0.5)
    print ("Out Of Range")                   #display out of range
