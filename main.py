import streamlit as st

# Configuração visual da Axion3D
st.set_page_config(page_title="Axion3D - Precificação Inteligente", page_icon="🚀")

st.title("🚀 Axion3D: Calculadora de Orçamentos")
st.markdown("---")

# --- 1. IDENTIFICAÇÃO ---
st.subheader("👤 Dados do Cliente")
col_cli1, col_cli2 = st.columns(2)
with col_cli1:
    nome_cliente = st.text_input("Nome do Cliente")
with col_cli2:
    nome_projeto = st.text_input("Nome da Peça/Projeto")

# --- 2. CUSTOS DE IMPRESSÃO (TÉCNICO) ---
st.subheader("⚙️ Custos de Impressão")
c1, c2, c3 = st.columns(3)
with c1:
    peso = st.number_input("Peso Final (g)", min_value=0.0, value=100.0)
    preco_material = st.number_input("Preço Filamento (R$/kg)", value=120.0)
with c2:
    tempo = st.number_input("Tempo Total (horas)", min_value=0.0, value=5.0)
    consumo_maquina = st.number_input("Consumo Máquina (W)", value=150.0)
with c3:
    energia_kwh = st.number_input("Valor kWh (R$)", value=0.85)
    depreciacao_h = st.number_input("Depreciação Máquina/h (R$)", value=0.50)

# --- 3. CUSTOS AGREGADOS (O DIFERENCIAL) ---
st.subheader("🎨 Valor Agregado & Pós-Processamento")
ca1, ca2, ca3 = st.columns(3)
with ca1:
    embalagem = st.number_input("Embalagem (R$)", value=0.0)
    pintura = st.number_input("Pintura/Insumos (R$)", value=0.0)
with ca2:
    iluminacao = st.number_input("LED/Eletrônicos (R$)", value=0.0)
    aderecos = st.number_input("Adereços/Bases (R$)", value=0.0)
with ca3:
    mao_de_obra_pos = st.number_input("Mão de Obra Manual (R$)", value=0.0)
    outros_custos = st.number_input("Outros (R$)", value=0.0)

# --- 4. MARGEM E CÁLCULO FINAL ---
st.markdown("---")
margem_lucro = st.slider("Margem de Lucro (%)", 0, 300, 100)

# Fórmulas
custo_filamento = (preco_material / 1000) * peso
custo_energia = (consumo_maquina / 1000) * tempo * energia_kwh
custo_depreciacao = tempo * depreciacao_h
total_agregados = embalagem + pintura + iluminacao + aderecos + mao_de_obra_pos + outros_custos

custo_total_real = custo_filamento + custo_energia + custo_depreciacao + total_agregados
preco_final = custo_total_real * (1 + (margem_lucro / 100))

# EXIBIÇÃO DO RESULTADO
st.metric(label="PREÇO SUGERIDO PARA VENDA", value=f"R$ {preco_final:.2f}")

# --- 5. GERADOR DE ORÇAMENTO ---
if st.button("✨ GERAR ORÇAMENTO PARA ENVIO"):
    resumo = f"""
*ORÇAMENTO - AXION3D* 🚀
---------------------------------------
👤 *Cliente:* {nome_cliente}
📦 *Projeto:* {nome_projeto}

*Detalhes do Serviço:*
- Impressão 3D de alta precisão
- Pós-processamento e acabamento personalizado
- Tempo de produção: {tempo} horas

*Investimento:*
💰 *Valor Total: R$ {preco_final:.2f}*
---------------------------------------
💳 Formas de pagamento: [Inserir Suas Opções]
🚚 Prazo de entrega: [X] dias úteis.
✅ Validade: 5 dias.

_Axion3D - Transformando ideias em realidade._
    """
    st.text_area("Copie e envie ao cliente:", resumo, height=250)
