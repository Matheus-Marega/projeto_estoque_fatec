from dotenv import load_dotenv
import os
import psycopg2
from contextlib import contextmanager

@contextmanager
def instance_cursor():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexao com o banco de dados fechada.")


load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")


def testar_conexao():
    try:
        with instance_cursor() as cursor:
            cursor.execute("SELECT 1;")
            resultado = cursor.fetchone()
            if resultado and resultado[0] == 1:
                print("Conexão ao banco de dados bem-sucedida!")
            else:
                print("Conexão falhou.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")


testar_conexao()