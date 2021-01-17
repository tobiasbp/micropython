# Blinking the built in LED using PWM
from machine import PWM, Pin

# The pin to use with PWM
PWM_PIN = 22
PWM_FREQ = 1
PWM_DUTY = 512

# Set up the PWM pin
pwm_01 = PWM(Pin(22), freq=PWM_FREQ, duty=PWM_DUTY)

print("PMW running on pin", PWM_PIN) 
