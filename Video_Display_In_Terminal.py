from bisect import bisect
from PIL import Image
import numpy as np
import random
import math
import cv2
import sys
import os

cap = cv2.VideoCapture('test.mp4')

def convertToText(image):
    greyscale = [
                " ",
                " ",
                ".,-",
                "_ivc=!/|\\~",
                "gjez2]/(YL)t[+T7Vf",
                "mdK4ZGbNDXY5P*Q",
                "W8KMA",
                "#%$"
                ]
    
    zonebounds=[36,72,108,144,180,216,252]
    
    maxLen = 80
    width, height = image.size
    rate = float(maxLen) / max(width, height)
    width = int(rate * width)
    height = int(rate * height)
    
    im = image
    im=im.resize((width, height),Image.BILINEAR)
    im=im.convert("L")
 
    str=""
    for y in range(0,im.size[1]):
        for x in range(0,im.size[0]):
            lum=255-im.getpixel((x,y))
            row=bisect(zonebounds,lum)
            possibles=greyscale[row]
            str=str+possibles[random.randint(0,len(possibles)-1)]
        str=str+"\n"
 
    print(str)



if __name__ == "__main__":
    os.system('cls')

    currentFrame = 0    
    try:
        while(True):
            ret, frame = cap.read()
            if ret != True:
                break
            else:
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                convertToText(frame)

        cap.release()
        cv2.destroyAllWindows()

    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()