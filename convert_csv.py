# abrir um arquivo csv converter para excel e salvar na mesma pasta

import pandas as pd
import os

df = pd.read_csv("C:\\asimov\Streamlit\\Projeto Streamlit FIFA\\datasets\\CLEAN_FIFA23_official_data.csv")

# Agora com arquivo aberto converter para excel
excel_path = os.path.join(os.path.dirname(__file__), "CLEAN_FIFA23_official_data.xlsx")
df.to_excel(excel_path, index=False)