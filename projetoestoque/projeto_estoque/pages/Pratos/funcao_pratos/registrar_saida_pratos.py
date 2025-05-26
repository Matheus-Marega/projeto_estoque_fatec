import streamlit as st
from database.queries import buscar_ID_prato, buscar_ingredientes_pratos,buscar_ingredientes_por_ID,atualizar_qtd_tabela_produtos,verificar_pratos_no_banco

def registrar_saida_pratos(prato):
    id_prato = buscar_ID_prato(prato)
    lista_ingredientes_e_qtd = buscar_ingredientes_pratos(id_prato[0])
    for ingrediente in lista_ingredientes_e_qtd:
        nome_ingrediente = buscar_ingredientes_por_ID(ingrediente[0])
        print(f" ID: {ingrediente[0]}, Ingrediente: {nome_ingrediente}, Quantidade Utilizada: {ingrediente[1]}")	
        atualizar_qtd_tabela_produtos(ingrediente[0],ingrediente[1])
    st.success("Saída de pratos registrada com sucesso!")


def formatar_nome_prato():
    lista = []
    for pratos1 in verificar_pratos_no_banco():   
        # lista.append(produtos)
        for itens in pratos1:
            lista.append(itens)
    return lista
