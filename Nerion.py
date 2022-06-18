import numpy as np
import cv2
import pyautogui
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
#from pynput.keyboard import Key, Controller #obsolete
import time
import webbrowser 
from datetime import datetime


while(1):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    decodedObjects = pyzbar.decode(image)
    now = datetime.now()
    print("Scan completed: ", now.strftime("%H:%M:%S"),"\n")
    url = ""
    for obj in decodedObjects:
        print("Type:", obj.type)
        url = obj.data
        print("Data: ", obj.data, "\n")
    if(decodedObjects):
        webbrowser.open_new_tab(url) 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Code Recorded at", current_time,"\n")
        print("Program will wait for 30 seconds before resume scanning.")
        time.sleep(30)                                 
    time.sleep(5)
