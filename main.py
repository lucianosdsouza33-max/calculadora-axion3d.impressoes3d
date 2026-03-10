import streamlit as st
import pandas as pd
import os
import datetime
import urllib.parse

st.set_page_config(page_title="Axion3D Pro", layout="wide")

try:
    st.image("", width=220)
except:
    st.title("Axion3D - Gestao")

if not os.path.exists("estoque.csv"):
    pd.DataFrame([{"Item": "PLA", "Qtd": 1000.0}]).to_csv("estoque.csv", index=False)

df_e = pd.read_csv("estoque.csv")

menu = st.sidebar.radio("Navegacao", ["Calculadora", "Estoque", "Vendas"])

if menu == "Calculadora":
    st.header("Novo Orcamento")
nome = st.text_input("Cliente")
whats = st.text_input("WhatsApp (Ex: 5551999998888)")
peca = st.text_input("Nome da Peca")
peso = st.number_input("Peso (g)", value=50.0)
tempo = st.number_input("Tempo (h)", value=2.0)
total = ((peso * 0.15) + (tempo * 1.50)) * 2
st.subheader(f"Total: R$ {total:.2f}")

if menu == "Estoque":
    st.header("Estoque")
st.write(df_e)
if st.button("Resetar 1000g"):
    df_e.loc[0, "Qtd"] = 1000.0
df_e.to_csv("estoque.csv", index=False)
st.rerun()

if menu == "Vendas":
    st.header("Historico")
if os.path.exists("vendas.csv"):
    st.dataframe(pd.read_csv("vendas.csv"))
else:
    st.write("Nenhuma venda encontrada.")
