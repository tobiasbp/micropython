# A simple LED chaser using adressable LEDs of type WS2812/NeoPixel
# https://docs.micropython.org/en/latest/esp8266/quickref.html#neopixel-driver
# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine, neopixel, time


# LED strip configuration
LED_STRIP_PIN = 14
LED_STRIP_LENGTH = 42
LED_FADE_SPEED = 4
LED_COLOR = (40, 0, 0)

# Create a neopixels object representing a strip of LEDS
np = neopixel.NeoPixel(machine.Pin(LED_STRIP_PIN), LED_STRIP_LENGTH)

while True:
    # Run through LEDs in the strip
    for i in range(np.n):
        # Light current LED
        np[i] = LED_COLOR

        # Lower intensity of all leds
        for x in range(np.n):
            np[x] = [v - int(LED_FADE_SPEED) if v > int(LED_FADE_SPEED) else 0 for v in np[x]]

        # Refresh LED strip
        np.write()
