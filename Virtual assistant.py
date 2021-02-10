import pyttsx3
import wikipedia
import datetime
import webbrowser


engine = pyttsx3.init('sapi5')

def speak(text):
    print(f'[JARVIS]):{text}')
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    greeting = ''

    if hour >=0 and hour < 12:
        greeting = 'good morning'
    elif hour >=12 and hour < 18:
        greeting = 'good aternoon'
    else:
        greeting = 'good evening'
    speak(f'{greeting} i am jarvis. how may i help u today?')

def takeCommand():
    query = input()
    return query


wish_me()
while True:
    query = takeCommand().lower()

    query = query.replace('jarvis', '')

    if 'wikipedia' in query:
        speak('SEARCHING WIKIPEDIA....')
        query = query.replace('WIKIPEDIA', '')
        query = query.replace('search', '')
        query = query.replace('for', '')
        results = wikipedia.summary(query, sentences = 1)
        speak(f'Accordding to Wikipedia, {results}')
        
    elif 'open youtube' in query:
        speak('opening youtube')
        webbrowser.open("http://youtube.com")
    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("http://google.com")
    elif 'open stack overflow' in query:
        speak('opening Stackoverflow')
        webbrowseropen("http://stackoverflow.com")
    elif 'what' in query and 'time' in query:
        strtime = datetime.datetime.now().strtime("%H:%M%S")
    elif 'meaning of life' in query:
        speak('sir the meaning of life is 42.')
    elif 'how are u' in query :
        speak('i am doing well,sir.')
    else:
        speak('i didn\'t quiet catch u sir. can u please try again?')
        
        




