import streamlit as st
from pages.Funcao_produtos.botao_cadastrar_produto import cadastrar_produto

st.title("Cadastrar Produtos")

nome_produto = st.text_input("Nome do Produto")
unidade_medida = st.selectbox("Unidade de Medida", ["Kilograma", "Grama", "Litro", "Mililitro","Unidade"])
marca_produto = st.text_input("Marca do Produto")
cadastrar_produto(nome_produto, unidade_medida, marca_produto)
