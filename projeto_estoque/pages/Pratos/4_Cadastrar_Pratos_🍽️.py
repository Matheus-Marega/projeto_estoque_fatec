import streamlit as st
from pages.Produtos.Funcao_produtos.registrar_entrada_produtos import verificar_produtos_do_banco as buscar_produtos_db
from pages.Pratos.funcao_pratos.cadastro_qtd_ingredientes import cadastrar_pratos

# ⚙️ Função cacheada
@st.cache_data
def produtos_cache():
    return buscar_produtos_db()

# ⏳ Inicialização do estado
if "produtos_do_banco" not in st.session_state:
    st.session_state["produtos_do_banco"] = produtos_cache()
if "ingredientes" not in st.session_state:
    st.session_state["ingredientes"] = []
if "erro_nome" not in st.session_state:
    st.session_state["erro_nome"] = False
if "erro_ingredientes" not in st.session_state:
    st.session_state["erro_ingredientes"] = False
if "etapa_cadastro" not in st.session_state:
    st.session_state["etapa_cadastro"] = False

# 🧂 Dados dos produtos
produtos = st.session_state["produtos_do_banco"]

# 🖼️ Interface
st.title("Cadastrar Pratos 🍽️")

st.text_input("Nome do prato", key="nome_prato")
st.multiselect("Ingredientes", produtos, key="ingredientes")
st.selectbox("Categoria", ["Entrada", "Prato Principal", "Sobremesa"], key="categoria_prato")

#Atualizar dados do banco manualmente
if st.button("🔄 Atualizar Produtos do Banco"):
    st.cache_data.clear()
    st.session_state["produtos_do_banco"] = produtos_cache()
    st.success("Produtos atualizados com sucesso!")

# ⚠️ Validação
if st.session_state["erro_nome"] or st.session_state["erro_ingredientes"]:
    st.error("Preencha os campos obrigatórios.")


def iniciar_cadastro():
    st.session_state["etapa_cadastro"] = True

st.button("Próximo", on_click=iniciar_cadastro)

# Exibe a próxima etapa se o usuário clicou
if st.session_state["etapa_cadastro"]:
    cadastrar_pratos()
