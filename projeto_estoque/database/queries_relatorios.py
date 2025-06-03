import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERSERVER = os.getenv("USERSERVER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")


def verificar_produtos_perto_de_acabar():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT nome_produto,quantidade_em_estoque
        FROM produtos
        WHERE quantidade_em_estoque < 10
        ORDER BY quantidade_em_estoque ASC;
        """
    cursor.execute(query)
    request = cursor.fetchall()
    print(request)
    if(connection):
        cursor.close()
        connection.close()
    return request


