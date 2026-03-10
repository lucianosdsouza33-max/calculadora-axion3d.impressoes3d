import streamlit as st
import urllib.parse
import pandas as pd
import datetime
import os
st.set_page_config(page_title="Axion3D Pro", page_icon="🚀", layout="wide")
LINK_LOGO = ""
st.markdown(f'center img src="{LINK_LOGO}" width="200" /center', unsafe_allow_html=True)
def carregar(arq, col):
if os.path.exists(arq): return pd.read_csv(arq)
return pd.DataFrame(columns=col)

def salvar(df, arq): df.to_csv(arq, index=False)

ARQ_PED = "pedidos_axion3d.csv"
ARQ_EST = "estoque_axion3d.csv"
cols_p = ["Data", "Cliente", "Projeto", "Material", "Peso", "Valor"]
cols_e = ["Item", "Quantidade", "Alerta"]

df_est = carregar(ARQ_EST, cols_e)
if df_est.empty:
df_est = pd.DataFrame([{"Item": "PLA", "Quantidade": 1000.0, "Alerta": 200.0}])
salvar(df_est, ARQ_EST)
menu = st.sidebar.selectbox("Menu", ["Calculadora", "Estoque", "Historico"])

if menu == "Calculadora":
st.header("📐 Novo Orcamento")
nome = st.text_input("Cliente")
whats = st.text_input("WhatsApp (Ex: 5551999998888)")
peca = st.text_input("Peca")
mat_sel = st.selectbox("Material", df_est["Item"].tolist())
peso = st.number_input("Peso (g)", value=50.0)
tempo = st.number_input("Tempo (h)", value=2.0)
lucro = st.slider("Lucro %", 50, 400, 100)

elif menu == "Estoque":
st.header("📦 Estoque")
st.dataframe(df_est)
item = st.selectbox("Ajustar", df_est["Item"].tolist())
qtd = st.number_input("Nova Qtd (g)", value=1000.0)
if st.button("Atualizar"):
df_est.loc[df_est['Item'] == item, 'Quantidade'] = qtd
salvar(df_est, ARQ_EST)
st.rerun()

else:
st.header("📜 Historico")
st.table(carregar(ARQ_PED, cols_p))
