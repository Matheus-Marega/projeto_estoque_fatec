import streamlit as st
from database.queries import (
    verificar_info_utilizada_nos_pratos,
    verificar_pratos_no_banco,
    verificar_produtos,
    atualizar_nome_prato,
    atualizar_ingredientes_pratos,
    excluir_prato
)

from time import sleep

@st.cache_data
def pratos_cache():
    return [itens[0] for itens in verificar_pratos_no_banco()]

@st.dialog("Alterar Pratos Cadastrados")
def editar_pratos_cadastrados():
    if "prato_a_editar" not in st.session_state:
        st.session_state["prato_a_editar"] = None

    editar_pratos = pratos_cache()
    prato_selecionado = st.selectbox("Selecione o prato", editar_pratos)

    if st.button("Editar"):
        st.session_state["prato_a_editar"] = prato_selecionado
        pratos_cache.clear()
    

    if st.session_state["prato_a_editar"]:
        dados = verificar_info_utilizada_nos_pratos(st.session_state["prato_a_editar"])
        opcoes = ["Kilograma", "Grama", "Litro", "Mililitro", "Unidade"]

        with st.form("form_edicao"):
            nome_prato_novo = st.text_input("Nome do Prato", value=st.session_state["prato_a_editar"])
            st.divider()
            st.text("Produtos utilizados nesse prato:")

            for tupla in dados:
                produto_nome = tupla[0][0] if isinstance(tupla[0], tuple) else tupla[0]
                st.selectbox(
                    "Produto",
                    options=verificar_produtos(),
                    index=verificar_produtos().index(produto_nome),
                    key=f"produto_{tupla[0]}"
                )
                st.number_input("Quantidade", value=float(tupla[1][0]), key=f"quantidade_{tupla[0]}")
                st.selectbox(
                    "Unidade de Medida",
                    options=opcoes,
                    index=opcoes.index(tupla[2][0]),
                    key=f"unidade_{tupla[0]}"
                )
                st.divider()
            excluido = st.checkbox("Excluir este prato", value=False)
            submit = st.form_submit_button("Salvar Alterações")

            if submit:
                if excluido:
                    excluir_prato(prato_selecionado)
                    st.success("Prato excluído com sucesso!")
                    sleep(2)
                    pratos_cache.clear()
                    del st.session_state["prato_a_editar"]
                    st.rerun()
                else:
                    atualizar_nome_prato(st.session_state["prato_a_editar"], nome_prato_novo)

                    produtos_novos = []
                    qtd_atualizada = []
                    unidade_medida = []

                    for tupla in dados:
                        produtos_novos.append(st.session_state[f"produto_{tupla[0]}"])
                        qtd_atualizada.append(st.session_state[f"quantidade_{tupla[0]}"])
                        unidade_medida.append(st.session_state[f"unidade_{tupla[0]}"])

                    st.text("Produtos novos: ")
                    st.text(produtos_novos)
                    st.text("Quantidades atualizadas: ")
                    st.text(qtd_atualizada)
                    st.text("Unidades de medida: ")
                    st.text(unidade_medida)

                    atualizar_ingredientes_pratos(
                        nome_prato=st.session_state["prato_a_editar"],
                        produtos_novos=produtos_novos,
                        qtd_atualizada=qtd_atualizada,
                        unidade_medida=unidade_medida
                    )

                    st.success("Prato atualizado com sucesso!")
                    sleep(2)
                    pratos_cache.clear()
                    del st.session_state["prato_a_editar"]
                    st.rerun()
