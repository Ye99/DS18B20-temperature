from machine import Pin
import onewire
import time, ds18x20

ow = onewire.OneWire(Pin(12)) # create a OneWire bus on GPIO12, which is D6 on NodeMCU board.
ds_sensor = ds18x20.DS18X20(ow)
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print('sensor {sensor} reading {temperature}'.format(sensor=rom, temperature=ds_sensor.read_temp(rom)))
  time.sleep(5)

