#!/usr/bin/python3
##### Import Libraries
import time
import os
import os.path
import syslogclient
import Integrity
import sys
swapfileport = "/var/run/file-integrity-checker.swap"
if(len(sys.argv) == 2):
    print("we check integrity of {}".format(sys.argv[1].strip()))
    argument=sys.argv[1].strip()
    monitor = Integrity.Integrity(swapfileport, directory=argument)
else:
    monitor = Integrity.Integrity(swapfileport)

while True:
    monitor.list_last()
    monitor.list_now()
    monitor.check_integrity()
    time.sleep(5)
    #print("Logging!!!")