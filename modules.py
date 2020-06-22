#-*-coding:utf-8-*-
from utils import *

class ClassV():
    def __init__(self):
        #frames
        self.frames = []
        self.cur_pos = None
        #V's
        self.Vs = []



    def init_add(self,frames):
        self.frames = frames

        #calc difference
        for i in range(len(frames)):
            if i == 0:
                _,delta = IDsum(frames[0],frames[0])
            else:
                _,delta = IDsum(frames[i-1],frames[i])

            delta = IDarea(delta)
            self.Vs.append(delta)

        self.cur_pos = len(frames)//2

    def add(self, frame):
        _, delta = IDsum(self.frames[-1],frame) #get difference
        delta = IDarea(delta)

        self.frames.append(frame)
        self.Vs.append(delta)

        #filter
        self.frames.pop(0)
        self.Vs.pop(0)

    def get_Vmax(self,T,pos):
        if T % 2 == 0:
            r = int(T/2)
            return max(self.Vs[pos-r:pos+r])
        else:
            r = int((T-1)/2)
            return max(self.Vs[pos-r:pos+r+1])

    def get_Vmin(self,T,pos):
        if T % 2 == 0:
            r = int(T/2)
            return min(self.Vs[pos-r+1:pos+r+1])
        else:
            r = int((T-1)/2)
            return min(self.Vs[pos-r:pos+r+1])

    def get_cur_frame(self):
        return self.frames[self.cur_pos].copy()

    def get_prev_frame(self):
        return self.frames[self.cur_pos-1].copy()
