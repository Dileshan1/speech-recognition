import speech_recognition as sr

recg = sr.Recognizer()

with sr.Microphone() as scorue:
    print("Tell some thing")

    audio = recg.listen(scorue)

    try:
        text = recg.recognize_google(audio,)       # (language="si-LK") for sinhala
        print(text)
    except:
        print("Not recognized")