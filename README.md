Python interface to PerfectPrime Thermometer TC0309 over serial.

Use as a command-line utility:
```
$ python3 -u -m tc0309
{'low battery': False, 'units': 'C', 'T1': 21.3}
{'low battery': False, 'units': 'C', 'T1': 21.3}
{'low battery': False, 'units': 'C', 'T1': 21.3}
{'low battery': False, 'units': 'C', 'T1': 27.0}
{'low battery': False, 'units': 'C', 'T1': 27.0}
{'low battery': False, 'units': 'C', 'T1': 30.1}
{'low battery': False, 'units': 'C', 'T1': 30.1}
^C
```

Use as a python module:
```
$ python3
Python 3.11.6 (main, Apr 10 2024, 17:26:07) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from tc0309 import tc0309
>>> t = tc0309(port="/dev/ttyUSB0")
>>> t.get_record()
{'low battery': False, 'units': 'C', 'T1': 21.5}
>>>
```
