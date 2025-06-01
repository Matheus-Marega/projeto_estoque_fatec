import streamlit as st
from pages.Produtos.Funcao_produtos.botao_cadastrar_produto import cadastrar_produto

if "nome_produto_cadastro" not in st.session_state:
    st.session_state.nome_produto_cadastro = ""

st.title("Cadastrar Produtos no Estoque ✏️")

nome_produto = st.text_input("Nome do Produto",key="nome_produto_cadastro")
unidade_medida = st.selectbox("Unidade de Medida", ["Kilograma", "Grama", "Litro", "Mililitro","Unidade"])
marca_produto = st.text_input("Marca do Produto")
cadastrar_produto(nome_produto, unidade_medida, marca_produto)
