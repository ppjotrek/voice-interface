######################################
Instalacja środowiska wirtualnego

1. Przejdź na:
https://docs.conda.io/en/latest/miniconda.html
2. Ściągnij Miniconda3 Windows 64-bit
3. Uruchom Anaconda Prompt ze Start Menu Windows
4.Przejdź do kartoteki ze skryptami (jest tam również plik conda.yml)
5. Wykonaj polecenie: conda env create -f conda.yml
6. Aktywuj środowisko wirtualne:
   conda activate speech
7. Deaktywuj środowisko:
   conda deactivate
8. Zamknij Anaconda Prompt

Instalacja jest zakończona

###################################
Użycie środowiska

1. Przed wykonaniem skryptów należy ponownie uruchomić Anaconda Prompt

2. Przechodzę do kartoteki ze skryptami

3. Aktywowanie środowiska:
conda activate speech

4. Uruchamiam skrypty w Anaconda Prompt:
python main.py

5. Instalacja dodatkowych bibliotek np. TTS:
pip install pyttsx3

Laboratorium 1
Uruchomienie przykładowych skryptów

Laboratorium 2
Zaprojektować aplikację, wykorzystującą API Google np. kalkulator, do którego polecenia wydawane są głosowo. 
Kalkulator jest uruchamiamy bez parametrów, następnie kalkulator oczekuje na polecenia. Możliwe stopnie złożoności aplikacji i odpowiadające im oceny:
polecenie z podstawowym działaniem, np. dodawaniem: 2 plus 2 - ocena 3.0,
wykonywanie wszystkich działań 2-argumentowych (+, -, *, /, potęga) - ocena 3.5,
działania jednoargumentowe podawane przed lub za liczbą: pierwiastek z, silnia - ocena 4.0,
nawiasy, np. “otwórz nawias trzy plus siedem zamknij nawias razy sześć równa się” - ocena 4.5,
liczby wielocyfrowe, z zakresu od -999 999 … do 999 999 - ocena 5.0.

Laboratorium 3
Prezentacja aplikacji. Ocena aplikacji (głosowanie, ocena wg. rankingu).
