import time

from tc0309 import tc0309

t = tc0309('/dev/ttyUSB0')
while True:
    record = t.get_record()
    print(f"{record}")
    time.sleep(1)

