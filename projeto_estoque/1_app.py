import streamlit_authenticator as stauth
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login_2():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def login_form(authenticator):
    name, authentication_status, username = authenticator.login('Login')
    if authentication_status:
        authenticator.logout('Logout', 'main')
        logo = st.logo("images/EscritaLogoTechnova2.png", size="large")
        pg = st.navigation(
            {
                "Produtos": [cadastrar_produtos, registrar_entrada_produtos, gerenciar_produtos],
                "Pratos": [cadastrar_pratos, registrar_saida_pratos, gerenciar_pratos],
                "Relatórios": [relatorio_visao_geral],
                "Account": [logout_page,config,dev_config_pg],
                
            }
        )
    elif authentication_status == False:
        st.error('Usuário ou senha incorretos')
    elif authentication_status == None:
        st.warning('Insira um nome de usuário e uma senha')

    


    
        clicou_em_registrar = st.button("Registrar")
        if clicou_em_registrar:
            st.session_state['clicou_registrar'] = True
            st.rerun()


def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()



def configuracoes():
    print("Hello, user!")




login_page = st.Page(login_2, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
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



relatorio_visao_geral = st.Page(
    "pages/Relatorios/relatorio_visao_geral.py", title="Relatório de Visão Geral")

if st.session_state.logged_in:
    logo = st.logo("images/EscritaLogoTechnova2.png", size="large")
    pg = st.navigation(
        {
            "Produtos": [cadastrar_produtos, registrar_entrada_produtos, gerenciar_produtos],
            "Pratos": [cadastrar_pratos, registrar_saida_pratos, gerenciar_pratos],
            "Relatórios": [relatorio_visao_geral],
            "Account": [logout_page,config,dev_config_pg],
            
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()