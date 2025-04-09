import webbrowser
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.say("Cześć, jak się masz?")
engine.runAndWait()

#voices = engine.getProperty('voices')
#for voice in voices:
   #print(voice.id,voice.languages)
   #engine.setProperty('voice', voice.id)

speech = sr.Recognizer()

def voice_to_text():
 voice_input = ""
 with sr.Microphone() as source:
  speech.adjust_for_ambient_noise(source)
  try:
   audio = speech.listen(source)
   voice_input = speech.recognize_google(audio,language='pl')
  except sr.UnknownValueError:
   pass
  except sr.RequestError:
   pass
  except sr.WaitTimeoutError:
   pass
 return voice_input

while True:

 engine.say("Pajton Cię słucha")
 engine.runAndWait()

 #print('Python Cię słucha...')
 inp = voice_to_text()
 print(f'Powiedziałeś {inp}.')
 if 'stop' in inp.lower():
  print('Do widzenia!')
  break
 elif "przeglądarka" in inp.lower():
  inp = inp.replace('przeglądarka','')
  adres = "http://" + inp.replace(' krokpa ','.').strip()
  print('adres=',adres)
  flag = webbrowser.open(adres)
  print(flag)
  continue