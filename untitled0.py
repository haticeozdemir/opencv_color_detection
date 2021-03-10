# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:07:27 2021

@author: HaticeOzdemir
"""
import numpy as np
import cv2
cap =cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame =cap.read()
    frame = cv2.flip(frame,1)
    #MASK UYGULANIR HSV RENK UZAYI KULLANILIR AYNI RENGİN RENK TONUNU TESPİT ETMEK KOLAYDIR
    #yesil
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #yesil
    lower_green =np.array([54,100,50])
    upper_green =np.array([75,255,255])
    green_mask = cv2.inRange(hsv_frame,lower_green,upper_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    #blue
    lower_blue =np.array([100,150,0])
    upper_blue =np.array([140,255,255])
    blue_mask = cv2.inRange(hsv_frame,lower_blue,upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    

    cv2.imshow("webcam", frame)
    #cv2.imshow("Green mask", green_mask)
    cv2.imshow("green and blue", blue)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()