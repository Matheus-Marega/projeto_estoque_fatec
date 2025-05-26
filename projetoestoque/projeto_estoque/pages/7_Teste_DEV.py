import streamlit as st
from database.queries import verificar_produtos
from pages.Funcao_produtos.registrar_entrada_produtos import registrar_entrada_produtos

st.title("Teste de Desenvolvimento")
if st.button("Teste Retorno Produtos",key="teste_retorno_produtos"):
    print(registrar_entrada_produtos())