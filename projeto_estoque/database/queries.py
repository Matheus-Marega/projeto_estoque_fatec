import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")


def cadastrar_produto_DB(nome_produto, unidade_medida, marca_produto, quantidade):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        INSERT INTO PRODUTOS (nome_produto, unidade_medida, marca_produto, quantidade_em_estoque)
        VALUES (%s, %s, %s, %s)
        """
    cursor.execute(query, (nome_produto, unidade_medida, marca_produto, quantidade))
    connection.commit()
    print("Produtos cadastrados com sucesso.")
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")



def verificar_produtos():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT nome_produto FROM produtos
        """
    cursor.execute(query,)
    request = cursor.fetchall()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    return request


def verificar_unidade_medida_produto(nome_produto):
    print(f"Nome do produto: {nome_produto}")
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT unidade_medida FROM produtos WHERE nome_produto = %s
        """
    cursor.execute(query,(nome_produto, ))
    request = cursor.fetchone()
    if request:
         unidade = request[0]  # pega o valor dentro da tupla
    else:
         unidade = None

    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    return unidade

def verificar_marca_do_produto(nome_produto):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT marca_produto FROM produtos WHERE nome_produto = %s
        """
    cursor.execute(query,(nome_produto, ))
    request = cursor.fetchone()
    if request:
         marca = request[0]  # pega o valor dentro da tupla
    else:
         marca = None

    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    return marca

def verificar_pratos_no_banco():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT nome_prato FROM pratos
        """
    cursor.execute(query,)
    request = cursor.fetchall()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return request

def adiciona_qtd_produto(nome_produto,quantidade):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        UPDATE produtos
        SET quantidade_em_estoque = quantidade_em_estoque + %s
        WHERE nome_produto = %s;
        """
    cursor.execute(query,(quantidade,nome_produto))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return True


def cadastra_pratos_no_DB(nome_prato,categoria_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        INSERT INTO pratos (nome_prato, categoria_prato)
        VALUES (%s, %s)
        """
    cursor.execute(query,(nome_prato,categoria_prato))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")



def cadastrar_ingredientes_pratos(id_prato, ingredientes_id, quantidade_utilizada):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        INSERT INTO ingredientes_pratos (prato_id, ingrediente_id,quantidade_utilizada)
        VALUES (%s, %s, %s)
        """
    cursor.execute(query,(id_prato, ingredientes_id, quantidade_utilizada))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")



def buscar_ID_prato(nome_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT id FROM pratos WHERE nome_prato = %s
        """
    cursor.execute(query,(nome_prato,))
    request = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return request


def buscar_ID_ingredientes(nome_ingrediente):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT id FROM produtos WHERE nome_produto = %s
        """
    cursor.execute(query,(nome_ingrediente,))
    request = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return request

def buscar_ingredientes_por_ID(id_ingrediente):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT nome_produto FROM produtos WHERE id = %s
        """
    cursor.execute(query,(id_ingrediente,))
    request = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return request

def buscar_ingredientes_pratos(id_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT ingrediente_id, quantidade_utilizada FROM ingredientes_pratos WHERE prato_id = %s
        """
    cursor.execute(query,(id_prato,))
    request = cursor.fetchall()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return request

def atualizar_qtd_tabela_produtos(id_prato,quantidade_utilizada_ingredientes):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        UPDATE produtos
        SET quantidade = quantidade - %s
        WHERE id = %s
        """
    cursor.execute(query,(quantidade_utilizada_ingredientes, id_prato))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")