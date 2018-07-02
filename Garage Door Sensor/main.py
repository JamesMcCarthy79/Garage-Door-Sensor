#Garage Door Sensor V1.0

from machine import RTC
from machine import ADC
from machine import Pin
from machine import Timer
import time
import pycom
import math
import gc

from network import WLAN
from mqtt import MQTTClient

execfile('/flash/Wi-Fi/Wi-Fi.py')

f_device = open('/flash/Config/Device_Details.txt', 'r')

device_setting = f_device.readline()
device_strings = [i.strip() for i in device_setting.split(',')]
f_device.close()

rtc = RTC()
adc = ADC()
echo = Pin(Pin.exp_board.G7, mode=Pin.IN)
trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT)
trigger(0)
chrono = Timer.Chrono()
pycom.heartbeat(False)

def settimeout(duration):
     pass

client = MQTTClient("garage", "your mqtt broker host", user="mqtt user here", password="mqtt password here", port=mqtt port here)
client.settimeout = settimeout
client.connect()
mqtt_topic = "garagedoor"

try:
    while True:
        if wlan.isconnected():

            pycom.rgbled(0x00007f)				# blue
            chrono.reset()
            trigger(1)
            time.sleep_us(10)
            trigger(0)
            while echo() == 0:
                pass
            chrono.start()
            while echo() == 1:
                pass
            chrono.stop()
            distance = chrono.read_us() / 58.0
            print(device_strings[0], "- Readings")
            print('--------------------------------')
            print("Distance : " + "{:.0f} cm".format(distance))
            if distance > 20:
                dist=("Open")
            else:
                if distance < 19:
                    dist=("Obstruction")
                else:
                    dist=("Closed")

            client.publish(mqtt_topic, dist)
            print(str(dist))
            print('--------------------------------')
            gc.enable()
            gc.collect()
            pycom.heartbeat(False)
            time.sleep(30)

except KeyboardInterrupt:
    pass
