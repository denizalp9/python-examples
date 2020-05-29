from gtts import  gTTS # google text-to-speech(Yazıyı sese dönüştürme) modülü
import playsound # Pythonda ses oynatma modülü
import speech_recognition as sr # google speech-to-text(Sesi yazıya dönüştürme) modülü

# Burada yaptığım şey basitçe bir metini ses dosyasına çevirip aynı ses dosyasını çalmak.

def speak(text):
    tts = gTTS(text=text, lang="tr") # text = okunacak metin, lang = dil (örn: eng, tr, fr)
    file = "testaudio.mp3" # Metini sese çevirdikten sonra kaydetmesi için bir dosya adı seçiyorum.
    tts.save(file) # Yukarıda belirlediğim isimli bir dosya kaydeder

    playsound.playsound(file) # Programı kullanan kişinin bu sesi duyması için dosyayı oynatıyorum

speak("Enes Batur")