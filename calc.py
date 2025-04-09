import webbrowser
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.say("Witaj w kalkulatorze!")
engine.runAndWait()

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
    
    while True:
        
        engine.say("Powiedz 'stop', aby zakończyć program.")

        print('Mów teraz')
        inp = voice_to_text()
        print(f'Usłyszałem "{inp}".')
        
        if 'stop' in inp.lower():
            print('Do widzenia!')
            break
        
        else:
            parsed_input = inp.split()
            
            if len(parsed_input) == 3:
                try:
                    num1 = float(parsed_input[0].replace(",", "."))
                    operator = parsed_input[1]
                    num2 = float(parsed_input[2].replace(",", "."))
                    
                    print("Zrozumiano operację: ", num1, operator, num2)
                    engine.say("Liczę")
                    
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*' or operator == 'x':
                        result = num1 * num2
                    elif operator == '/':
                        result = num1 / num2
                    else:
                        raise ValueError("Nieznany operator")
                    
                    print(f"Wynik to {result}.")
                except ValueError:
                    print("Nie rozpoznano operatora. Może nie jest zaimplementowany?")
            else:
                print("Nie rozpoznano danych wejściowych. Spróbuj jeszcze raz...")
                
            continue
        
         
    
    
if __name__ == "__main__":
    main()