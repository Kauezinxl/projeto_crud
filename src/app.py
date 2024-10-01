from tkinter import *
import services

def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)

        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)

    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciamento de Usuario')

    titulo = Label(janela, text='CRUD', font=('Arial', 20))
    titulo.pack(pady=30)

    # Componentes de entrada
    # Nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    # EmaiL
    email = Label(janela, text='Email:')
    email.place(x=50, y=130)

    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=130)

    # Senha
    senha = Label(janela, text='Senha:')
    senha.place(x=50, y=160)

    # Comando show para esconder a senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=100, y=160)

    cadastrar = Button(janela, text='Cadastrar', width=10, command=on_enviar)
    cadastrar.place(x=100, y=200)

    lista = Button(janela, text='Listar Usuários', width=15)
    lista.place(x=200, y=200)

    janela.mainloop()

if __name__ == '__main__':
    main()
