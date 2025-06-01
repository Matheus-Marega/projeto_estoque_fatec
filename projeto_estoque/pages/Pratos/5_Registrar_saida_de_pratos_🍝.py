import streamlit as st
from database.queries import validacao_quantidade_de_produtos_em_estoque_para_registrar_saida_de_pratos,verificar_ingredientes_cadastrados_no_prato
from pages.Pratos.funcao_pratos.registrar_saida_pratos import registrar_saida_pratos,formatar_nome_prato


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.title("Registrar Saída de Pratos 🍝")

prato = st.selectbox("Selecione o prato", formatar_nome_prato())
st.number_input("Quantidade", min_value=1, step=1)
#st.text_area("Observações")
ingredientes_no_prato = verificar_ingredientes_cadastrados_no_prato(prato)
if st.button("Registrar Saída"):
    counter = 0
    for ingrediente in ingredientes_no_prato:
        validacao = validacao_quantidade_de_produtos_em_estoque_para_registrar_saida_de_pratos(prato)
        print(validacao)
        if validacao[0] <= 0:
            st.error(f"Não há ingredientes suficientes para registrar a saída do prato: {prato}")
            st.error(f"Produtos insuficientes: {ingrediente}")
            break
        else:
            counter += 1
        while counter < len(ingredientes_no_prato):
            registrar_saida_pratos(prato)
            del st.session_state[counter]