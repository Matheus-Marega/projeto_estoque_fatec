import streamlit as st
import pandas as pd
from database.queries_relatorios import verificar_produtos_perto_de_acabar


def dataframe_visao_geral():
    df = pd.DataFrame(verificar_produtos_perto_de_acabar(), columns=["Nome do Produto", "Quantidade em Estoque"])
    #df2 = st.dataframe(df, use_container_width=True)
    return df

def relatorio_visao_geral():
    df = dataframe_visao_geral()
    grafico = st.bar_chart(df.set_index("Nome do Produto")["Quantidade em Estoque"],use_container_width=True)
    return grafico
    
if st.button("Verificar Produtos Perto de Acabar"):
    st.subheader("Lista de produtos que estão perto de acabar:")
    col1, col2 = st.columns(2,gap="medium",vertical_alignment="top")
    with col2:
        relatorio_visao_geral()
    with col1:
        st.dataframe(dataframe_visao_geral(), use_container_width=True)
