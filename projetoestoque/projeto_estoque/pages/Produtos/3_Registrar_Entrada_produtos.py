import streamlit as st
from pages.Produtos.Funcao_produtos.registrar_entrada_produtos import verificar_produtos_do_banco
from database.queries import verificar_marca_do_produto, verificar_unidade_medida_produto
from database.queries import adiciona_qtd_produto
from pages.funcao_uteis.validacoes import validar_unidade_de_medida_nos_campos_de_texto2

if "quantidade_produto" not in st.session_state:    
    st.session_state['quantidade_produto'] = 0


st.write("# Registrar Entrada de Produtos")
produto_selecionado = st.selectbox("Selecione o produto", verificar_produtos_do_banco()) #Retorna uma lista de produtos do banco de dados

try:
    marca_produto = verificar_marca_do_produto(produto_selecionado)
    st.subheader(f"*Marca do Produto:* {marca_produto}") #Mostra a marca do produto selecionado

    unidade_medida = verificar_unidade_medida_produto(produto_selecionado)
    st.subheader(f"*Unidade de Medida:* {unidade_medida}") #Mostra a unidade de medida do produto selecionado

    validar_unidade_de_medida_nos_campos_de_texto2(unidade_medida)

    if st.button("Registrar Entrada", key="registrar_entrada"):
        try:
            adiciona_qtd_produto(produto_selecionado,st.session_state['quantidade_produto'] ) #Adiciona a quantidade do produto no banco de dados
            st.success("Entrada registrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao registrar entrada: {e}")
except Exception as e:
    st.error(f"Nenhum produto cadastrado no sistema")
