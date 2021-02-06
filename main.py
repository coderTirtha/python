import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
while True:
    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
        except:
            pass
        return command



    def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing...' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            talk('Current time is' + time)
        elif 'how are you' in command:
            talk("I'm fine. You?")
        elif 'fine' in command:
            talk('How can I help you?')
        elif 'not fine' in command:
            talk('What happened?')
        elif 'annoying' in command:
            talk('I did not catch that but it sounds like you are frustrated. To learn about my functions try asking "What can you do?"')
            print("I didn't catch that, but it sounds like you're frustrated. To learn about my functions, try asking, 'What can you do?'")
        elif 'what can you do' in command:
            print("I can tell you about your daily routine, next meeting, your dating time if you ask me.")
            talk('I can tell you about your daily routine, next meeting, your dating time if you ask me.')
        elif 'tumi ki amay' in command:
            talk('yes. ami toomake, khuub vaalo kore cini.')
            print('Yes. I know you.')
        elif 'do you know me' in command:
            talk('Yes. I know you very well. Do you know me?')
        elif 'listening' in command:
            talk("i'm listening you clearly. how can i help you?")
    run_alexa()