import pyttsx3
import speech_recognition as sr
import os
from datetime import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = False


def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_after_run():
    speak("Google assistant is ready!")
speak_after_run()



#check for the time
def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M") #make the date time in digital format
    return current_time



while True:  #this is to loop the commands
    try:  #This is to catch error
        with sr.Microphone() as mic:
            print("Listening...")
            speak("Listening for a command")
            recognizer.adjust_for_ambient_noise(mic, duration=1.5) #this makes the command heard properly.
            audio = recognizer.listen(mic)  #listens for the audio 
            commands = recognizer.recognize_google(audio).lower().strip()
            print(f"You said: {commands}")

            if "open chrome" in commands:
                print("opening Chrome")
                speak("Opening Chrome")
                os.system("start chrome")

            elif "Open edge" in commands:
                bot_response = "Opening Microsoft Edge" #the bot response
                print(bot_response)
                speak(bot_response)
                os.system("start edge")
        
            elif "Open microsoft edge" in commands:
                bot_response = "Opening Microsoft Edge"
                print(bot_response)
                speak(bot_response)
                os.system("start edge")



            elif "what is the time" in commands:
               current_time = tell_time()
               print(f"The time is {current_time}") #prints the current time.
               speak(f"The time is {current_time}") #speak the current time.

            elif "shut down" in commands:
                print("Shutting down your computer")
                speak("shutting down your computer!")
                os.system("shutdown /s /f /t 0")
            
            elif "turn off computer" in commands:
                print("Shutting down your computer")
                speak("shutting down your computer!")
                os.system("shutdown /s /f /t 0")
            
            elif "open youtube" in commands:
                print("Opening Youtube")
                speak("Opening YouTube!")
                os.system("start chrome https://www.youtube.com")

            elif "lock computer" in commands:
                print("Locking computer")
                speak("Locking computer")
                os.system("shutdown /s /f /t 0")

            elif "stop" in commands:
                bot_response = "bye, and have a great day "
                print(bot_response)
                speak(bot_response)
                break

            elif "bye" in commands:
                print("bye")
                speak("bye")
                break


               #if command isnt said print it doesnt understand!
            else:
                print("I don't understand that!")
                speak("I don't understand that!")
    except sr.UnknownValueError:
        print("I didnt hear that")
        speak("I did not hear that!")
    except sr.RequestError:
        print("There was an error...Try again.")
        speak("There was an error...Try again.")
