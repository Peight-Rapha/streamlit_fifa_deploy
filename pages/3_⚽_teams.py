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

# Filtrar pelo clube selecionado
df_filtered = df_data[df_data['Club'] == club]

# Criando seletor de posição com base no clube filtrado
posicoes = df_filtered['Position'].unique()
posicao = st.sidebar.selectbox("Position", posicoes)

# Filtrar pelo posição selecionada
df_filtered = df_filtered[df_filtered['Position'] == posicao].set_index('Name')

# Exibir informações do clube e posição
if not df_filtered.empty:
    st.image(df_filtered.iloc[0]["Club Logo"])
    st.markdown(f"## {club}")
    st.markdown(f"**Posição:** {posicao}")

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
                     "Wage(£)": st.column_config.ProgressColumn(
                         "Weekly Wage", format = "£%d", min_value=0, max_value=df_filtered["Wage(£)"].max()
                     ),
                     "Photo": st.column_config.ImageColumn(),
                     "Flag": st.column_config.ImageColumn("Country")
                })
else:
    st.warning("Nenhum jogador encontrado para esse clube e posição.")