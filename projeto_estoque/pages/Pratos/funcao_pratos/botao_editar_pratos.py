import streamlit as st
from database.queries import verificar_info_produtos, atualizar_produto
from pages.Produtos.Funcao_produtos.registrar_entrada_produtos import verificar_pratos_no_banco,verificar_info_utilizada_nos_pratos

@st.cache_data
def pratos_cache():
    return verificar_pratos_no_banco()

@st.dialog("Alterar Pratos Cadastrados")
def editar_pratos_cadastrados():
    if "prato_a_editar" not in st.session_state:
        st.session_state["prato_a_editar"] = None

    editar_pratos_cadastrados = pratos_cache()
    prato_a_ser_editado = st.selectbox("Selecione o prato", editar_pratos_cadastrados)

    if st.button("Editar"):
        while True:
            try:
                st.session_state["prato_a_editar"] = prato_a_ser_editado
                pratos_cache.clear()
                break
            except IndexError:
                continue



# CONTINUAR APARTIR DAQUI.

# O QUE PRECISA SER FEITO: CRIAR UMA QUERIE QUE PUXA TODAS AS INFORMAÇÕES DO PRATO SELECIONADO(NOME DO PRATO, 
# QUANTIDADE UTILIZADA, UNIDADE DE MEDIDA E NOME DO INGREDIENTE), E ENTÃO
# CRIAR UM FORMULARIO PARA EDITAR AS INFORMAÇÕES DO PRATO, E ENTÃO ATUALIZAR O PRATO NO BANCO DE DADOS.
# FUNCAO INICIADA EM verificar_info_cadastradas_nos_pratos 


    if st.session_state["prato_a_editar"]:
        dados = verificar_info_utilizada_nos_pratos(st.session_state["prato_a_editar"])
        info = dados[0]  # Pega a primeira tupla

        with st.form("form_edicao"):
            nome = st.text_input("Nome do Produto", value=st.session_state["prato_a_editar"])
            marca = st.text_input("Marca do Produto", value=info[1])
            unidade = st.selectbox("Unidade de Medida",
                                   ["Kilograma", "Grama", "Litro", "Mililitro", "Unidade"],
                                   index=["Kilograma", "Grama", "Litro", "Mililitro", "Unidade"].index(info[0]))
            qtd = st.text_input("Quantidade em Estoque", value=info[3])
            submit = st.form_submit_button("Salvar Alterações")

            if submit:
                atualizar_produto(nome, marca, unidade, qtd)
                st.success("Produto atualizado com sucesso!")
                st.session_state["produto_a_editar"] = None
                pratos_cache.clear()

                st.rerun()