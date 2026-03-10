import streamlit as st
import pandas as pd
import os
import datetime
import urllib.parse

st.set_page_config(page_title="Axion3D Pro", layout="wide")

LINK_LOGO = ""

def carregar(arq, col):
if os.path.exists(arq):
try: return pd.read_csv(arq)
except: return pd.DataFrame(columns=col)
return pd.DataFrame(columns=col)

def salvar(df, arq):
df.to_csv(arq, index=False)

ARQ_P = "pedidos_axion.csv"
ARQ_E = "estoque_axion.csv"

df_e = carregar(ARQ_E, ["Item", "Qtd", "Alerta"])
if df_e.empty:
df_e = pd.DataFrame([{"Item": "PLA", "Qtd": 1000.0, "Alerta": 200.0}])
salvar(df_e, ARQ_E)

st.markdown(f'center img src="{LINK_LOGO}" width="200" /center', unsafe_allow_html=True)

menu = st.sidebar.selectbox("Menu", ["Calculadora", "Estoque", "Vendas"])

if menu == "Calculadora":
st.header("Novo Orcamento")
nome = st.text_input("Cliente")
whats = st.text_input("WhatsApp (Ex: 5551999998888)")
peca = st.text_input("Projeto")
peso = st.number_input("Peso (g)", value=50.0)
tempo = st.number_input("Tempo (h)", value=2.0)
lucro = st.slider("Lucro %", 50, 500, 100)

elif menu == "Estoque":
st.header("Estoque")
st.write(df_e)
if st.button("Resetar para 1000g"):
df_e.loc[0, "Qtd"] = 1000.0
salvar(df_e, ARQ_E)
st.rerun()

else:
st.header("Historico")
st.dataframe(carregar(ARQ_P, ["Data", "Cliente", "Peca", "Valor"]))
