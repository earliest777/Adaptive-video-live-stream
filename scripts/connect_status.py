#!/usr/bin/python

import os
import subprocess
import re
import sys


def subprocessping(npings, url):
    proc = subprocess.Popen(["ping","-c", npings, url],stdout=subprocess.PIPE)
    proc.wait()
    return proc.communicate()


def check_connection(npings, url):
    (out,err) =subprocessping(npings,url)

    print out
##cannot ping phone so we need to check connetion with the cellphone ...
    if out.find("packet")==-1:
        print "Cannot reach  " +url
        return -1

##since there is a device connected to the raspberry
##we need to check if the rasp can  ping it
##and the quality of the connection

    strings=out.split(",")
    values=[]

    for i in range(0, 3):
        values.append(int(re.search(r'\d+', strings[i]).group()))

    #Percentage of lost packets
    if values[2]>50:
        return 1
    else :
        if values[2]!=0:
            return 0
        else:
            return 2

if __name__ == "__main__":

    #var=check_connection("10", "google.pt")
    #print var
    sys.exit()
