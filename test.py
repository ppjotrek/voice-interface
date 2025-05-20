import speech_recognition as sr
import pyttsx3
import ast

def kalkulator_nawiasy():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Powiedz polecenie z nawiasami...")
        audio = r.listen(source)

    try:
        tekst = r.recognize_google(audio, language='pl-PL').lower()
        print(f"Rozpoznano: {tekst}")

        tekst = tekst.replace("otwórz nawias", "(").replace("zamknij nawias", ")").replace("plus", "+").replace("minus", "-").replace("razy", "*").replace("dzielone przez", "/").replace("do potęgi", "**").replace("równa się", "")

        print(f"Zinterpretowano: {tekst}")

        try:
            wynik = ast.literal_eval(tekst.strip())
            engine.say(f"Wynik to {wynik}")
            engine.runAndWait()
        except (SyntaxError, TypeError):
            engine.say("Niepoprawne wyrażenie.")
            engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("Nie rozumiem, powtórz proszę.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Błąd połączenia z API Google: {e}")
        engine.say("Wystąpił błąd z rozpoznawaniem mowy.")
        engine.runAndWait()

if __name__ == "__main__":
    kalkulator_nawiasy()