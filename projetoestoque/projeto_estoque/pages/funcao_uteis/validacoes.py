import streamlit as st

def validar_unidade_de_medida_nos_campos_de_texto(unidade_medida, indice_key_number_input):

    if "quantidade_produto" not in st.session_state:
        st.session_state["quantidade_produto"] = 0
    
    if unidade_medida in ["Kilograma","Grama","Litro","Mililitro"]:
        tipo_de_dado = float
        valor_inicial = 0.0
    elif unidade_medida in ["Unidade"]:
        tipo_de_dado = int
        valor_inicial = 0

    quantidade_produto = st.number_input(
    "Quantidade a ser adicionada:",
    min_value=0.0 if tipo_de_dado == float else 0,
    value=valor_inicial,
    step=0.1 if tipo_de_dado == float else 1,
    format="%.2f" if tipo_de_dado == float else "%d",
    key=f"quantidade_produto{indice_key_number_input}"
    )
    

    return quantidade_produto

import streamlit as st

def validar_unidade_de_medida_nos_campos_de_texto2(unidade_medida):

    if unidade_medida in ["Kilograma","Grama","Litro","Mililitro"]:
        tipo_de_dado = float
        valor_inicial = 0.0
    elif unidade_medida in ["Unidade"]:
        tipo_de_dado = int
        valor_inicial = 0

    quantidade_produto = st.number_input(
    "Quantidade a ser adicionada:",
    min_value=0.0 if tipo_de_dado == float else 0,
    value=valor_inicial,
    step=0.1 if tipo_de_dado == float else 1,
    format="%.2f" if tipo_de_dado == float else "%d",
    )
    st.session_state['quantidade_produto'] = quantidade_produto

    return quantidade_produto



