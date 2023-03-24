import speech_recognition as sr
b=sr.Recognizer()
def recognize():
    with sr.Microphone() as mp:
        print("listening...")
        aa=b.listen(mp)
        bb=b.recognize_google(aa)
        #you can use anything for recognizing the voice like recognize_amazon or recognize_azure
        print(bb)
    return bb


ab=recognize()

print(ab)
