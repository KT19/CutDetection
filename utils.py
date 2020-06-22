#-*-coding:utf-8-*-
import numpy as np

def IDsum(prev, cur):
    cur = np.array(cur, dtype=np.float)/255
    prev = np.array(prev,dtype=np.float)/255
    delta = np.abs(cur-prev)
    S = np.mean(delta)

    return S,delta

def IDarea(delta,thres=1./16.):
    N = delta.size

    IDa = np.sum(delta[delta>thres])

    return IDa/N

def Dt(object,T,pos):
    return object.get_Vmax(T,pos)

def Et(object,T,pos):
    return object.get_Vmin(T,pos)

def St(object,T,pos):
    assert T > 0, "Time T shoule be T > 0"

    if T % 2 == 0:
        r = int(T/2)
        left = -r+1
        right = r
    else:
        r = int((T-1)/2)
        left = -r
        right = r

    temp = []
    while left <= right:
        temp.append(Dt(object,T,pos=pos+left))
        left += 1

    return min(temp)

def Pfilter(object, T1, T2):
    St1 = St(object,T1,object.cur_pos)

    """calculate Dt2"""
    if T2 % 2 == 0:
        r = int(T2/2)
        Dl = -r
        Dr = r
    else:
        r = int((T2-1)/2)
        Dl = -r
        Dr = r+1

    Dt2 = []
    while Dl < Dr:
        pos = object.cur_pos+Dl
        Dl += 1
        """calculate Et2"""
        if T2 % 2 == 0:
            r = int(T2/2)
            left = -r+1
            right = r
        else:
            r = int((T2-1)/2)
            left = -r
            right = r


        temp = []
        while left <= right:
            temp.append(St(object,T1,pos+left))
            left += 1

        Dt2.append(min(temp))

    return St1-max(Dt2)
