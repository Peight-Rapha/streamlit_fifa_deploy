import streamlit as st

# Ajustando o layout para aumenta wide
st.set_page_config(
    page_title="Player",
    page_icon="🏃‍➡️",
    layout="wide"
)

df_data = st.session_state['data']
df_data.columns.to_list()

# Criando seletor de clubes
clubes = df_data['Club'].unique()
club = st.sidebar.selectbox("Club", clubes)

# Cruiando selector de jogadores com filtro de clube
df_players = df_data[df_data['Club'] == club] # Filtrando jogadores do clube selecionado
players = df_players['Name'].unique() # Filtrando jogadores do clube selecionado
player = st.sidebar.selectbox("Jogador", players) # Criando selector de jogadores com filtro de clube

player_stats = df_players[df_players['Name'] == player] # Filtrando jogadores do clube selecionado

st.image(player_stats['Photo'].values[0], width=50) # Exibindo imagem do jogador
st.title(player_stats['Name'].values[0])

st.markdown(f"**Clube:** {player_stats['Club'].values[0]}")
st.markdown(f"**Posição:** {player_stats['Position'].values[0]}")


col1, col2, col3, col4 = st.columns(4)
# Criando Colunas para 'Age', 'Height', 'Weight'
col1.metric('Idade', player_stats['Age'].values[0])
col2.metric('Altura', player_stats['Height(cm.)'].values[0])
col3.metric('Peso', f"{player_stats['Weight(lbs.)'].values[0]* 0.453:.2f}")
st.divider()

st.subheader(f"Overall: ({player_stats['Overall'].values[0]})")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
# Criando Colunas para 'Valor de Mercado', 'Renumeração semanal', 'Clausula de rescisão'
col1.metric('valor de Mercado', player_stats['Value(£)'].values[0])
col2.metric('Renumeração semanal', player_stats['Wage(£)'].values[0])
col3.metric('Cláusula de rescição', f"{player_stats['Release Clause(£)'].values[0]* 0.453:.2f}")