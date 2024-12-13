import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipediaapi
import cv2

def convert_speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said - {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the request to Google Web Speech API; {e}")

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(query):
    headers = {'User-Agent': 'YourAppName/1.0 (your@email.com)'}
    wiki_wiki = wikipediaapi.Wikipedia('en', headers=headers)
    page = wiki_wiki.page(query)

    if page.exists():
        webbrowser.open(page.fullurl)
        return f"Opening Wikipedia page for {query} in your browser."
    else:
        return f"Sorry, I couldn't find information on '{query}' in Wikipedia."

while True:
    text = "how can I help you"
    text_to_speech(text)
    command = convert_speech_to_text()
    if command is not None:
        command = command.lower()

        if 'open instagram' in command:
            #for this command say open instagram
            text_to_speech("opening Instagram")
            webbrowser.open("https://www.instagram.com")
            break

        elif 'open control panel' in command:
            #for this command say open control panel
            text_to_speech("opening Control Panel")
            os.system("control panel")
            break

        elif 'open browser' in command:
            #for this command say open browser
            text_to_speech("opening Browser")
            webbrowser.open("https://www.chrome.com")
            break

        elif 'search on google about' in command:
            #for use this command say  search on google about(your search)
            search_query = command.replace('search on google', '').strip()
            text_to_speech(f"searching on Google for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            break

        elif 'open whatsapp' in command:
            #for this command say open whatsapp
            text_to_speech("opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com/")
            break

        elif 'facebook' in command:
            #for this command say open facebook
            text_to_speech("opening Facebook")
            webbrowser.open("https://www.facebook.com")
            break

        elif 'twitter' in command:
            #for this command say open twitter
            text_to_speech("opening Twitter")
            webbrowser.open("https://twitter.com")
            break
        elif 'wikipedia of' in command:
            #for use this command say wikipedia of(your search)
            query = command.replace('wikipedia', '').strip()
            print(f"Searching Wikipedia for: {query}")
            result = search_wikipedia(query)
            text_to_speech(result)

        elif 'open camera' in command:
            #for this command say open camera and to quit from camera use keyword 'q'
            try:
                text_to_speech("opening Camera")
                cap = cv2.VideoCapture(0)
                camera_open = True  # Set the flag to True
                while camera_open:
                    ret, frame = cap.read()
                    cv2.imshow('Camera', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        camera_open = False  # Set the flag to False
                        break  # Add this line to break out of the loop when 'q' is pressed

                cap.release()
                cv2.destroyAllWindows()
                text_to_speech("Closing the camera")
            except Exception as e:
                print(f"Error opening camera: {e}")
                text_to_speech("Sorry, I couldn't open the camera.")  
        elif 'exit' in command:
            #for exiting say exit
            text_to_speech("Goodbye, see you again")
            break
        else:
            # General Wikipedia query
            print(f"Searching Wikipedia for: {command}")
            result = search_wikipedia(command)
            text_to_speech(result)
    else:
        text_to_speech("Sorry, I couldn't understand. Please try again.")
