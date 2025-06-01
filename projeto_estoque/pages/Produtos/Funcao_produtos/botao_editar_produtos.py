import streamlit as st
from database.queries import verificar_info_produtos
from pages.Produtos.Funcao_produtos.registrar_entrada_produtos import verificar_produtos_do_banco


@st.dialog("Alterar Produto")
def editar_produtos_do_estoque():
    if "mostrar_edicao" not in st.session_state:
        st.session_state['mostrar_edicao'] = False

    produto_a_ser_editado = st.selectbox("Selecione o produto que deseja editar", verificar_produtos_do_banco())

    if st.button("Próximo"):
        st.session_state['mostrar_edicao'] = True
        st.subheader("Altere as informações desejadas:")
        produtos2 = verificar_info_produtos(produto_a_ser_editado)
        for i, info in enumerate(produtos2):
            nome_prod = st.text_input(f"*Nome do Produto*", placeholder=info[2], key=f"nome_produto_{i}")
            marca_prod = st.text_input(f"*Marca do Produto*", placeholder=info[1], key=f"marca_produto_{i}")
            unidade_medida = st.selectbox(f"*Unidade de Medida*", options=["Kilograma", "Grama", "Litro", "Mililitro", "Unidade"], index=["Kilograma", "Grama", "Litro", "Mililitro", "Unidade"].index(info[0]), key=f"unidade_medida_{i}")
            quantidade_estoque = st.text_input(f"*Quantidade em Estoque*", placeholder=info[3], key=f"quantidade_estoque_{i}")

        # if nome_prod == st.session_state["nome_produto_"]:
        #     st.session_state["nome_produto_"] = nome_prod
        # if marca_prod == st.session_state["marca_produto_"]:
        #     st.session_state["marca_produto_"] = marca_prod
        # if unidade_medida == st.session_state["unidade_medida_"]:
        #     st.session_state["unidade_medida_"] = unidade_medida
        # if quantidade_estoque == st.session_state["quantidade_estoque_"]:
        #     st.session_state["quantidade_estoque_"] = quantidade_estoque


        st.button("Salvar Alterações", key="salvar_alteracoes")
        