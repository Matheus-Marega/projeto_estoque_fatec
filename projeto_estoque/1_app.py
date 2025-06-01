import streamlit as st


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login_2():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()


def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()


def configuracao_user():
    print("Hello, user!")

def configuracoes():
    print("Hello, user!")




login_page = st.Page(login_2, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
config_user = st.Page(configuracao_user,title="Configurações de Usuário", icon=":material/settings:")
config = st.Page(configuracoes, title="Configurações", icon=":material/settings:")  
dev_config_pg = st.Page("pages/7_Teste_DEV.py", title="Configurações de Desenvolvimento", icon=":material/settings:")


cadastrar_pratos = st.Page(
    "pages/Pratos/4_Cadastrar_Pratos_🍽️.py", title="Cadastrar Pratos")
registrar_saida_pratos = st.Page(
    "pages/Pratos/5_Registrar_saida_de_pratos_🍝.py", title="Registrar Saída de Pratos")
gerenciar_pratos = st.Page("pages/Pratos/9_Gerenciar_Pratos.py", title="Gerenciar Pratos")



cadastrar_produtos = st.Page(
    "pages/Produtos/2_Cadastrar_Produtos_🛍️.py", title="Cadastrar Produtos")
registrar_entrada_produtos = st.Page(
    "pages/Produtos/3_Registrar_Entrada_produtos.py", title="Registrar Entrada de Produtos")
gerenciar_produtos = st.Page("pages/Produtos/8_Gerenciar_Produtos.py", title="Gerenciar Produtos")



if st.session_state.logged_in:
    logo = st.logo("images/EscritaLogoTechnova2.png", size="large")
    pg = st.navigation(
        {
            "Produtos": [cadastrar_produtos, registrar_entrada_produtos, gerenciar_produtos],
            "Pratos": [cadastrar_pratos, registrar_saida_pratos, gerenciar_pratos],
            "Account": [logout_page, config_user,config,dev_config_pg]
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
