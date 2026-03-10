import streamlit as st
from modules.dashboard import dashboard
from modules.calculadora import calculadora
from modules.estoque import estoque
from modules.clientes import clientes
from modules.vendas import vendas

st.set_page_config(page_title="Axion3D Manager", layout="wide")

st.title("Axion3D - Gestão de Impressão 3D")

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard","Novo Orçamento","Clientes","Estoque","Vendas"]
)

if menu == "Dashboard":
    dashboard()

elif menu == "Novo Orçamento":
    calculadora()

elif menu == "Clientes":
    clientes()

elif menu == "Estoque":
    estoque()

elif menu == "Vendas":
    vendas()
