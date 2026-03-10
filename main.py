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
lucro = st.slider("Margem de Lucro (%)", 50, 500, 100)
extras = st.number_input("Custos Extras (Pintura/Leds)", value=0.0)

if st.button("SALVAR VENDA"):
    df_e.loc[0, "Qtd"] -= peso
df_e.to_csv("estoque.csv", index=False)
if os.path.exists("vendas.csv"):
    df_v = pd.read_csv("vendas.csv")
else:
    df_v = pd.DataFrame(columns=["Data", "Cliente", "Peca", "Valor"])
nova_v = pd.DataFrame([{"Data": datetime.datetime.now().strftime("%d/%m/%Y"), "Cliente": nome, "Peca": peca, "Valor": total}])
df_v = pd.concat([df_v, nova_v], ignore_index=True)
df_v.to_csv("vendas.csv", index=False)
st.success("Venda salva!")

msg = f"Axion3D: {peca}. Valor: R$ {total:.2f}"
link = f"https://wa.me/{whats}?text={urllib.parse.quote(msg)}"
st.markdown(f"[link suspeito removido]")

if menu == "Vendas":
    st.header("Historico")
if os.path.exists("vendas.csv"):
    st.dataframe(pd.read_csv("vendas.csv"))
else:
    st.write("Nenhuma venda encontrada.")
