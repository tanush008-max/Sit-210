import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pins for LEDs
red, white, green = 17, 27, 22
GPIO.setup(red, GPIO.OUT)
GPIO.setup(white, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

pwm_red = GPIO.PWM(red, 1000)
pwm_white = GPIO.PWM(white, 1000)
pwm_green = GPIO.PWM(green, 1000)

pwm_red.start(0)
pwm_white.start(0)
pwm_green.start(0)

def set_red(val): pwm_red.ChangeDutyCycle(int(val))
def set_white(val): pwm_white.ChangeDutyCycle(int(val))
def set_green(val): pwm_green.ChangeDutyCycle(int(val))

def exit_program():
    pwm_red.stop()
    pwm_white.stop()
    pwm_green.stop()
    GPIO.cleanup()
    window.quit()
    window.destroy()

window = tk.Tk()
window.title("LED Brightness Control")

tk.Label(window, text="Red LED").pack()
tk.Scale(window, from_=0, to=100, orient="horizontal", command=set_red, length=300).pack()

tk.Label(window, text="White LED").pack()
tk.Scale(window, from_=0, to=100, orient="horizontal", command=set_white, length=300).pack()

tk.Label(window, text="Green LED").pack()
tk.Scale(window, from_=0, to=100, orient="horizontal", command=set_green, length=300).pack()

tk.Button(window, text="Exit", command=exit_program, width=20, height=2, bg="black", fg="white").pack(pady=10)
window.protocol("WM_DELETE_WINDOW", exit_program)
window.mainloop()
