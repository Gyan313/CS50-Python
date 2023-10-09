import pyttsx3
import cowsay

engine = pyttsx3.init()
# --> library pyttsx3 has a class named init contains function named init() that
#     returns obj for this class

this = input("What to say: ")

cowsay.cow(this)
engine.say(this)
engine.runAndWait()
