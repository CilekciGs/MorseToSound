import sys
import time
from playsound import playsound


morse = {'A': '.-', 'B': '-...',
         'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-',
         'L': '.-..', 'M': '--', 'N': '-.',
         'O': '---', 'P': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--',
         'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.',
         '0': '-----', ', ': '--..--', '.': '.-.-.-',
         '?': '..--..', '/': '-..-.', '-': '-....-',
         '(': '-.--.', ')': '-.--.-'}


def eng2morse(text):
    return "".join([morse[char] if char != " " else " " for char in text])


def main(args):
    # TODO check the input text consistency
    print(args[-1])
    out = eng2morse(args[-1].upper())
    print(out)
    for idx in out:
        if idx == ".":
            playsound("sounds/dit.wav")
        elif idx == "-":
            playsound("sounds/dah.wav")
        elif idx == " ":
            time.sleep(0.25)
        else:
            continue



if __name__ == '__main__':
   main(sys.argv)

