import streamlit as st
from database.queries import verificar_pratos_no_banco
from pages.Pratos.funcao_pratos.registrar_saida_pratos import registrar_saida_pratos,formatar_nome_prato

st.title("Registrar Saída de Pratos")

prato = st.selectbox("Selecione o prato", formatar_nome_prato())
st.number_input("Quantidade", min_value=1, step=1)
#st.text_area("Observações")
if st.button("Registrar Saída"):
    registrar_saida_pratos(prato)