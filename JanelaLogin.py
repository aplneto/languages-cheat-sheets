'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Antônio Paulino de Lima Neto (apln2); Gustavo Pimentel Fernandes de Melo (gpfm)
Email:	{apln2, gpfm}[at]cin[dot]ufpe[dot]br
Data:	2017-10-03

Copyright(c) 2017 Antônio Paulino de Lima Neto

Configurações da Janela de Login e da Função de Login
'''
from tkinter import *
from tkinter import messagebox
from Rotinas import SalvarAcao
from Usuarios import DecifrarUsuarios

class Login():
    'Objetos da Classe da Janela de Login'
    def __init__(self):
        # Configurações iniciais da janela de Login
        self.JaneladeLogin = Toplevel()
        w, h = self.JaneladeLogin.winfo_screenwidth(), self.JaneladeLogin.winfo_screenheight()
        self.JaneladeLogin.title("Login")
        self.JaneladeLogin.grab_set()
        self.JaneladeLogin.resizable(FALSE, FALSE)
        self.JaneladeLogin.geometry("194x185")
        self.JaneladeLogin.geometry("+%d+%d" % ((w/2)-97,(h/2)-93))  # Centralização da Janela de Login na Tela

        # Inicialização dos Widgets na Janela
        LabelTitulo = Label (self.JaneladeLogin, text="Python Vehicle Keeper")
        LabelUsuario = Label(self.JaneladeLogin, text="Usuario: ")
        LabelSenha = Label(self.JaneladeLogin, text="Senha: ")
        self.EntryUsuario = Entry(self.JaneladeLogin, width=15)
        self.EntrySenha = Entry(self.JaneladeLogin, show='*', width=15)
        BotaoLogin = Button(self.JaneladeLogin, text="Login", command=self.VerificarLogin, width=10)
        BotaoCancelar = Button(self.JaneladeLogin, text="Cancelar", command=self.JaneladeLogin.destroy, width=10)
        LabelCopyright = Label (self.JaneladeLogin, text="2017 apln2-gpfm")

        # Posicionamento dos Widgets da Janela de Login
        LabelTitulo.grid(row=0, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
        LabelUsuario.grid(row=1, column=0, padx=5, pady=5)
        LabelSenha.grid(row=2, column=0, padx=5, pady=5)
        self.EntryUsuario.grid(row=1, column=1, padx=5, pady=5)
        self.EntrySenha.grid(row=2, column=1, padx=5, pady=5)
        BotaoLogin.grid(row=4, column=0, padx=5, pady=5, sticky=W+E)
        BotaoCancelar.grid(row=4, column=1, padx=5, pady=5, sticky=W+E)
        LabelCopyright.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=W+E)

        # Associação de Teclas
        self.JaneladeLogin.bind('<Return>', BotaoLogin["command"])
        self.JaneladeLogin.bind('<Escape>', BotaoCancelar["command"])

        self.EntryUsuario.focus_force()

    def VerificarLogin(self):
        """
        Funçao definida para o pressionamento do botão de login
        """
        DicionarioUsuarios = DecifrarUsuarios()
        Usuario = self.EntryUsuario.get()
        Senha = self.EntrySenha.get()
        if Usuario in DicionarioUsuarios:  # Se o nome de usuário estiver no dicionário de usuários
            if DicionarioUsuarios[Usuario][0] == Senha:  # Se a senha estiver correta a senha do usuário
                settings = open(".settings.txt", 'w')
                settings.write(Usuario)
                settings.close()
                SalvarAcao(Usuario, 'l')
                self.JaneladeLogin.destroy()
            else:  # Se a senha não estiver correta
                messagebox.showerror("Erro de Senha","Senha incorreta.\nPor favor, verifique sua "
                                                     "senha e tente novamente.")
                self.EntrySenha.delete(0, END)  # Apaga os caracteres no campo de senha
        else:  # Se o nome de usuário não estiver no dicionário de usuários
            messagebox.showerror("Erro de Usuário", "Nome de usuário informado não existe.\n"
                                                    "Por favor, verifique o nome de usuário e tente novamente.")