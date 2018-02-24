# pialarm

## Use case

Attach rpi to a access controlled door. Every time door is used, increase counter, until event counter is big enought to trigger event. When event is triggered, light a lamp to notify security worker to perform an action.

- Hardware: RaspberryPi Rev. 2, model B
- Software: Raspbian Stretch Lite
- Packages
  - supervisorctl
  - python-pigpio
  
Make sure supervisord and pigpiod are enabled during boot (via systemctl enable).

The code uses Broadcom PIN numbering scheme!

[pigpio](http://abyz.me.uk/rpi/pigpio/python.html)

[supervisor](http://supervisord.org/)

## Important PINs

|PIN|IN/OUT|Purpose|
|---|------|-------|
|4  |OUT   |Alarm light|
|13 |IN    |Door's 3.3V event|
|26 |OUT   |Status LED(When program is running, show green light)|


```
Type 3 - Model A+, B+, Pi Zero, Pi2B, Pi3B

    40 pin expansion header (J8).

    Hardware revision numbers of 16 or greater.

    User GPIO 2-27 (0 and 1 are reserved).


	GPIO 	pin 	pin 	GPIO 	
3V3 	- 	1 	2 	- 	5V
SDA 	2 	3 	4 	- 	5V
SCL 	3 	5 	6 	- 	Ground

	4 	7 	8 	14 	TXD
Ground 	- 	9 	10 	15 	RXD
ce1 	17 	11 	12 	18 	ce0

	27 	13 	14 	- 	Ground

	22 	15 	16 	23 	
3V3 	-
	17 	18 	24 	
MOSI 	10 	19 	20 	- 	Ground
MISO 	9 	21 	22 	25 	
SCLK 	11 	23 	24 	8 	CE0
Ground 	- 	25 	26 	7 	CE1
ID_SD 	0 	27 	28 	1 	ID_SC

	5 	29 	30 	- 	Ground

	6 	31 	32 	12 	

	13 	33 	34 	- 	Ground
miso 	19 	35 	36 	16 	ce2

	26 	37 	38 	20 	mosi
Ground 	- 	39 	40 	21 	sclk
```
