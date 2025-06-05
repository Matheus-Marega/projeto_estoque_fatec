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
    lista_temporaria = []
    query = f"""
        SELECT nome_produto FROM produtos
        """
    cursor.execute(query,)
    request = cursor.fetchall()
    if(connection):
        cursor.close()
        connection.close()
    return [item[0] for item in request]

def verificar_quantidade_do_produto_em_estoque(nome_produto):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT quantidade_em_estoque FROM produtos WHERE nome_produto = %s
        """
    cursor.execute(query,(nome_produto,))
    request = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    return request


def verificar_se_produto_ja_existe_no_DB(nome_produto):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT nome_produto FROM produtos WHERE nome_produto = %s
        """
    cursor.execute(query,(nome_produto,))
    request = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    if request == None:
        return False
    else:
        return True

def verificar_se_prato_ja_existe_no_DB(nome_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT nome_prato FROM pratos WHERE nome_prato = %s
        """
    cursor.execute(query,(nome_prato,))
    request = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    if request == None:
        return False
    else:
        return True


def verificar_unidade_medida_produto(nome_produto):
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
        print("Unidade retornada: ",unidade)
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

def verificar_info_produtos(nome_produto):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT unidade_medida, marca_produto, nome_produto, quantidade_em_estoque FROM produtos WHERE nome_produto = %s
        """
    cursor.execute(query,(nome_produto, ))
    request = cursor.fetchall()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
        print(request)
    return request

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

def validacao_quantidade_de_produtos_em_estoque_para_registrar_saida_de_pratos(nome_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT id 
        FROM pratos 
        WHERE nome_prato = %s
        """
    cursor.execute(query,(nome_prato,))
    id_prato = cursor.fetchone()

    query = f"""
        SELECT ingrediente_id
        FROM ingredientes_pratos 
        WHERE prato_id = %s
        """
    cursor.execute(query,(id_prato,))
    id_ingredientes = cursor.fetchone()

    query = f"""
        SELECT quantidade_em_estoque
        FROM produtos 
        WHERE id = %s
        """
    cursor.execute(query,(id_ingredientes,))
    quantidade_do_produto_em_estoque = cursor.fetchone()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return quantidade_do_produto_em_estoque



def verificar_ingredientes_cadastrados_no_prato(nome_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT id 
        FROM pratos 
        WHERE nome_prato = %s
        """
    cursor.execute(query,(nome_prato,))
    id_prato = cursor.fetchone()

    query = f"""
        SELECT ingrediente_id
        FROM ingredientes_pratos 
        WHERE prato_id = %s
        """
    cursor.execute(query,(id_prato,))
    id_ingredientes = cursor.fetchall()
    print(f"ID dos ingredientes: {id_ingredientes}")

    lista_temporaria = []
    for id in id_ingredientes:
        query = f"""
            SELECT nome_produto
            FROM produtos 
            WHERE id = %s
            """
        cursor.execute(query,(id))
        nome_do_produto_em_estoque = cursor.fetchone()
        lista_temporaria.append(nome_do_produto_em_estoque)

    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")
    return lista_temporaria

def verificar_info_utilizada_nos_pratos(nome_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT id 
        FROM pratos 
        WHERE nome_prato = %s
        """
    cursor.execute(query,(nome_prato,))
    id_prato = cursor.fetchone()

    query = f"""
        SELECT ingrediente_id
        FROM ingredientes_pratos 
        WHERE prato_id = %s
        """
    cursor.execute(query,(id_prato,))
    id_ingredientes = cursor.fetchall()
    print(f"ID dos ingredientes: {id_ingredientes}")


    lista_temporaria = []
    for id in id_ingredientes:
        query = f"""
            SELECT nome_produto
            FROM produtos 
            WHERE id = %s
            """
        cursor.execute(query,(id))
        nome_do_produto_em_estoque = cursor.fetchone()

        query = f"""
            SELECT quantidade_utilizada
            FROM ingredientes_pratos
            WHERE prato_id = %s and ingrediente_id = %s
        """
        cursor.execute(query,(id_prato,id))
        quantidade_utilizada = cursor.fetchone()

        query = f"""
            SELECT unidade_medida_utilizada_no_prato
            FROM ingredientes_pratos
            WHERE prato_id = %s and ingrediente_id = %s
        """
        cursor.execute(query,(id_prato,id))
        unidade_medida_utilizada_no_prato = cursor.fetchone()
        lista_temporaria.append((nome_do_produto_em_estoque, quantidade_utilizada, unidade_medida_utilizada_no_prato))

    if(connection):
        cursor.close()
        connection.close()
    return lista_temporaria


def verificar_info_cadastradas_nos_pratos(nome_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        SELECT id 
        FROM pratos 
        WHERE nome_prato = %s
        """
    cursor.execute(query,(nome_prato,))
    id_prato = cursor.fetchone()

    query = f"""
        SELECT ingrediente_id
        FROM ingredientes_pratos 
        WHERE prato_id = %s
        """
    cursor.execute(query,(id_prato,))
    id_ingredientes = cursor.fetchall()
    print(f"ID dos ingredientes: {id_ingredientes}")

    lista_temporaria = []
    for id in id_ingredientes:
        query = f"""
            SELECT nome_produto
            FROM produtos 
            WHERE id = %s
            """
        cursor.execute(query,(id))
        nome_do_produto_em_estoque = cursor.fetchone()

        query = f"""
            SELECT quantidade_utilizada
            FROM ingredientes_pratos
            WHERE prato_id = %s and ingrediente_id = %s
        """
        cursor.execute(query,(id_prato,id))
        quantidade_utilizada = cursor.fetchone()

        query = f"""
            SELECT unidade_medida_utilizada_no_prato
            FROM ingredientes_pratos
            WHERE prato_id = %s and ingrediente_id = %s
        """
        cursor.execute(query,(id_prato,id))
        unidade_medida_utilizada_no_prato = cursor.fetchone()
        lista_temporaria.append((nome_do_produto_em_estoque, quantidade_utilizada, unidade_medida_utilizada_no_prato))

    if(connection):
        cursor.close()
        connection.close()
    return lista_temporaria

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

def cadastrar_usuarios_no_DB(nome, user, senha):
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()

    query= f'''
        INSERT INTO REGISTROS VALUES
        {nome, user, senha}
        ''' 
    cursor.execute(query)
    connection.commit()
    if connection:
        cursor.close()
        connection.close()
        print('Conexão com PostgreSQL encerrada')



def cadastrar_ingredientes_pratos(id_prato, ingredientes_id, quantidade_utilizada,unidade_medida_utilizada_no_prato):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        INSERT INTO ingredientes_pratos (prato_id, ingrediente_id,quantidade_utilizada,unidade_medida_utilizada_no_prato)
        VALUES (%s, %s, %s, %s)
        """
    cursor.execute(query,(id_prato, ingredientes_id, quantidade_utilizada,unidade_medida_utilizada_no_prato))
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

def consultar_usuario_no_DB(user):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query= '''
            SELECT nome, usuario, senha 
            FROM REGISTROS
            WHERE usuario = %s   
            '''
    cursor.execute(query, (user, ))
    request = cursor.fetchall()
    return request


def consultar_todos_usuarios():
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query= '''
            SELECT * 
            FROM REGISTROS   
            '''
    cursor.execute(query, )
    request = cursor.fetchall()
    return request


def atualizar_qtd_tabela_produtos(id_prato,quantidade_utilizada_ingredientes):
    connection = psycopg2.connect(database=DATABASE,host=HOST,user=USERSERVER,password=PASSWORD,port=PORT)
    cursor = connection.cursor()
    query = f"""
        UPDATE produtos
        SET quantidade_em_estoque = quantidade_em_estoque - %s
        WHERE id = %s
        """
    cursor.execute(query,(quantidade_utilizada_ingredientes, id_prato))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")

def atualizar_produto(nome_produto,marca_produto, unidade_medida, quantidade_em_estoque):
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()
    query = f"""
        UPDATE produtos
        SET unidade_medida = %s, marca_produto = %s, quantidade_em_estoque = %s, nome_produto = %s
        WHERE nome_produto = %s
        """
    cursor.execute(query, (unidade_medida, marca_produto, quantidade_em_estoque, nome_produto, nome_produto))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")


def atualizar_nome_prato(nome_prato_antigo, nome_prato_novo):
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()
    query = f"""
        UPDATE pratos
        SET nome_prato = %s
        WHERE nome_prato = %s
        """
    cursor.execute(query, (nome_prato_novo, nome_prato_antigo))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")

# def atualizar_ingredientes_pratos(nome_prato, produtos_novos,qtd_atualizada:list,unidade_medida:list):
#     connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
#     cursor = connection.cursor()
#     query = f"""
#         SELECT id 
#         FROM pratos 
#         WHERE nome_prato = %s
#         """
#     cursor.execute(query,(nome_prato,))
#     id_prato= cursor.fetchone()

#     query = f"""
#         SELECT ingrediente_id
#         FROM ingredientes_pratos 
#         WHERE prato_id = %s
#         """
#     cursor.execute(query,(id_prato,))
#     id_ingredientes_antigos = cursor.fetchall()

#     print("----------------------------------------------")
#     print(produtos_novos)
#     print("----------------------------------------------")
#     lista_temp = []
#     for produtos in produtos_novos:
#         print(produtos)
#         query = f"""
#             SELECT id
#             FROM PRODUTOS
#             WHERE nome_produto = %s
#             """
#         cursor.execute(query, (produtos,))
#         id_ingredientes_novos = cursor.fetchall()
#         lista_temp.append(id_ingredientes_novos)

#     query = f"""
#         UPDATE ingredientes_pratos
#         SET ingrediente_id = %s,
#         quantidade_utilizada = %s, 
#         unidade_medida_utilizada_no_prato = %s
#         WHERE prato_id = %s AND ingrediente_id = %s
#         """
#     for (id_novo, id_antigo, qtd, unidade) in zip(lista_temp, id_ingredientes_antigos, qtd_atualizada, unidade_medida):
#         id_novo = id_novo[0] if isinstance(id_novo, tuple) else id_novo
#         id_antigo = id_antigo[0] if isinstance(id_antigo, tuple) else id_antigo
#         qtd = qtd[0] if isinstance(qtd, tuple) else qtd
#         unidade = unidade[0] if isinstance(unidade, tuple) else unidade

#         cursor.execute(query, (id_novo, qtd, unidade, id_prato[0], id_antigo))


def atualizar_ingredientes_pratos(nome_prato, produtos_novos, qtd_atualizada: list, unidade_medida: list):
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id FROM pratos WHERE nome_prato = %s
    """, (nome_prato,))
    id_prato = cursor.fetchone()[0]


    cursor.execute("""
        SELECT ingrediente_id FROM ingredientes_pratos WHERE prato_id = %s
    """, (id_prato,))
    id_ingredientes_antigos = [item[0] for item in cursor.fetchall()]

    for produto, qtd, unidade, id_antigo in zip(produtos_novos, qtd_atualizada, unidade_medida, id_ingredientes_antigos):
        cursor.execute("""
            SELECT id FROM produtos WHERE nome_produto = %s
        """, (produto,))
        id_novo = cursor.fetchone()[0]

        cursor.execute("""
            UPDATE ingredientes_pratos
            SET ingrediente_id = %s,
                quantidade_utilizada = %s,
                unidade_medida_utilizada_no_prato = %s
            WHERE prato_id = %s AND ingrediente_id = %s
        """, (id_novo, qtd, unidade, id_prato, id_antigo))

    connection.commit()
    cursor.close()
    connection.close()
    print("Conexão com o banco de dados encerrada.")


def excluir_prato(nome_prato):
    connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = connection.cursor()

    query = f"""
            SELECT id FROM pratos 
            WHERE nome_prato = %s
            """
    cursor.execute(query, (nome_prato,))
    resultado = cursor.fetchone()

    if resultado is None:
        print(f"Prato '{nome_prato}' não encontrado.")
        cursor.close()
        connection.close()
        return

    id_prato = resultado[0]
    query = f"""
            DELETE FROM ingredientes_pratos 
            WHERE prato_id = %s
            """
    cursor.execute(query, (id_prato,))

    query = f"""
            DELETE FROM pratos 
            WHERE id = %s
            """
    cursor.execute(query, (id_prato,))
    connection.commit()
    if(connection):
        cursor.close()
        connection.close()
        print("Conexao com o banco de dados fechada.")





