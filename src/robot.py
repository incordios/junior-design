import sys
import socket
import selectors
import traceback
import multiprocessing
import time
import keyboard 
import threading

from Protocol import libserver
from Protocol import libclient

from Utils.robotUtils import create_request, listen_for_director, start_connection, initiate_connection

ROBOT_NAME = "<INSERT MATCHING ROBOT NAME IN CSV FILE"
HOST = "<DIRECTOR IP ADDR>"
PORT = # DIRECTOR LISTENING PORT 

LISTEN_PORT = # ROBOT LISTEN PORT

if __name__ == "__main__":
  print('Register with director...')
  registration_request = create_request(ROBOT_NAME, "Register", LISTEN_PORT) 
  initiate_connection(DIRECTOR_HOST, PORT, registration_request, libclient)
  print('Finished registration, booting up server to listen...')
  
  while True:
    msg = listen_for_director('0.0.0.0', LISTEN_PORT, libserver)
    print(msg)
    if msg['value'] == 'break':
      break
      
    print('Main Loop recieved ', msg, ' so will start to do corresponding task')
    # READ THE MESSAGE AND DO WHATEVER YOUR ROBOT WILL DO.
    while True:
        if GPIO.input(40) == 1:
            speak("""if you can hear this
            the audio system is working""")
            sleep(1)
            oscillate(2)
            speak("""if the motors oscillated twice
            the motor system is working""")
            sleep(1)
            speak("""lastly, the LEDs should start blinking""")
            for _ in range(3):
                sleep(1)
                led.on()
                sleep(1)
                led.off()
                sleep(1)
        else:
            # connect to director
            
            # wait for lines
            
            # Motor - adjust constants for arm
            t1 = threading.Thread(target=oscillate, args=(5,))
            t2 = threading.Thread(target=speak, args=(
            """Who's ready for tea? We have all kinds! Earl Grey, English Breakfast
            Chamomile, and iced. And birthdays are my favorite celebrations
            so I knew I had to prepare accordingly.""",))
            
            t1.start()
            t2.start()
         
            #join the threads
            t1.join()
            t2.join()

            GPIO.cleanup()
