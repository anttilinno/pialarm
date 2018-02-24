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
