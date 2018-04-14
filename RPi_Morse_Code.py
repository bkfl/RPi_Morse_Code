from tkinter import *
from tkinter import messagebox
from gpiozero import LED
from time import sleep
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

# OUTPUTS
led = LED(21)

# GUI
root = Tk()
root.title("RPi: Morse Code")

# EVENT FUNCTIONS
def blink():
    input = eInput.get()
    # Check input is between 1 and 12 characters
    if (1 < len(input) < 13):
        # Check string contains letters only
        if (input.isalpha()):
            for c in input:
                morseBlink(c)
                morseCharRest()
        else:
            messagebox.showinfo("Error", "Input must contain only letters.")
    else:
        messagebox.showinfo("Error", "Input must be 1 to 12 characters.")

def close():
    RPi.GPIO.cleanup()
    root.destroy()

# FUNCTIONS
def morseDot():
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.3)

def morseDash():
    led.on()
    sleep(0.9)
    led.off()
    sleep(0.3)

def morseCharRest():
    sleep(0.6)

def morseBlink(char):
    if (char == 'a'):
        morseDot()
        morseDash()
    elif (char == 'b'):
        morseDash()
        morseDot()
        morseDot()
        morseDot()
    elif (char == 'c'):
        morseDash()
        morseDot()
        morseDash()
        morseDot()
    elif (char == 'd'):
        morseDash()
        morseDot()
        morseDot()
    elif (char == 'e'):
        morseDot()
    elif (char == 'f'):
        morseDot()
        morseDot()
        morseDash()
        morseDot()
    elif (char == 'g'):
        morseDash()
        morseDash()
        morseDot()
    elif (char == 'h'):
        morseDot()
        morseDot()
        morseDot()
        morseDot()
    elif (char == 'i'):
        morseDot()
        morseDot()
    elif (char == 'j'):
        morseDot()
        morseDash()
        morseDash()
        morseDash()
    elif (char == 'k'):
        morseDash()
        morseDot()
        morseDash()
    elif (char == 'l'):
        morseDot()
        morseDash()
        morseDot()
        morseDot()
    elif (char == 'm'):
        morseDash()
        morseDash()
    elif (char == 'n'):
        morseDash()
        morseDot()
    elif (char == 'o'):
        morseDash()
        morseDash()
        morseDash()
    elif (char == 'p'):
        morseDot()
        morseDash()
        morseDash()
        morseDot()
    elif (char == 'q'):
        morseDash()
        morseDash()
        morseDot()
        morseDash()
    elif (char == 'r'):
        morseDot()
        morseDash()
        morseDot()
    elif (char == 's'):
        morseDot()
        morseDot()
        morseDot()
    elif (char == 't'):
        morseDash()
    elif (char == 'u'):
        morseDot()
        morseDot()
        morseDash()
    elif (char == 'v'):
        morseDot()
        morseDot()
        morseDot()
        morseDash()
    elif (char == 'w'):
        morseDot()
        morseDash()
        morseDash()
    elif (char == 'x'):
        morseDash()
        morseDot()
        morseDot()
        morseDash()
    elif (char == 'y'):
        morseDash()
        morseDot()
        morseDash()
        morseDash()
    elif (char == 'z'):
        morseDash()
        morseDash()
        morseDot()
        morseDot()


# WIDGETS
lbl1 = Label(root, text="Enter a word (12 char max):")
lbl1.pack()
eInput = Entry(root)
eInput.pack()
btnBlink = Button(root, text="Blink It!", command=blink)
btnBlink.pack()
btnClose = Button(root, text="Close", command=close)
btnClose.pack()
