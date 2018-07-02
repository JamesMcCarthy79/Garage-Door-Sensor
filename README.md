<p align="center">
  <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Garage%20Door%20Sensor.jpg" width="250"/>
</p>
<h1 align="center">Garage-Door-Sensor</h1>
<p align="center">Build Description for my Garage Door Sensor and Integration into Home Assistant</p>
<p align="center">Be sure to :star: my repo!</p>
<p align="center">
  <href="https://pycom.io/downloads/"><img src="https://img.shields.io/badge/WiPy-v1.18.0-5294E2.svg"/>
  <href="https://pycom.io/downloads/"><img src="https://img.shields.io/badge/Sensor%20Code-v1.0-5294E2.svg"/>
<hr --- </hr> 
<p align="center">
  This repo is help anyone that wishes to build a cheap distance sensor to determine if your garage door is open/closed and if your car is parked inside or not.</p>
<hr --- </hr>
<p align="left">The scope of this project was to create a sensor that could tell me if I have left my door open or not from within my home automation software "Home Assistant". Once intergrated into home assistant I could then set automations to close the door during my goodnight script if it was still open or close it if we are not home for more then 10mins.</p> 
<h4>Garage Sensor Topology</h4>
<p align="center">
  <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Garage%20Sensor%20Topo.png"/>
</p>

<h3 align="left">Garage Door Sensor Hardware</h3> 
<img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Pycom.png" width="200"/> 
<p align="left">I used the Pycom WiPy as my micro controller and the Pycom expansion board for my pin breakouts.
<hr --- </hr>

| [Pycom WiPy 3.0](https://core-electronics.com.au/pycom-wipy-3-0.html) | [Pycom Expansion Board 3.0](https://core-electronics.com.au/pycom-expansion-board-3-0-42869.html) | [HC-SR04](https://core-electronics.com.au/hc-sr04-ultrasonic-module-distance-measuring-sensor.html) | [ABS Enclosure](https://www.jaycar.com.au/snap-fit-abs-enclosure-50-4-x-50-x-27mm/p/HB6006) |
| --- | --- | --- | --- |
| <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/WiPy.jpg" width="250"/> | <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Expansion%20Board.jpg" width="250"/> | <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Ultrasonic.jpg" width="250"/> | <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Enclosure.jpg" width="250"/> |

<h3 align="left">Setup Guide</h3> 
<h4 align="left">Step One - Update to Latest Firmware</h4>
You will firstly need to update your boards firmware to the latest version details of how to do this can be found here...(https://docs.pycom.io/chapter/gettingstarted/installation/firmwaretool.html)
<h4 align="left">Step Two - Upload Code to Board</h4>
<p>To access your board you will need to load up your favourite editor I use Atom it has a plugin called pymakr designed for programming your pycom boards. Copy all the contents from within the `Garage Sensor folder` and add them to the root of your module.</p>
<p align="center">
  <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Garage%20Sensor%20Screenshots/01.%20Upload%20Code.png" width="500"/>
<p>You will need to edit the `boot.py` file on line 19 with your preferred username/password this will set the access to the sensor once you connect to it from its IP Address.</p>
<p align="center">
  <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Garage%20Sensor%20Screenshots/02.%20Update%20Boot%20File.png" width="500"/> 
<p>Next you will need to go into the `Config` Folder and edit the `Wi-Fi_Details` file, in here you will set your wireless SSID and Password. You can also set a static IP details in here, the code uses dhcp by default if you wish to use staic IP Address please see section below.</p>
<p align="center">
  <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Garage%20Sensor%20Screenshots/03.%20Update%20Wi-Fi%20File.png" width="500"/> 
<hr --- </hr>
<h4>**If you would like to use a Static IP Address read below otherwise skip this step**</h4>
<p>To use a Static IP you will need to go to the `Wi-Fi` folder and edit the `Wi-Fi.py` file. Place a hashtag infront of line 33 and remove the hashtag from line 32, this will tell the code to take the details from the IP settings you set in the step above.</p>
<p align="center">
  <img src="https://github.com/JamesMcCarthy79/Garage-Door-Sensor/blob/master/Garage%20Door%20Sensor%20Pics/Garage%20Sensor%20Screenshots/04.%20Set%20Static%20IP.png" width="500"/> 
<p>Lastly it's time to adjust the distances to suit your purpose open the `main.py` and scroll down to line 57. This line will print on the screen the actual distance to an object in "cm" you can use this to adjust the lines below to your own use case.</br>
<p>Line 58 - Is your distance when the door is open I use the distance measured when the door is closed plus 1cm.</br>
<p>Line 59 - This is the payload that is will be sent to your broker if the door is "open"</br>
<p>Line 
