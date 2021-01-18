# A demo of reading temperature sensors DS18x20 on a 1-Wire bus.
# Since the internal pull up is activated on the pin used for the
# 1-Wire bus, no external pull up resistor is needed.

from machine import Pin
import time, ds18x20, onewire

# The pin to
OW_PIN = 12

# Set up a 1-Wire bus on pin (with internal pull up resistor activated)
one_wire_bus = onewire.OneWire(Pin(OW_PIN))

# An object representing all sensors on the bus
sensors = ds18x20.DS18X20(one_wire_bus)

# A list of unique 64 bit serial codes for the connectede sensors
sensor_ids = sensors.scan()

# Print status
print("Found {} devices on 1-Wire bus on pin {}.".format(len(sensor_ids), OW_PIN))

# Tell sensors to measure temperature
sensors.convert_temp()

# Wait while sensors measure temperature. Takes 750ms (At 12bit resolution) according to datasheet.
time.sleep_ms(750)

# Read the stored temperature off of the sensors
for id in range(len(sensor_ids)):
    print("Sensor {}: {} C".format(id, sensors.read_temp(sensor_ids[id])))
