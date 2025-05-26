import streamlit as st
import webbrowser
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="Player",
    page_icon="🏃‍➡️",
    layout="wide"
)

st.markdown("# FIFA23 OFFICIAL DATASET ⚽")
st.sidebar.markdown("Desenvolvido por Raphael Silva")

if "data" not in st.session_state:
    df_data = pd.read_csv("C:\\asimov\\Streamlit\\Projeto Streamlit FIFA - Raphael\\datasets\\CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] > datetime.today().year]
    ##df_data.columns
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state["data"] = df_data


btn = st.button("Acesse os dados do Kaggle")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/nyagami/ea-sports-fc-25-database-ratings-and-stats")

st.markdown("""## Sobre o Projeto

Este projeto utiliza um dataset oficial do FIFA 23, trazendo informações detalhadas sobre jogadores, clubes e ligas presentes no jogo. Aqui, você poderá explorar estatísticas, comparar atributos e visualizar dados relevantes para análises esportivas e curiosidades do universo do futebol virtual.

Os dados foram obtidos a partir do Kaggle e são ideais para quem deseja conhecer melhor o desempenho dos atletas, identificar talentos e entender as tendências do futebol digital.

Aproveite para navegar pelas diferentes seções e descobrir insights sobre o mundo do FIFA 23!""")
