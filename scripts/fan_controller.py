import os
import time
import pigpio

# CONFIGURATION
PWM_PIN = 12         #Must be 12, 13, 18 o 19 for PWM hardware 
TEMP_MIN = 45          
TEMP_MAX = 70         
PWM_FREQ = 25000        
CHECK_WAIT = 5         


DUTY_MIN = 0.66      # 0.66 = 3.3V  
DUTY_MAX = 1.0

pi = pigpio.pi()

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

print(f"Control de ventilador activo en GPIO {PWM_PIN}...")

try:
    while True:
        current_temp = get_cpu_temp()
        new_speed = calculate_speed(current_temp)
        duty= int(new_speed * 1000000)
        pi.hardware_PWM(PWM_PIN, PWM_FREQ, duty)
        
        print(f"Temp: {current_temp}°C -> Speed (PWM): {new_speed:.2f}")
        time.sleep(CHECK_WAIT)

except KeyboardInterrupt:
    pi.hardware_PWM(PWM_PIN, PWM_FREQ, 0)
    pi.stop()