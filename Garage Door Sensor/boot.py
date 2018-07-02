from machine import UART
import machine
import os

import pycom
import network
import time

pycom.heartbeat(False)

uart = UART(0, baudrate=115200)
os.dupterm(uart)

machine.main('main.py')

server = network.Server()
server.deinit() # disable the server
# enable the server again with new settings
server.init(login=('your username here', 'your password here'), timeout=600)

pycom.rgbled(0x800080)		# purple
