import machine
import pycom
import time
import binascii
import network
from network import WLAN
from machine import RTC


pycom.heartbeat(False)      # turn off the heartbeat LED so that it can be reused

deviceID=binascii.hexlify(machine.unique_id())   # get device unique id and save to file on device
print (deviceID[8:12])

f_wifi = open('/flash/Config/Wi-Fi_Details.txt', 'r')     # read wifi SSID and password from file
                                                                        # file format is:  SSID, WLAN.WPA2, password
wifi_setting = f_wifi.readline()
wifi_strings = [i.strip() for i in wifi_setting.split(',')]
f_wifi.close()

#print(wifi_strings[0],  wifi_strings[1],  wifi_strings[2])

f=open('/flash/device_name', 'w''')
f.write(deviceID[8:12])
f.close()

print('LED on')
pycom.rgbled(0x7f0000)		# red
time.sleep(2)

wlan = WLAN(mode=WLAN.STA)
#wlan.ifconfig(config=(wifi_strings[3], wifi_strings[4], wifi_strings[5], wifi_strings[6]))  #Enable for static IP use
wlan.connect(wifi_strings[0],  auth=(WLAN.WPA2, wifi_strings[2]), timeout = 5000)
print('Wi-Fi Connecting To :', wifi_strings[0],)
while not wlan.isconnected():
	machine.idle()  #loop until connected

print('Connected')
pycom.rgbled(0x00007f)		# blue
time.sleep(2)

print('Requesting Time Sync')
rtc = RTC()
rtc.ntp_sync('129.250.35.251', 3600)
pycom.rgbled(0xffff00)		# yellow
time.sleep(2)
print("Current Time - " + str(rtc.now()))
print("IP Details - " + str(wlan.ifconfig()))


pycom.rgbled(0x007f00)		# green
time.sleep(2)
