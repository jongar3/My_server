import os
import time
from gpiozero import PWMOutputDevice

# CONFIGURATION
GPIO_PIN = 14          
TEMP_MIN = 45          
TEMP_MAX = 70         
PWM_FREQ = 25000        
CHECK_WAIT = 5         


DUTY_MIN = 0.66      # 0.66 = 3.3V  
DUTY_MAX = 1.0

fan = PWMOutputDevice(GPIO_PIN, frequency=PWM_FREQ)

def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    temp_str = res.replace("temp=","").replace("'C\n","")
    return float(temp_str)

def calculate_speed(temp):
    if temp < TEMP_MIN:
        return 0.0
    if temp >= TEMP_MAX:
        return DUTY_MAX
    else:
        speed = DUTY_MIN + (DUTY_MAX - DUTY_MIN) * ((temp - TEMP_MIN) / (TEMP_MAX - TEMP_MIN))
        return speed

print(f"Control de ventilador activo en GPIO {GPIO_PIN}...")

try:
    while True:
        current_temp = get_cpu_temp()
        new_speed = calculate_speed(current_temp)
        
        fan.value = new_speed
        
        print(f"Temp: {current_temp}°C -> Speed (PWM): {new_speed:.2f}")
        time.sleep(CHECK_WAIT)

except KeyboardInterrupt:
    fan.off()
    print("\nPrograma detenido.")