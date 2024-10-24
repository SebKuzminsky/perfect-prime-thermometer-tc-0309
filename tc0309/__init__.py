import serial
import time

class tc0309:
    def __init__(self, port):
        self.serial = serial.Serial(
            port=port,
            baudrate=9600,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1.0
        )
        self.model = self.get_model()

    def get_model(self) -> str:
        self.serial.write(b'K')
        line = ''
        now = time.time()
        while time.time() - now < 1.0:
            char = self.serial.read()
            if char == b'\r': break
            line += char.decode()
        if len(line) > 0:
            return line.encode()
        else:
            raise ValueError("no response to 'K' command")

    def _decode(self, raw: bytes):
        # Validate the raw buffer.
        if len(raw) != 45: raise ValueError
        if raw[0] != 0x02: raise ValueError
        if raw[44] != 0x03: raise ValueError

        result = { }

        result['low battery'] = bool(raw[1] & 0x40)
        result['units'] = 'C' if raw[1] & 0x80 else 'F'

        t1 = (raw[7] << 8) + raw[8]
        if t1 != 0x7fff:
            result['T1'] = t1/10

        t2 = (raw[9] << 8) + raw[10]
        if t2 != 0x7fff:
            result['T2'] = t2/10

        t3 = (raw[11] << 8) + raw[12]
        if t3 != 0x7fff:
            result['T3'] = t3/10

        t4 = (raw[13] << 8) + raw[14]
        if t4 != 0x7fff:
            result['T4'] = t4/10

        return result

    def get_record(self):
        self.serial.write(b'A')
        buffer = self.serial.read(size=45)
        return self._decode(buffer)
