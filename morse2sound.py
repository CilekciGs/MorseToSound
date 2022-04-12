#!/usr/bin/env python

# import required libraries
import os
import sys
import tkinter as tk

# running os
ros = os.uname().sysname

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')

# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
	rawInput = inputtxt.get(1.0, "end-1c")
	message = rawInput.lower()

	# convert process with string replace method
	encoding = message.replace(" ", "/ ")
	encoding = encoding.replace("a", ".- ")
	encoding = encoding.replace("b", "-... ")
	encoding = encoding.replace("c", "-.-. ")
	encoding = encoding.replace("d", "-.. ")
	encoding = encoding.replace("e", ". ")
	encoding = encoding.replace("f", "..-. ")
	encoding = encoding.replace("g", "--. ")
	encoding = encoding.replace("h", ".... ")
	encrypting = encoding.replace("i", ".. ")
	encrypting = encrypting.replace("j", ".--- ")
	encrypting = encrypting.replace("k", "-.- ")
	encrypting = encrypting.replace("l", ".-.. ")
	encrypting = encrypting.replace("m", "-- ")
	encrypting = encrypting.replace("n", "-. ")
	encrypting = encrypting.replace("o", "--- ")
	encrypting = encrypting.replace("p", ".--. ")
	encrypting = encrypting.replace("q", "--.- ")
	encrypting = encrypting.replace("r", ".-. ")
	encrypting = encrypting.replace("s", "... ")
	encrypting = encrypting.replace("t", "- ")
	encrypting = encrypting.replace("u", ".-- ")
	encrypting = encrypting.replace("v", "...- ")
	encrypting = encrypting.replace("w", ".-- ")
	encrypting = encrypting.replace("x", "-..- ")
	encrypting = encrypting.replace("y", "-.-- ")
	encryptedMessage = encrypting.replace("z", "--.. ")
	encryptedMessage = encrypting.lower()

	lbl.config(text = (encryptedMessage))

	import subprocess
	import time

	sounds_folder = "sounds/"

	for char in encryptedMessage:
		if char == ".":
			if ros == 'Linux':
				subprocess.call(["aplay", sounds_folder+ "dit.wav"])
			else:
				subprocess.call(["afplay", sounds_folder+ "dit.wav"])
		elif char == "-":
			if ros == 'Linux':
				subprocess.call(["aplay", sounds_folder + "dah.wav"])
			else:
				subprocess.call(["afplay", sounds_folder + "dah.wav"])
		else:
			time.sleep(.1)

# TextBox Creation
inputtxt = tk.Text(frame, height = 5, width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame, text = "Translate", command = printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
