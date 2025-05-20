import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init()

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

def main():
    
    engine.say("Kalkulator jest gotowy do pracy.")
    engine.say("Wprowadź operację, którą chcesz wykonać. Powiedz 'stop', aby zakończyć program.")
    engine.runAndWait()
    time.sleep(5)
    
    while True:

        print('Wprowadź operację...')
        inp = voice_to_text().lower()
        
        if 'stop' in inp:
            print('Do widzenia!')
            break
        
        else:
            
            interpreted = inp.replace("otwórz nawias", "(").replace("zamknij nawias", ")").replace("plus", "+").replace("minus", "-").replace("razy", "*").replace("dzielone przez", "/").replace("do potęgi", "**").replace("silnia", "factorial").replace("pierwiastek", "sqrt").replace("równa się", "")
            print(f"Działanie: {interpreted}")
            
            try:
                wynik = eval(interpreted.strip())
                print(f"Wynik to {wynik}")
                time.sleep(3)
            except (SyntaxError, TypeError):
                print("Niepoprawne wyrażenie.")
                time.sleep(3)
            except NameError as e:
                print(f"Błąd: {e}")
                time.sleep(3)
                
            
            continue
        
         
    
    
if __name__ == "__main__":
    main()