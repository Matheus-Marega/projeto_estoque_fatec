import streamlit as st
import random
from datetime import datetime

# Simula uma função que acessa o banco
def buscar_produtos_db():
    print("🔄 Consultando banco de dados...")
    return [f"Produto {i}" for i in range(1, random.randint(3, 6))]

# Wrapper com cache
@st.cache_data
def produtos_cache():
    return buscar_produtos_db()

# Inicializa os dados no session_state
if "produtos_do_banco" not in st.session_state:
    st.session_state["produtos_do_banco"] = produtos_cache()
if "ingredientes" not in st.session_state:
    st.session_state["ingredientes"] = []
if "botao_clicado" not in st.session_state:
    st.session_state["botao_clicado"] = False

st.title("Cadastro de Prato")

# Campo de seleção com base nos dados armazenados
ingredientes = st.multiselect("Escolha os ingredientes:", st.session_state["produtos_do_banco"], key="ingredientes")

# Mostra seleção atual
st.write("Ingredientes selecionados:", ingredientes)

# Botão para atualizar produtos (limpa cache e refaz consulta)
if st.button("🔁 Atualizar Produtos do Banco"):
    st.cache_data.clear()
    st.session_state["produtos_do_banco"] = produtos_cache()
    st.success(f"Produtos atualizados às {datetime.now().strftime('%H:%M:%S')}")

# Botão de cadastro (simula fluxo com estado)
def marcar_botao():
    st.session_state["botao_clicado"] = True

st.button("✅ Cadastrar Prato", on_click=marcar_botao)

# Executa o fluxo apenas se o botão for clicado
if st.session_state["botao_clicado"]:
    st.success(f"Prato cadastrado com: {st.session_state['ingredientes']}")
    st.session_state["botao_clicado"] = False
