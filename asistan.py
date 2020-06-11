# Test
import speech_recognition as sr # google speech-to-text(Sesi yazıya dönüştürme) modülü
from gtts import  gTTS # google text-to-speech(Yazıyı sese dönüştürme) modülü
import playsound # Pythonda ses oynatma modülü
import time
import datetime
import os
import locale
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_VOLUME_MUTE, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK

# win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

# Burada yaptığım şey basitçe bir metini ses dosyasına çevirip aynı ses dosyasını çalmak.

def speak(text):
    tts = gTTS(text=text, lang="tr") # text = okunacak metin, lang = dil (örn: eng, tr, fr)
    file = "audio.mp3" # Metini sese çevirdikten sonra kaydetmesi için bir dosya adı seçiyorum.
    tts.save(file) # Yukarıda belirlediğim isimli bir dosya kaydeder
    playsound.playsound(file) # Programı kullanan kişinin bu sesi duyması için dosyayı oynatıyorum
    os.system("del audio.mp3")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source) # Dinlenilenleri tutmak için bir değişken
        said = "" # Söyleneni tutmak için bir değişken

        try:
            said = r.recognize_google(audio, language = 'tr') # recognize_google, google'ın söylenenleri anlama hizmetini kullanır. language = dil (örn: eng, tr, fr)
            print("Söylenilen: " + said)
            if said == "İleri" or said == "İlerle":
                said = "ileri"
        except Exception as e: # Mikrofonun algılanmaması, google'a bağlanamama gibi durumlarda
            return ""
    return said.lower()


def checkcommand(list, audio, event, speak1): # Bu fonksiyonu söylenilenler içinde belli bir liste kelime aratmak için kullandım
    for i in list:
        if audio.count(i) >= 1:
            speak(speak1)
            win32api.keybd_event(event, 0, KEYEVENTF_EXTENDEDKEY, 0)
            print("Şu işlemi yaptım: " + list)
            time.sleep(3)



def checksleep(list, audio, sleep1, speak1, speak2): # Yukarıdaki fonksiyonla aynı mantıkta fakat sleep işlevini gerçekleştiriyor
    for i in list:
        if audio.count(i) >= 1:
            print("Uyuyorum.")
            speak(speak1)
            time.sleep(sleep1)
            print("Uyandım.")
            speak(speak2)


locale.setlocale(locale.LC_ALL, 'turkish')
zaman = datetime.datetime.now()
tarih = datetime.datetime.strftime(zaman, '%c')




speak("Asistan Devrede")
print(tarih + " Çalıştırıldı...")


#kelime listeleri

KEYWORD = "asistan"
PLAYPAUSE = ["dur", "başlat", "devam", "durdur", "devam ettir"]
FORWARD = ["İleri", "ileri", "İlerle", "ileri", "illeri", "geç", "next", "skip", "sonraki", "değiş", "diğeri", "atla", "Müziği değiştir", "müziği değiştir"]
BACKWARD = ["Geri", "geri", "önceki", "az önce", "önceki müzik"]
MUTE = ["Sustur", "mute", "sesi kapat", "sesi indir", "sus", "müziği sustur", "sesleri kes", "sesleri aç", "unmute", "susturmayı aç", "konuş", "aç"]
SLEEP = ["dinlen", "mola", "kısa kes", "yeter"]
LONGSLEEP = ["kafana göre takıl", "takıl kafana göre", "teşekkür ederim", "sağol canım", "long sleep", "afk", "uyu"]
QUIT = ["Çık", "çık", "çıkış", "kapat", "programı sonlandır", "sonlandır", "quit", "exit", "kendine iyi bak"]

# main loop

while True:
    kwdedect = "\n"
    kwdedect = get_audio()

    try:
        if kwdedect.count(KEYWORD) >= 1:
            checkcommand(PLAYPAUSE, kwdedect, VK_MEDIA_PLAY_PAUSE, "Başlatıyorum ya da Durduruyorum")
            checkcommand(FORWARD, kwdedect, VK_MEDIA_NEXT_TRACK, "Bir sonraki şarkıya geçiyorum")
            checkcommand(BACKWARD, kwdedect, VK_MEDIA_PREV_TRACK, "Bir önceki şarkıya geçiyorum")
            checkcommand(MUTE, kwdedect, VK_VOLUME_MUTE, "Sistem seslerini susturuyorum")
            checksleep(SLEEP, kwdedect, 35, "Kısa bir mola veriyorum", "Günaydın")
            checksleep(LONGSLEEP, kwdedect, 120, "Uzun bir mola veriyorum", "Günaydın")

            for i in QUIT:
                if kwdedect.count(i) >= 1:
                    speak("İyi günler")
                    print(tarih + " Çıkış yapılıyor...")
                    quit()


            time.sleep(1)
    except TypeError:
        print("Algılanamadı.")
