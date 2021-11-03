import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
import time
from transformers import pipeline
# zaczynamy od zaimportowania bibliotek

# st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

def load_csv():
    df = pd.read_csv("cwiczenie_1.csv", sep = ';')
    return st.dataframe(df)


# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Aplikacja tłumacząca tekst 🐱‍🐉')
# st.balloons()
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

# st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

#st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

#st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.
# st.spinner()
# with st.spinner(text='Pracuję... 👀'):
#     time.sleep(2)
#     # st.success('Done 🎉')
#     load_csv()

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
st.write('W aplikacji możesz wpisać tekst po angielsku i sprawdzić wydzwięk tekstu oraz przetłumaczyć tekst na niemiecki')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

#st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

#with st.echo():
#    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy




# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Przetwarzanie języka naturalnego')
st.write('Wybierz z dostępnych opcji to czego potrzebujesz i wpisz tekst')

def tlumacz_tekstu():
    option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumacz z angielskiego na niemiecki",
    ],
)
    if option == "Wydźwięk emocjonalny tekstu (eng)":
        text = st.text_area(label="Wpisz tekst")
        if text:
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
            st.write(answer)
    elif option == "Tłumacz z angielskiego na niemiecki":
        text = st.text_area(label="Wpisz tekst")
        if text:
            classifier = pipeline("translation_en_to_de")
            answer = classifier(text)
            st.write(answer)

with st.spinner(text='Pracuję... 👀'):
    time.sleep(6)
    tlumacz_tekstu()
    st.balloons()
    



st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')

st.write("❤️ Numer studenta: S15134")
