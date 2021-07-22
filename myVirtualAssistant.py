# install pyaudio --- using pip install pyaudio or pip install pipwin and then pipwin install pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
voiceDetector = pyttsx3.init()
voices = voiceDetector.getProperty('voices')
# Getting a female assistant
voiceDetector.setProperty('voice', voices[1].id)
voiceDetector.say("Hello !  My name is Virtual Assistant... I am your Assistant... How can I help you?")
voiceDetector.runAndWait()

# function to make the virtual assistant speak back
def speak(text):
    voiceDetector.say(text)
    voiceDetector.runAndWait()

print("How can I help you ?")

def detectingVoice():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audioVoice = listener.listen(source)
            command = listener.recognize_google(audioVoice)
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                # speak(command)

            # get the command time
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('The Time is...' + time)
                print('The Time is...' + time)

            # search in wikipedia
            elif 'what is' in command:
                searchInWikipedia = command.replace('what is', '')
                information = wikipedia.summary(searchInWikipedia, 1)
                print(information)
                speak(information)

            # search a person in wikipedia
            elif 'who is' in command:
                searchPersonWikipedia = command.replace('who is', '')
                personInfo = wikipedia.summary(searchPersonWikipedia, 1)
                print(personInfo)
                speak(personInfo)

            # Cracking a joke
            elif 'joke' in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            else:
                speak('Please say or ask something...')
                print('Please say or ask something...')
                detectingVoice()


    except:
        print("Error... Try Again")
        responseBack()
        pass
    return command


def responseBack():
    command = detectingVoice()
    print(command)

    if 'play' in command:
        music = command.replace('play', '')
        speak("Playing ")
        print('playing some song')
        pywhatkit.playonyt(music)

while True:
    responseBack()

