import sys
import socket
import selectors
import traceback
import multiprocessing
import time
import threading

from Protocol import libserver
from Protocol import libclient

from Utils.robotUtils import (
    get_ipv4,
    create_request,
    listen_for_director,
    start_connection,
    initiate_connection,
)

from Utils.motorUtils import (
    oscillate,
    testMode,
    ledOn,
    ledOff,
)

from Utils.audioUtils import (
    speak,
)

ROBOT_NAME = "Robot1"
DIRECTOR_HOST = "127.0.0.1"
PORT = 65432

SELF_HOST = "127.0.0.1"
LISTEN_PORT = 8000

if __name__ == "__main__":
    print("Register with director...")

    registration_request = create_request(ROBOT_NAME, "Register", LISTEN_PORT)
    initiate_connection(DIRECTOR_HOST, PORT, registration_request, libclient)

    print("Finished registration, booting up server to listen...")

    while True:
        msg = listen_for_director(SELF_HOST, LISTEN_PORT, libserver)

        print(msg)
        if msg["value"] == "break":
            break
        
        if msg:
            print("Main Loop recieved ", msg, " so will start to do corresponding task")
            speak(msg["value"])
        
        #test mode is never run, bc this if statement is not in parallel
        if testMode():
            speak(
                """if you can hear this
        the audio system and wifi is working"""
            )
            time.sleep(1)
            oscillate(2)
            speak(
                """if the motors oscillated twice
        the motor system is working"""
            )
            time.sleep(1)
            speak("""lastly, the L.E.D light should start blinking""")
            for _ in range(3):
                time.sleep(1)
                ledOn()
                time.sleep(1)
                ledOff()
                time.sleep(1)
            speak(
                """flip the switch off to stop the test mode from
        continuing"""
            )
            time.sleep(2)

