from database.queries import verificar_produtos
import streamlit as st

def verificar_produtos_do_banco():
    lista = []
    for produtos in verificar_produtos():   
        # lista.append(produtos)
        for itens in produtos:
            lista.append(itens)
    return lista

    
