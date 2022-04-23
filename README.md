# raspberry-pi-pico-codes

## Regulating AC Current
Regulating AC current using TRIAC and optocouplers; and sending command using a remote control.

Range hints for output signal to optocoupler (from microcontroller to AC load), with respect to 220V:
- for 65w stand fan (GFC brand), range is: 101 - 140
- for 100w bulb, range is: 70 - 160
- for 0.5w dim led, range is: 86 - 180

### Code
ac_current_regulator_with_remote.py
### Demos:
<img width="200" src="https://lh3.googleusercontent.com/pw/AM-JKLUUTcbrkwN0k4GdYYPLzYfm2h_Gtfh3CcplOAoeuN--eVhhz1spzuz4gzJSnulnbgmCVrdLSqaIklSBfi5040YH_uq6OawRwKKizfJiW0rXISrLq6fbHqKEua75bRL2WJePeRa4QsSyLUSGPR8SSPAO=w1191-h893-no" alt="raspberry pi pico with circuitry to make a ac current regulator using remote control and infrared receiver">

<a href="https://photos.google.com/share/AF1QipMxJeXe8Dkfav_fJePZEocG_cxru361X8TlcnVONiT_fjRgSJim8aCU-Fa11UC1pA/photo/AF1QipOptelYxb8-xW6-5J3ekF9xvNZq1vNsd7QG7PdN?key=WU9GYXdtT3dUOHdkZVVSRlJKeWJBaVRmdDNXQjNB">Regulating a fan with remote control (video; bonus- background scream of my kid)</a>

<a href="https://photos.google.com/share/AF1QipMxJeXe8Dkfav_fJePZEocG_cxru361X8TlcnVONiT_fjRgSJim8aCU-Fa11UC1pA/photo/AF1QipMz-pJeHNw6iP89N1ydZmmvExvDDAOiCz8xLoHA?key=WU9GYXdtT3dUOHdkZVVSRlJKeWJBaVRmdDNXQjNB">Regulating a bulb with remote control (video)</a>

<a href="https://photos.google.com/share/AF1QipMxJeXe8Dkfav_fJePZEocG_cxru361X8TlcnVONiT_fjRgSJim8aCU-Fa11UC1pA/photo/AF1QipPbjrCDit_wPDPTwOCN23eMKoTIX3RGfSgwVuLn?key=WU9GYXdtT3dUOHdkZVVSRlJKeWJBaVRmdDNXQjNB">Regulating a bulb with potentiometer (video)</a>


## Gsa Sensor (MQ2)
Gas sensors (the cheap one that we purchase for experiment)
needed to be calibrated after purchasing.
I.e, after running the sensor, voltage output in clean air should be used to calibrate the sensor reading.
Those sensors are not that accurate and should not be used
for professional purpose.

For Gas (MQ2) sensor, use that code, written for Raspberry PI; so remove ADC (MCP3008) chip related code:
https://github.com/tutRPi/Raspberry-Pi-Gas-Sensor-MQ/blob/master/mq.py

Also have a look, written for raspberry pi:
https://github.com/filips123/GasDetection


## Water (or rain) Drop Sensor
Initial (not raining) ADC value is the max int - 65535. The more the rain or water drops falls on the detector sheet, the lower the value becomes.
For binary Pin input, neutral value is 1, if heavy drops are detected, value will be 0; so for light drops value will remain 0.

N.B.:
1. There's a nob in the sensor, probably to adjust the sensitivity.
2. The sheet needs to be connected with the sensor.

## Line Tracking Sensor
This sensor can differentiate between while and
black in front of it which is helpful to track
a black line on white background or a white line
on a black background.
Digital (binary) values will be enough for detection.
There's a potentiometer onb on the sensor to incread or decrease hte sensitivity fo the sendor.
This sensor has IR sender and receiver which works as detector of white and black.
A 1inch straigh and unambiguous line should be drawn to work with.

## Sound Sensor
Probably too much analog (voltage) noise in my sensor (from HiPi). Value is always high.

## Joystick
HiPi Joystick has 3 pins besides VCC and GND. X, Y pins will be in ADC;
Bt (middle button) will be a binary pin.
Neutral value for button is 1, 0 - when pressed. Neutral value for 
X or Y is around 65535/2. Value will increase or decrease according 
to the inclination towards a direction of the stick.  
For Example, moving the stick UP will slowly decrease X value (this 
is odd, up/down should be connected to Y ware of the module).


## All Demo Pictures and Videos
https://photos.app.goo.gl/YCahwJrahAJGaoKj6
