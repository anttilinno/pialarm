import pigpio
import time
import sys
import time

pi = pigpio.pi()

# Main settings
ALARM_COUNT = 5 # light lamp after evennt no 50
GATE_INPUT_PIN = 13 # input current
ALARM_PIN = 4 # show light after ALARM_COUNT
STATUS_PIN = 26 # show green light, if program is running
CORRECT_EVENT_GAP = 1.5 # count only events, that are 1.5s apart

if not pi.connected:
   exit()

last_event = time.time()
counter = 0

pi.set_mode(GATE_INPUT_PIN, pigpio.INPUT)
pi.set_pull_up_down(GATE_INPUT_PIN, pigpio.PUD_UP)

pi.set_mode(ALARM_PIN, pigpio.OUTPUT)
pi.write(ALARM_PIN, 0)

pi.set_mode(STATUS_PIN, pigpio.OUTPUT)
pi.write(STATUS_PIN, 1)

def cbf(gpio, level, tick):
   this_event = time.time()
   global last_event
   global counter
   try:
       time_diff = this_event - last_event
       if time_diff > CORRECT_EVENT_GAP:
           counter += 1
           if counter > ALARM_COUNT:
               pi.write(ALARM_PIN, 1)
               time.sleep(5)
               pi.write(ALARM_PIN, 0)
               counter = 0
   except:
       pass
   last_event = this_event

cb1 = pi.callback(GATE_INPUT_PIN, pigpio.RISING_EDGE, cbf)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        pi.stop()
        sys.exit()

