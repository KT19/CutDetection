#-*-coding:utf-8-*-
import numpy as np
import cv2
from modules import ClassV
from utils import *

def main(path):
    #create class for cut detection
    object = ClassV()

    #read
    cap = cv2.VideoCapture(path)

    #set init reading
    init_T = 15
    frames = []
    for i in range(init_T):
        _,frame = cap.read()

        frames.append(frame)

    object.init_add(frames)
    values = []

    #text config
    font = cv2.FONT_HERSHEY_SIMPLEX
    WHITE = (255,255,255)

    #config for detection
    thres = 24

    #continue until the end
    num_cut = 0
    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret is False:
            break
        object.add(frame)


        prev_img = object.get_prev_frame() #h,w,c
        cv2.putText(prev_img,"frame:t-1",(10,380), font, 1, WHITE, 2, cv2.LINE_AA)
        img = object.get_cur_frame() #h,w,c
        cv2.putText(img,"frame:t",(10,380), font, 1, WHITE, 2, cv2.LINE_AA)


        value = Pfilter(object, T1=4, T2=2)*100

        if value > thres:
            color = (0,0,255)
            num_cut += 1
        else:
            color = (200, 0, 0)

        cv2.putText(img,"diff: "+str(value)[:5],(10,50), font, 1, color, 2, cv2.LINE_AA)
        img = cv2.hconcat([prev_img,img])
        cv2.imshow('CutDetection',img)

        if value > thres:
            cv2.waitKey()
        #wait
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break

        values.append(value)

    #release
    values.sort()
    print("total cut is {}".format(num_cut))
    cv2.waitKey()
    cap.release()
    cv2.destroyAllWindows()



if __name__ =="__main__":
    main(path="path_to_movies")
