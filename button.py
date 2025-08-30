import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

red, green, blue = 17, 27, 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def all_off():
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)

def led_control(color):
    all_off()
    if color == "red":
        GPIO.output(red, GPIO.HIGH)
    elif color == "green":
        GPIO.output(green, GPIO.HIGH)
    elif color == "blue":
        GPIO.output(blue, GPIO.HIGH)

def exit_program():
    all_off()
    GPIO.cleanup()
    window.quit()
    window.destroy()

window = tk.Tk()
window.title("LED Control GUI")

selected_led = tk.StringVar()

tk.Radiobutton(window, text="Red LED", variable=selected_led, value="red",
               command=lambda: led_control("red")).pack(anchor="w")

tk.Radiobutton(window, text="Green LED", variable=selected_led, value="green",
               command=lambda: led_control("green")).pack(anchor="w")

tk.Radiobutton(window, text="Blue LED", variable=selected_led, value="blue",
               command=lambda: led_control("blue")).pack(anchor="w")

tk.Button(window, text="Exit", command=exit_program, bg="black", fg="white").pack(pady=10)

window.mainloop()
