import streamlit as st
import pandas as pd
import random

st.title('Simulador de Lançamento de Moedas')

flips = st.number_input('Quantas vezes você quer lançar a moeda?', min_value=1, value=10)

if st.button('Lançar'):
    results = [random.choice(['Cara', 'Coroa']) for _ in range(flips)]
    df = pd.DataFrame(results, columns=['Resultado'])
    st.write(df['Resultado'].value_counts())
    st.bar_chart(df['Resultado'].value_counts())
