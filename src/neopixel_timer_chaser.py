# A timer based LED chaser using adressable LEDs of type WS2812/NeoPixel
# Tested on a an ESP32 running MicroPython
import machine, neopixel
from machine import Timer

# Pin to use for controlling LEDs
LED_STRIP_PIN = 14
# Number of LEDs on LED strip
LED_STRIP_LENGTH = 42
# How many times a second (HZ) to advance the LED
LED_ADVANCE_RATE_HZ = 20
# The color of the lit LED
LED_COLOR = (100, 0, 0)
# How many times a second (HZ) to refresh LEDs
LED_REFRESH_RATE_HZ = 20
# The speed of fading. Higher values = faster fades with less granularity
LED_FADE_SPEED = 15
# Frequency of lowering the intensity of the LEDS
LED_FADE_RATE_HZ = LED_REFRESH_RATE_HZ

# Create a neopixels object representing a strip of LEDS
np = neopixel.NeoPixel(machine.Pin(LED_STRIP_PIN), LED_STRIP_LENGTH)

# Index of the currently lit LED
led_index = 0


def advance(timer):
    """
    Advance lit LED
    """
    global np, led_index, LED_COLOR
    # Light LED
    np[led_index] = LED_COLOR
    # Set index of next LED
    if led_index == np.n - 1:
        led_index = 0
    else:
        led_index += 1


def fade(timer):
    """
    Lower intensity for all LEDs on strip
    """
    global np, LED_FADE_SPEED
    for i in range(np.n):
        np[i] = [
            v - int(LED_FADE_SPEED) if v > int(LED_FADE_SPEED) else 0 for v in np[i]
        ]


# Timer for advancing the lit LED
timer_advance = Timer(0)
timer_advance.init(
    period=int(1000 / LED_ADVANCE_RATE_HZ),
    mode=Timer.PERIODIC,
    callback=advance,
)

# Timer for fading out LEDs
timer_fade = Timer(1)
timer_fade.init(
    period=int(1000 / LED_FADE_RATE_HZ),
    mode=Timer.PERIODIC,
    callback=fade,
)

# Timer for updating the LED strip
timer_refresh = Timer(2)
timer_refresh.init(
    period=int(1000 / LED_REFRESH_RATE_HZ),
    mode=Timer.PERIODIC,
    callback=lambda t: np.write(),
)
