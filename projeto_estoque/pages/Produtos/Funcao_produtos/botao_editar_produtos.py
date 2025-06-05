import streamlit as st
from database.queries import verificar_info_produtos, atualizar_produto
from pages.Produtos.Funcao_produtos.registrar_entrada_produtos import verificar_produtos_do_banco

@st.cache_data
def produtos_cache():
    return verificar_produtos_do_banco()

@st.dialog("Alterar Produto")
def editar_produtos_do_estoque():
    if "produto_a_editar" not in st.session_state:
        st.session_state["produto_a_editar"] = None

    produtos_disponiveis = produtos_cache()
    produto_a_ser_editado = st.selectbox("Selecione o produto", produtos_disponiveis)

    if st.button("Editar"):
        while True:
            try:
                st.session_state["produto_a_editar"] = produto_a_ser_editado
                produtos_cache.clear()
                print("Passou por aqui, quebrou o While")
                break
            except IndexError:
                print("Passou por aqui, deu erro de indexação")
                continue


    if st.session_state["produto_a_editar"]:
        dados = verificar_info_produtos(st.session_state["produto_a_editar"])
        info = dados[0]  # Pega a primeira tupla

        with st.form("form_edicao"):
            nome = st.text_input("Nome do Produto", value=info[2])
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
                produtos_cache.clear()

                st.rerun()