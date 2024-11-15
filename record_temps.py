#! /usr/bin/env python3

import time

from tc0309 import tc0309

thermometer0 = tc0309('/dev/ttyUSB0')

thermometer1 = tc0309('/dev/ttyUSB1')

while True:
    now = time.time()
    record0 = thermometer0.get_record()
    record1 = thermometer1.get_record()
    print(f"{now},{record0['T1']},{record0['T2']},{record0['T3']},{record0['T4']},{record1['T1']},{record1['T2']},{record1['T3']},{record1['T4']}")
    time.sleep(1)

