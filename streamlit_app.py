import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
import time
from transformers import pipeline


st.title('Aplikacja tłumacząca tekst 🐱‍🐉')
st.success('Wszystko działa!')
st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
st.write('W aplikacji możesz wpisać tekst po angielsku i sprawdzić wydzwięk tekstu oraz przetłumaczyć tekst na niemiecki')
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

st.error("❤️ Numer studenta: S15134")
