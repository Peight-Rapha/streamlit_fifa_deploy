import streamlit as st

st.set_page_config(
    page_title="Player",
    page_icon="🏃‍➡️",
    layout="wide"
)

# Ler o conjunto de dados salvo no state
df_data = st.session_state['data']

# Criando seletor de clubes
clubes = df_data['Club'].unique()
club = st.sidebar.selectbox("Club", clubes)
# Montar novo dataframe com base no que foi filtrado no clube
df_filtered = df_data[df_data['Club'] == club].set_index('Name')

st.markdown(f"**Posição:** {df_filtered['Position'].values[0]}")
# filtrando pela posição
df_filtered = df_filtered[df_filtered['Position'] == df_filtered['Position'].values[0]]

# Criando selector de imagem do club
st.image(df_filtered.iloc[0]["Club Logo"])
# Criando subtítul com o nome do clube
st.markdown(F"## {club}")

# Lista nome das colunas do df_filtered
columns = df_filtered.columns.to_list()

# Selecionando colunas desejadas
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", 
           "Height(cm.)", "Weight(lbs.)", 
           "Contract Valid Until", "Release Clause(£)"]

# Criar um dataframe usando streamlit para permitir personalização
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format= "%d", min_value=0, max_value=100
                 ),
                 # Personalizar coluna "Wage(£)" por renumeração mais alta
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format = "£%d", min_value=0, max_value=df_filtered["Wage(£)"].max()
                 ),
                 # Configurar "Photo" como imagem
                 "Photo": st.column_config.ImageColumn(),
                 # Bandeira do clube
                 "Flag": st.column_config.ImageColumn("Country")
            })