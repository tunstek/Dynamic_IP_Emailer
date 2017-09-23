import time
from send_email import *

from json import load
from urllib2 import urlopen



# *********************************************************************
# Main Loop
# *********************************************************************


while True:

    # Read in the previous IP
    f = open("ip.txt","r")
    oldIP = f.readline()
    f.close()

    newIP = load(urlopen('http://jsonip.com'))['ip']

    if oldIP != newIP:
        print "IP changed to: " + newIP
        print "Sending alert email.."
        subject = "CCC IP CHANGE"
        body = "The CCC dynamic IP has changed to: " + newIP
        send_alert(subject, body)

        file = open("ip.txt" ,'w')
        file.write(newIP)
        file.close()

    # repeat every 12 hours
    time.sleep(43200)
