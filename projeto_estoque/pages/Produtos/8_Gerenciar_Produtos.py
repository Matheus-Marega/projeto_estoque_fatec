import streamlit as st
from pages.Produtos.Funcao_produtos.registrar_entrada_produtos import verificar_produtos
from database.queries import verificar_info_produtos
from pages.Produtos.Funcao_produtos.botao_editar_produtos import editar_produtos_do_estoque




if "botao_editar" not in st.session_state:
    st.session_state["botao_editar"] = False


st.title("Produtos em Estoque")
botao_editar = st.button("Editar Produtos", key="editar_produtos")
if botao_editar:
    editar_produtos_do_estoque()


st.divider()

if verificar_produtos() == []:
    st.error("Nenhum produto cadastrado no sistema")
    st.stop()
else:
    for produtos in verificar_produtos():
        produtos2 = verificar_info_produtos(produtos)
        for info in produtos2:
            st.markdown(f"*Nome do Produto*: {info[2]}")
            st.markdown(f"*Marca do Produto*: {info[1]}")
            st.markdown(f"*Unidade de Medida*: {info[0]}")
            st.markdown(f"*Quantidade em Estoque*: {info[3]}")
            st.divider()