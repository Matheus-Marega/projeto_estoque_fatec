# import psycopg2

# def testar_conexao():
#     try:
#         connection = psycopg2.connect(
#             database="railway",
#             host="postgres.railway.internal",
#             user="postgres",
#             password="MhRHzMMgcFyvznPGnPIHhyBpCLpwpJWw",
#             port="5432"
#         )
#         cursor = connection.cursor()
#         cursor.execute("SELECT 1;")
#         resultado = cursor.fetchone()
#         print("Conexão bem-sucedida!" if resultado[0] == 1 else "Falha na conexão.")
#     except Exception as e:
#         print(f"Erro ao conectar: {e}")
#     finally:
#         if 'connection' in locals() and connection:
#             cursor.close()
#             connection.close()

# testar_conexao()
