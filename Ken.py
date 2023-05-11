import pyttsx3
import openai
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Yo():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Evening...")
    speak("I'm Ken... how you doin'!? Want help with something...!?")


openai.api_key = "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"
content = input("Ask your quesitons: ")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])


def takeCommmand():
    # takes microphone input from the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again...")
        return "None"
    return query


# def sendemail(to, content):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()
#     server.login("buriburi@gmail.com", "your-password")
#     server.sendmail('buriburi@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":
    Yo()
    # speak("It's more fun to chase than be chased.. that's why young girls grow up to be adults falling in love with love")
    print(completion.choices[0].message.content)
    speak(completion.choices[0].message.content)
    
    while True:
        query = takeCommmand().lower()
    
        # logic for xecuting tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open one piece" in query:
            webbrowser.open("https://zoro.to/one-piece-100")

        # elif "play music" in query:
        #     music_dir = "D:\bleh.."
        # songs = os.listdir(music_dir)
        # os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\Buri Buri\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        # elif "email to buri" in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommmand()
        #         to = "buriburi@gmail.com"
        #         speak("Email has been sent")
        #         sendemail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         # print(e)
        #         speak("Sorry my friend.. couldn't send the email right away")

