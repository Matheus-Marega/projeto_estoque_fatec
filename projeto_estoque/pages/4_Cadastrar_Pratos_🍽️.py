import streamlit as st
from pages.Funcao_produtos.registrar_entrada_produtos import verificar_produtos_do_banco
from pages.funcao_pratos.cadastro_qtd_ingredientes import cadastrar_pratos

if "ingredientes" not in st.session_state:
    st.session_state['ingredientes'] = []
if 'nome_prato' not in st.session_state:
    st.session_state['nome_prato'] = ""
if "categoria_prato" not in st.session_state:
    st.session_state['categoria_prato'] = ""
if 'etapa_cadastro' not in st.session_state:
    st.session_state['etapa_cadastro'] = False

st.title("Cadastrar Pratos")

if not st.session_state['etapa_cadastro']:
    nome_prato = st.text_input("Nome do prato", key="nome_prato")
    ingredientes = st.multiselect("Ingredientes", verificar_produtos_do_banco(), key="ingredientes")
    categoria_prato = st.selectbox("Categoria", ["Entrada", "Prato Principal", "Sobremesa"], key="categoria")
    proximo = st.button("Próximo", key="proximo")

    if proximo:
        if not nome_prato:
            st.error("Preencha o nome do prato")
        elif not ingredientes:
            st.error("Selecione os ingredientes")
        else:
            st.session_state['etapa_cadastro'] = True
            st.rerun()
else:
    cadastrar_pratos()