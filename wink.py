#!/usr/bin/env python3

import os

dir = "/tmp"
sel = None
drv = None
junk = None

def cleanup():
    os.system("wget -O /tmp/wink.pl http://csc.gotdns.com/doc/wink.pl")
    os.system("chmod +x /tmp/wink.pl")
    #os.system("umount /dev/{}".format(drv))
    #os.system("rm -f /tmp/found_files.txt*")
    #os.system("rm -f ./wink.sh")

def menu_func():
    os.chdir(dir)
    cleanup()
    os.system("clear")
    print("***********************************************************************")
    print("**********           ~WINK~32 on KNOPPIX [v.1]~             ***********")
    print("***********************************************************************")
    print("*           *********************************************             *")
    print("*           ***      USE AT YOUR OWN RISK !!!         ***             *")
    print("*           ***        YOU MUST BE ROOT !!!           ***             *")
    print("*           *********************************************             *")
    print("***********************************************************************")
    print("*                                                                     *")
    print("*  Choices 1, 2, or 3 run scripts, 0 - exits.                         *") 
    print("*                                                                     *")
    print("*  1 - View IP & ARP info                                             *")
    print("*  2 - View h/d, memory & system stats                                *")
    print("*  3 - Find lost files -win32_util                                    *")
    print("*  4 - Copy found files to save folder.                               *")    
    print("*  0 - exit program                                                   *")
    print("*                                                                     *")
    print("*   Please select and press [ENTER] .. :                              *") 
    print("*                                                                     *")
    print("***********************************************************************")
    print(" ")
    sel = input("Please select and press [ENTER] .. :")
    if sel == '1':
        ip_arp()
    elif sel == '2':
        status()
    elif sel == '3':
        win_file_find()
    elif sel == '4':
        wink()
    elif sel == '0':
        exit()
    else:
        print("Please enter 1, 2, 3 or 0")
        menu_func()

def ip_arp():
    os.system("clear")
    print(" ")
    print(" Your IP address is ...")
    os.system("ifconfig | grep 'inet addr:' | fgrep -v '127.0.0.' | cut -d: -f2 | cut -d' ' -f1")
    print(" Your ARP gateway is ...")
    os.system("arp -a")
    print(" ")
    input("press [Enter] to continue...")
    menu_func()

def status():
    os.system("clear")
    print("Version 1.0 system stat monitor - c.sinclair 2005")
    print("System stats for {} ,
    os.system("System stats for $HOSTNAME , on `/bin/date`")
    print("")
    print("Current disk space stats: ")
    os.system("df")
    print("")
    print("Current memory stats: ")
    os.system("free")
    print("")
    print("Virtual memory stats: ")
    os.system("vmstat")
    print("")
    print("Who's on the system: ")
    os.system("who")
    print("")
    print("Your current IP address is ..")
    os.system("ifconfig | grep 'inetaddr:' | fgrep -v '127.0.0.' | cut -d: -f2 | cut -d' ' -f1")
    print(" ")
    print(" ")
    input("press [Enter] to continue...")
    menu_func()

def win_file_find():
    os.system("clear")
    # code for finding lost files goes here
    print("press [Enter] to continue...")
    input()
    menu_func()

def wink():
    os.system("clear")
    # code for copying found files goes here
    print("press [Enter] to continue...")
    input()
    menu_func()

menu_func()
# nevdullc :: 2023
