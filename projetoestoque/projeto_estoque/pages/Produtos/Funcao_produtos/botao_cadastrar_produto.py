import streamlit as st
from database.models import criar_tabela_cadastro_produtos
from database.queries import cadastrar_produto_DB


def cadastrar_produto(nome_produto, unidade_medida, marca_produto):
    if st.button("Cadastrar Produto", key="cadastrar_produto"):
        try:
            criar_tabela_cadastro_produtos()
        except:
            print("Tabela PRODUTOS já existe.")

        cadastrar_produto_DB(nome_produto, unidade_medida, marca_produto, quantidade=0) #Adiciona o produto no banco de dados
        st.success("Produto cadastrado com sucesso!")