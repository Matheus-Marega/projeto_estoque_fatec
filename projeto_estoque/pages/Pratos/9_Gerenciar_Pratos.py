import streamlit as st
from database.queries import verificar_pratos_no_banco, verificar_info_utilizada_nos_pratos

# if "bt_editar_pratos" not in st.session_state:
#     st.session_state["bt_editar_pratos"] = False


st.title("Gerenciar Pratos")
botao_editar_pratos = st.button("Editar Pratos", key="bt_editar_pratos")
if botao_editar_pratos:
    st.text("Funcionalidade de edição de pratos ainda não implementada.")


st.divider()

if verificar_pratos_no_banco == []:
    st.error("Nenhum prato cadastrado no sistema")
    st.stop()
else:
    for pratos in verificar_pratos_no_banco():
        st.header(f"{pratos[0]}")
        st.subheader("Ingredientes utilizados:")
        produtos_no_prato = verificar_info_utilizada_nos_pratos(pratos)
        for info in produtos_no_prato:
            st.badge(f"*Nome do Produto*: {info[0][0]}           /          Quantidade Utilizada: {info[1][0]}           /          Unidade de Medida: {info[2][0]}",color="primary")
        st.divider()
