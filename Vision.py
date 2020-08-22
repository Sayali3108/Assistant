import os
import pyttsx3
import webbrowser
import random
pyttsx3.speak("Hello")
pyttsx3.speak("I'm your assistant VISION, How can I help you?")
while True:
	print("How can I help you: ")
	p=input()

	if(("chrome" in p) or ("browser" in p)):
    		pyttsx3.speak("Launching Chrome")
    		os.system("start chrome")

	elif(("music" in p) or ("media player" in p)):
    		pyttsx3.speak("Launching Windows Media Player")
    		os.system("start wmplayer")

	elif(("presentation" in p) or ("ppt" in p)):
    		pyttsx3.speak("Launching Power Point")
    		os.system("start POWERPNT")

	elif(("editor" in p) or ("notepad" in p)):
    		pyttsx3.speak("Launching notepad")
    		os.system("start notepad")

	elif(("firefox" in p) or ("mozilla" in p)):
    		pyttsx3.speak("Launching Mozilla Firefox")
    		os.system("start firefox")

	elif(("vlc" in p) or ("videoplayer" in p)):
    		pyttsx3.speak("Launching VLC ")
    		os.system("start vlc")

	elif(("word" in p) or ("microsoft word" in p)):
    		pyttsx3.speak("Launching Word")
    		os.system("start WINWORD")

	elif(("setting" in p) or ("control panel" in p)):
    		pyttsx3.speak("Launching Settings")
    		os.system("start Control")
	
	elif(("reader" in p) or ("pdf reader" in p)):
    		pyttsx3.speak("Launching Adobe PDF Reader ")
    		os.system("start AcroRd32")

	elif(("youtube" in p) or ("tube" in p)):
    		pyttsx3.speak("Launching Youtube ")
    		webbrowser.open("www.youtube.com")
	
	elif(("whatsapp" in p) or ("whatsapp web" in p)):
    		pyttsx3.speak("Launching Whatsapp. Scan the code")
    		webbrowser.open("https://web.whatsapp.com")
	
	elif(("gmail" in p) or ("mail box" in p)):
    		pyttsx3.speak("Launching Gmail")
    		webbrowser.open("www.gmail.com")

	elif(("what's up" in p) or ("how are you" in p)):
        	setReplies = ['Just doing some stuff!', 'I am good!',                                     
                      'Nice!','I am fine', 'I am amazing and full of power']
        	pyttsx3.speak(random.choice(setReplies))
	
	elif(("exit" in p)  or ("quit" in p)):
		pyttsx3.speak("Thank you. Have a good day!")
		break

	else:
		print("Sorry, I'm unable to perform")
		pyttsx3.speak("Sorry, I'm unable to perform")


