import speech_recognition as sr # google speech-to-text(Sesi yazıya dönüştürme) modülü

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source) # Dinlenilenleri tutmak için bir değişken
        said = "" # Söyleneni tutmak için bir değişken

        try:
            said = r.recognize_google(audio, language = 'tr') # recognize_google, google'ın söylenenleri anlama hizmetini kullanır. language = dil (örn: eng, tr, fr)
            print("Söylenilen: " + said)
        except Exception as e: # Mikrofonun algılanmaması, google'a bağlanamama gibi durumlarda
            print("Beklenmedik bir hata meydana geldi." + str(e))

get_audio()
