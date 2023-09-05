"""Module Main used for logging notes with date and time """
import datetime

import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import pywhatkit
import bot

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

activationWord = 'farmbot'


# setting path for Chrome
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

appID = '2KE58X-ULEHAJ9LP8'
wolframClient = wolframalpha.Client(appID)


"""
This method allows the AI assistant to compute problems


:param query: text that is sent to the WolframAlpha API and describes what is to be computed 
"""
def searchWolframAlpha(query = ''):
    response = wolframClient.query(query)

    if response['@success'] == 'false':
        return 'Could not Compute'
    else:
        result = ''

        pod0 = response['pod'][0]

        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
            # Get the result
            result = listOrDict(pod1['subpod'])
            # Remove bracketed section
            return result.split('(')[0]
        else:
            # Get the interpretation from pod0
            question = listOrDict(pod0['subpod'])
            # Remove bracketed section
            question = question.split('(')[0]

            speak('Computation failed. Querying Universal Databank')
            return search_wikipedia(question)



def listOrDict(var):

    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']


"""

This method searches wikipedia with the given query.

:param query: text that will be searched through wikipedia

"""
def search_wikipedia(query = ''):
    
    searchResults = wikipedia.search(query)
    
    if not searchResults:
        print('No Wikipedia Results')
        return 'No Results received'
    
    try:
        wikipage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikipage = wikipedia.page(error.options[0])
    
    print(wikipage.title)
    wikiSummary = str(wikipage.summary)
    
    return wikiSummary

"""

This method sets the properties for the speech recognition library.

:param text: the words that will be said by the Assistant 
:param rate: how fast the text will be spoken

"""
def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

"""
This is method listens for a voice to be spoken into the microphone.

"""
def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize(input_speech)
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'

    return query

"""
Main method

"""
if __name__ == '__main__':
    speak('All systems nominal')

    while True:
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings all')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)

            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)

            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal databank.')
                speak(search_wikipedia(query))

            if query[0] == 'compute' or query[0] == 'computer':
                query = ' '.join(query[1:])
                speak('Computing')
                try:
                    result = searchWolframAlpha(query)
                    speak(result)
                except:
                    speak('Unable to Compute.')

            if query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                with open('note_%s.txt' % now) as newFile:
                    newFile.write(newNote)
                speak('Note Written')


            if query[0] == 'play':
                speak('Playing song...')
                query = ' '.join(query[1:])
                pywhatkit.playonyt(query)

            if query[0] == 'information':
                bot.chat()


            if query[0] == 'exit':
                speak('Bye')
                break

