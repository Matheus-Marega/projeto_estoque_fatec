import streamlit as st
from database.models import criar_tabela_cadastro_pratos, criar_tabela_ingredientes_pratos
from database.queries import cadastra_pratos_no_DB, cadastrar_ingredientes_pratos, buscar_ID_prato,buscar_ID_ingredientes,verificar_unidade_medida_produto,verificar_marca_do_produto
from pages.funcao_uteis.validacoes import validar_unidade_de_medida_nos_campos_de_texto



def cadastrar_pratos():
    if "counter" not in st.session_state:
        st.session_state['counter'] = 0
    if "cadastrar_prato" not in st.session_state:
        st.session_state["cadastrar_prato"] = False


    try:
        criar_tabela_cadastro_pratos()
        criar_tabela_ingredientes_pratos()
    except Exception as e:
        st.error(f"Erro ao criar tabelas: {e}")


    lista_ingredientes = st.session_state['ingredientes']
    counter = 0

    for ingrediente in lista_ingredientes:
        st.subheader(ingrediente)


        
        unidade_de_medida = verificar_unidade_medida_produto(ingrediente)
        st.subheader(f"*Unidade de Medida:* {unidade_de_medida}")
        st.session_state["quantidade_produto"] = validar_unidade_de_medida_nos_campos_de_texto(unidade_de_medida, counter)
        

        
        st.subheader(f"*Marca do Produto:* {verificar_marca_do_produto(ingrediente)}")
       # st.text_area("Modo de Preparo", key=f"modo_preparo{counter}")
        st.divider()
        counter += 1

    if st.button("Cadastrar Prato", key="cadastrar_prato"):
        cadastra_pratos_no_DB(nome_prato=st.session_state['nome_prato'],categoria_prato=st.session_state['categoria_prato'])
        for i, ingrediente in enumerate(lista_ingredientes):
            cadastrar_ingredientes_pratos(
                buscar_ID_prato(st.session_state['nome_prato'])[0],
                buscar_ID_ingredientes(ingrediente)[0],
            )
        st.success("Prato cadastrado com sucesso!")
        st.session_state['etapa_cadastro'] = False
        st.session_state['nome_prato'] = ""
        st.session_state['ingredientes'] = []
        st.session_state['categoria_prato'] = ""


