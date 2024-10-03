from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)


def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado com sucesso!')
        

        cursor = conn.cursor()

        sql = "INSERT INTO usuario (nome, email, senha) values (%s, %s, %s)"       
        values = (nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        cursor.close()
    else:
        print('Falha ao conectar com o servidor!')

def lista_usuario():
    if conn.is_connected():
         print('Banco de dados conectado com sucesso!')
        
         cursor = conn.cursor()

         cursor.execute('Select id, nome, email from usuario;')

         usuarios = cursor.fetchall()
         cursor.close()
         conn.close()
         return usuarios
        
    else:
         print('Falha ao conectar com o banco de dados!')

def remover_usuario(email):
    if conn.is_connected():
        print('Banco conectado com sucesso!')

        cursor = conn.cursor()

        sql_select = 'select id, nome, email from usuario where email=%s;'
        cursor.execute(sql_select, (email,))

        usuarios = cursor.fetchone()
        if usuarios:
            print('Usuário encontrado!')
            sql_delete = 'delete from usuario where email=%s'
            cursor.execute(sql_delete, (email,))
            print('Usuário deletado com sucesso!')
            conn.commit()
            cursor.close()
            conn.close()

        else:
            print('Usuário não encontrado!')

            
