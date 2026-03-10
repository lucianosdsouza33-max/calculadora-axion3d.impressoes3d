import streamlit as st
import pandas as pd
import os
import datetime
import urllib.parse

st.set_page_config(page_title="Axion3D Pro", layout="wide")
st.image("", width=200)
if os.path.exists("estoque_axion.csv"):
df_e = pd.read_csv("estoque_axion.csv")
else:
df_e = pd.DataFrame([{"Item": "PLA", "Qtd": 1000.0, "Alerta": 200.0}])
df_e.to_csv("estoque_axion.csv", index=False)

menu = st.sidebar.selectbox("Menu", ["Calculadora", "Estoque", "Vendas"])

if menu == "Calculadora":
st.header("Novo Orcamento")
nome = st.text_input("Cliente")
whats = st.text_input("WhatsApp (Ex: 5551999998888)")
peca = st.text_input("Projeto")
peso = st.number_input("Peso (g)", value=50.0)
tempo = st.number_input("Tempo (h)", value=2.0)
lucro = st.slider("Lucro %", 50, 500, 100)

if menu == "Estoque":
st.header("Estoque")
st.write(df_e)
if st.button("Resetar para 1000g"):
df_e.loc[0, "Qtd"] = 1000.0
df_e.to_csv("estoque_axion.csv", index=False)
st.rerun()

if menu == "Vendas":
st.header("Historico")
if os.path.exists("pedidos_axion.csv"):
st.dataframe(pd.read_csv("pedidos_axion.csv"))
else:
st.write("Nenhuma venda registrada.")
