from pytube import YouTube
from bisect import bisect
from PIL import Image
import numpy as np
import random
import time
import math
import cv2
import sys
import os

def downloadYoutubeVideo(url):
    video = YouTube(url)
    stream = video.streams.filter(only_video = True, file_extension = "mp4")
    stream.last().download(filename="youtube_video")


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

    if len(sys.argv) < 3:
        print("Error: Input Arguments are wrong")
        print("If you want to convert local video file, the first argument is 'local', and the last is file name.")
        print("If you want to convert youtebe video, the first argument is 'youtube', and the last is youtube link.")
        sys.exit()
    else:
        if str(sys.argv[1]).lower() == "local":
            filename = sys.argv[2]
        elif str(sys.argv[1]).lower() == "youtube":
            downloadYoutubeVideo(sys.argv[2])
            filename = "youtube_video.mp4"
        else:
            print("The first argument is wrong")
            sys.exit()
    
    cap = cv2.VideoCapture(filename)
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
    