import streamlit as st
from database.models import criar_tabela_cadastro_produtos
from database.queries import cadastrar_produto_DB,verificar_se_produto_ja_existe_no_DB


def cadastrar_produto(nome_produto, unidade_medida, marca_produto):
    if st.button("Cadastrar Produto", key="cadastrar_produto"):
        try:
            criar_tabela_cadastro_produtos()
        except:
            print("Tabela PRODUTOS já existe.")

        if st.session_state.get("nome_produto_cadastro") == "":
            st.error("O nome do produto não pode ser vazio!")
        else:
            if verificar_se_produto_ja_existe_no_DB(nome_produto):
                st.error("Produto de mesmo nome já cadastrado!")
            else:
                cadastrar_produto_DB(nome_produto, unidade_medida, marca_produto, quantidade=0) #Adiciona o produto no banco de dados
                st.success("Produto cadastrado com sucesso!")
