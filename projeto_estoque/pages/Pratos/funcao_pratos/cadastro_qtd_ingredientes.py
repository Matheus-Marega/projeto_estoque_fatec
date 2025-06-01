import streamlit as st
from database.models import criar_tabela_cadastro_pratos, criar_tabela_ingredientes_pratos
from database.queries import cadastra_pratos_no_DB, cadastrar_ingredientes_pratos, buscar_ID_prato, buscar_ID_ingredientes, verificar_unidade_medida_produto, verificar_marca_do_produto
from pages.funcao_uteis.validacoes import validar_unidade_de_medida_nos_campos_de_texto




def cadastrar_pratos():
    if "categoria_prato" not in st.session_state:
        st.session_state['categoria_prato'] = "Entrada"
    if "nome_prato" not in st.session_state:
        st.session_state['nome_prato'] = ""
    if "counter_cadastro_pratos" not in st.session_state:
        st.session_state['counter_cadastro_pratos'] = 0


    try:
        criar_tabela_cadastro_pratos()
        criar_tabela_ingredientes_pratos()
    except Exception as e:
        st.error(f"Erro ao criar tabelas: {e}")

    lista_ingredientes = st.session_state['ingredientes']
    


    st.subheader(f"Preencha os detalhes do prato {st.session_state['nome_prato']}")

    for ingredientes in st.session_state["ingredientes"]:

        st.write(f"Ingrediente: {ingredientes}")
        if verificar_unidade_medida_produto(ingredientes) in ["Kilogramas","Gramas"]:
            st.selectbox(placeholder="Selecione a unidade de medida", options=["Kilogramas", "Gramas"])
        elif verificar_unidade_medida_produto(ingredientes) in ["Litros", "Mililitros"]:
            st.selectbox(placeholder="Selecione a unidade de medida", options=["Litros", "Mililitros"])
        elif verificar_unidade_medida_produto(ingredientes) == "Unidades":
            st.selectbox(placeholder="Selecione a unidade de medida", options=["Unidades"])
        else:
            st.text("Unidade de medida não encontrada")
        st.number_input("Digite a quantidade do ingrediente", min_value=0, key=f"quantidade_{ingredientes}")
        st.divider()


    if st.button("Cadastrar Prato"):
        cadastra_pratos_no_DB(
            st.session_state['nome_prato'],
            st.session_state['categoria_prato']
        )
        for ingrediente in lista_ingredientes:
            cadastrar_ingredientes_pratos(
                buscar_ID_prato(st.session_state['nome_prato'])[0],
                buscar_ID_ingredientes(ingrediente)[0],
                st.session_state[f"quantidade_{ingrediente}"]
            )
        st.success("Prato cadastrado com sucesso!")
        # Agora sim, limpe o estado se quiser reiniciar o fluxo
        del st.session_state['etapa_cadastro']
        del st.session_state['nome_prato']
        del st.session_state['ingredientes']
        del st.session_state['categoria_prato']
        st.rerun()
