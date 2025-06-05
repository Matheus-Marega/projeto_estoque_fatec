import streamlit as st
from database.models import criar_tabela_cadastro_pratos, criar_tabela_ingredientes_pratos
from database.queries import cadastra_pratos_no_DB, cadastrar_ingredientes_pratos,verificar_se_prato_ja_existe_no_DB, buscar_ID_prato, buscar_ID_ingredientes, verificar_unidade_medida_produto, verificar_marca_do_produto
from pages.funcao_uteis.validacoes import validar_unidade_de_medida_nos_campos_de_texto
from time import sleep




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
        print(f"Ingrediente: {ingredientes}")
        st.write(f"Ingrediente: {ingredientes}")
        if verificar_unidade_medida_produto(ingredientes) in ["Kilograma","Grama"]:
            st.selectbox(label="Selecione a Unidade de medida que sera utilizada no prato", placeholder="Selecione a unidade de medida", options=["Kilograma", "Grama"],key=f"unidade_media_{ingredientes}")
            st.number_input(f"Digite a quantidade do ingrediente utilizada", min_value=0.00, key=f"quantidade_{ingredientes}")
        elif verificar_unidade_medida_produto(ingredientes) in ["Litro", "Mililitro"]:
            st.selectbox(label="Selecione a Unidade de medida que sera utilizada no prato", placeholder="Selecione a unidade de medida", options=["Litro", "Mililitro"],key=f"unidade_media_{ingredientes}")
            st.number_input(f"Digite a quantidade do ingrediente utilizada", min_value=0.00, key=f"quantidade_{ingredientes}")
        elif verificar_unidade_medida_produto(ingredientes) == "Unidade":
            st.selectbox(label="Selecione a Unidade de medida que sera utilizada no prato", placeholder="Selecione a unidade de medida", options=["Unidade"],key=f"unidade_media_{ingredientes}")
            st.number_input(f"Digite a quantidade do ingrediente utilizada", min_value=0, key=f"quantidade_{ingredientes}")
        else:
            st.text("Unidade de medida não encontrada")



        st.divider()


    if st.button("Cadastrar Prato"):
        if verificar_se_prato_ja_existe_no_DB(st.session_state['nome_prato']):
                st.error("Prato de mesmo nome já cadastrado!")
        else:
            cadastra_pratos_no_DB(
                st.session_state['nome_prato'],
                st.session_state['categoria_prato'],
            )
            for ingrediente in lista_ingredientes:
                cadastrar_ingredientes_pratos(
                    buscar_ID_prato(st.session_state['nome_prato'])[0],
                    buscar_ID_ingredientes(ingrediente)[0],
                    st.session_state[f"quantidade_{ingrediente}"],
                    st.session_state[f"unidade_media_{ingrediente}"]
                )
            
            st.success("Prato cadastrado com sucesso!")
            sleep(2)
            # Agora sim, limpe o estado se quiser reiniciar o fluxo
            del st.session_state['etapa_cadastro']
            del st.session_state['nome_prato']
            del st.session_state['ingredientes']
            del st.session_state['categoria_prato']
            st.rerun()
