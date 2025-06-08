import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")


def criar_tabela_cadastro_produtos():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()

    query = """
        CREATE TABLE if not exists PRODUTOS (
        ID SERIAL PRIMARY KEY,
        nome_produto VARCHAR(100) NOT NULL,
        unidade_medida VARCHAR(50) NOT NULL,
        quantidade FLOAT,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        )
        """
    
    cursor.execute(query)
    connection.commit()
    print("Tabela PRODUTOS criada com sucesso.")
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")


def criar_tabela_cadastro_pratos():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()

    query = """
        CREATE TABLE if not exists PRATOS (
        ID SERIAL PRIMARY KEY,
        nome_prato VARCHAR(100) NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        )
        """
    
    cursor.execute(query)
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")

def criar_tabela_ingredientes_pratos():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()

    query = """
        CREATE TABLE if not exists INGREDIENTES_PRATOS (
        ID SERIAL PRIMARY KEY,
        prato_id INT REFERENCES PRATOS(ID) on DELETE CASCADE,
        ingrediente_id INT REFERENCES PRODUTOS(ID),
        quantidade_utilizada FLOAT,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
        )
        """

    cursor.execute(query)
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")


def criar_tabela():
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()
    query= f'''
        CREATE TABLE if not exists REGISTROS (
            nome varchar(255),
            usuario varchar(255),
            senha varchar(255)
        )
        ''' 
    cursor.execute(query)
    connection.commit()
    if connection:
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")