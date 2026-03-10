import streamlit as st
import pandas as pd
import os
import datetime
import urllib.parse

st.set_page_config(page_title="Axion3D Pro", layout="wide")
st.image("", width=200)
st.title("🚀 Axion3D - Gestao")

if not os.path.exists("estoque.csv"):
pd.DataFrame([{"Item": "PLA", "Qtd": 1000.0}]).to_csv("estoque.csv", index=False)

df_e = pd.read_csv("estoque.csv")

menu = st.sidebar.radio("Navegacao", ["Calculadora", "Estoque", "Vendas"])

if menu == "Calculadora":
st.header("Novo Orcamento")
nome = st.text_input("Cliente")
whats = st.text_input("WhatsApp (55...)")
peca = st.text_input("Nome da Peca")
peso = st.number_input("Peso (g)", value=50.0)
tempo = st.number_input("Tempo (h)", value=2.0)
total = ((peso * 0.15) + (tempo * 1.50)) * 2
st.subheader(f"Total: R$ {total:.2f}")
if st.button("SALVAR E BAIXAR ESTOQUE"):
df_e.loc[0, "Qtd"] -= peso
df_e.to_csv("estoque.csv", index=False)
if os.path.exists("vendas.csv"):
df_v = pd.read_csv("vendas.csv")
else:
df_v = pd.DataFrame(columns=["Data", "Cliente", "Peca", "Valor"])
nova_venda = pd.DataFrame([{"Data": datetime.datetime.now().strftime("%d/%m/%Y"), "Cliente": nome, "Peca": peca, "Valor": total}])
df_v = pd.concat([df_v, nova_venda], ignore_index=True)
df_v.to_csv("vendas.csv", index=False)
st.success("Venda registrada com sucesso!")
msg_zap = f"Axion3D - Orcamento: {peca}. Valor: R$ {total:.2f}"
link = f"{whats}?text={urllib.parse.quote(msg_zap)}"
st.markdown(f'a href="{link}" target="_blank" Enviar WhatsApp /a', unsafe_allow_html=True)

if menu == "Estoque":
st.header("Estoque")
st.write(df_e)
if st.button("Resetar Estoque para 1000g"):
df_e.loc[0, "Qtd"] = 1000.0
df_e.to_csv("estoque.csv", index=False)
st.rerun()

if menu == "Vendas":
st.header("Historico")
if os.path.exists("vendas.csv"):
st.dataframe(pd.read_csv("vendas.csv"))
else:
st.write("Nenhuma venda encontrada.")
