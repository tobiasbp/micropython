# Import ESP32 specific library
# http://docs.micropython.org/en/v1.13/library/esp32.html
import esp32

# Read temperature in fahrenheit from internal sensor
t_f = esp32.raw_temperature()

# Convert temperature in fahrenheit to celcius
t_c = (t_f -32) * 5/9

# Print temperature
print("Internal temperature (c):", t_c)
print("Internal temperature (f):", t_f)

