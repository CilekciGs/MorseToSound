#!/usr/bin/env python

# import required libraries
import os
import sys

# running os
ros = os.uname().sysname

##could do a foreach loop

if len(sys.argv) >= 2:
	for i in range(1, len(sys.argv)):
		rawInput = sys.argv[i]
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


		print("\n\n\nYour message of:")
		print('"', rawInput, '"')
		print("\n\n\nis encrypted to:")
		print('"', encryptedMessage, '"')

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
else:
	print("usage: python morse2sound.py text1 text2 text3...")
	exit()
