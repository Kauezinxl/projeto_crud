from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)
    pass

def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado com sucesso!')
        

        cursor = conn.cursor()

        sql = 'INSERT INTO usuário (nome, email, senha) values (%5, %5, %5)'
        values = (nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        cursor.close()






    else:
        print('Falha ao conectar com o servidor!')
