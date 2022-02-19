import tkinter
from cgitb import text

from win32com.client import Dispatch
from tkinter import *

def clearTextInput():
    print("Clearing text...")
    inputentry.delete("1.0", "end")


def textospeech():
    print("Speaking with text...")
    speak = Dispatch("SAPI.SpVoice")
    voices = speak.GetVoices()
    print(voices)
    string = inputentry.get("1.0", tkinter.END)
    speak.Speak(string)


var_root = Tk()
canvas_height = 450
canvas_width = 800
var_root.title(f"Text To Speech App with Python")
label_title = Label(text= "Type To Listen", font="comicsansms 16 bold")
label_title.pack(padx=10, pady=10)
inputentry = Text(var_root, height=20, width=40)
inputentry.pack(padx=10, pady=10)
Button(var_root, text="Speak", command=textospeech).pack(padx=10, pady=10)
Button(var_root, text="Clear", command=clearTextInput).pack(padx=10, pady=10)
var_root.geometry(f"{canvas_width}x{canvas_height}")
var_root.mainloop()