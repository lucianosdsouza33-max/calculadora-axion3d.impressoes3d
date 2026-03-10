import streamlit as st
import pandas as pd
import os
import datetime
import urllib.parse

st.set_page_config(page_title="Axion3D", layout="wide")
LOGO = "https://i.ibb.co/LzNfX7z/axion3d-logo.png"
st.image(LOGO, width=200)

def abrir(n):
    if os.path.exists(n): return pd.read_csv(n)
    return pd.DataFrame()

db_e = "est.csv"
df_e = abrir(db_e)
if df_e.empty: df_e = pd.DataFrame([{"Item":"PLA","Qtd":1000}])

menu = st.sidebar.radio("Menu", ["Calculadora", "Estoque"])

if menu == "Calculadora":
    n = st.text_input("Cliente")
    p = st.number_input("Peso (g)", 50)
    t = st.number_input("Horas", 2)
    v = ((p * 0.15) + (t * 1.5)) * 2
    st.write(f"Preço: R$ {v}")
    if st.button("Confirmar"):
        df_e.loc[0,"Qtd"] -= p
        df_e.to_csv(db_e, index=False)
        st.success("Vendido!")

else:
    st.write(df_e)
    if st.button("Resetar 1kg"):
        df_e.loc[0,"Qtd"] = 1000
        df_e.to_csv(db_e, index=False)
        st.rerun()
