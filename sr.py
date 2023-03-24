import speech_recognition as sr
b=sr.Recognizer()
def recognize():
    with sr.Microphone() as mp:
        print("listening...")
        aa=b.listen(mp)
        bb=b.recognize_google(aa)
        print(bb)
    return bb


ab=recognize()

print(ab)
