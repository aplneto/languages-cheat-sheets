'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Antônio Paulino de Lima Neto (apln2); Gustavo Pimentel Fernandes de Melo (gpfm)
Email:	{apln2, gpfm}[at]cin[dot]ufpe[dot]br
Data:	2017-10-03

Configuração da Janela de Cadastro
'''
from tkinter import *
from tkinter import messagebox
from Rotinas import CriptografarDicionario, SalvarAcao
from Usuarios import DecifrarUsuarios

class Cadastro():
    'Configurações dos objetos na janela de cadastro'
    def __init__(self):
        self.JanelaCadastro = Toplevel()
        self.JanelaCadastro.title("Cadastro")
        self.JanelaCadastro.resizable(FALSE, FALSE)
        self.JanelaCadastro.grab_set()
        self.JanelaCadastro.focus_force()
        w, h = self.JanelaCadastro.winfo_screenwidth(), self.JanelaCadastro.winfo_screenheight()
        self.JanelaCadastro.geometry("243x212")
        self.JanelaCadastro.geometry("+%d+%d" % ((w/2)-121, (h/2)-106))

        self.JanelaCadastro.bind('<F1>', self.JanelaAjuda)

        # Inicialização dos Widgets na Janela de Cadastro
        LabelTitulo = Label(self.JanelaCadastro, text="Python Vehicle Keeper")
        LabelUsuario = Label(self.JanelaCadastro, text="Nome de Usuário: ")
        LabelSenha = Label(self.JanelaCadastro, text="Senha: ")
        LabelConfirmacao = Label(self.JanelaCadastro, text="Confirmação de Senha:")

        self.EntryUsuario = Entry(self.JanelaCadastro, width=15)
        self.EntrySenha = Entry(self.JanelaCadastro, width=15, show='*')
        self.EntryConfirmacao = Entry(self.JanelaCadastro, width=15, show='*')

        BotaoCadastro = Button(self.JanelaCadastro, text="Cadastrar", command=self.Confirmar, width=10)
        BotaoCancelar = Button(self.JanelaCadastro, text="Cancelar", command=self.JanelaCadastro.destroy, width=10)

        LabelCopyright = Label(self.JanelaCadastro, text="2017 apln2-gpfm")
        LabelAjuda = Label(self.JanelaCadastro, text="Presione F1 para acessar a janela de ajuda.")

        # Posicionamento dos Widgets
        LabelTitulo.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky=W+E)
        LabelUsuario.grid(row=1, column=0, padx=5, pady=5)
        LabelSenha.grid(row=2, column=0, padx=5, pady=5)
        LabelConfirmacao.grid(row=3, column=0, padx=5, pady=5)
        self.EntryUsuario.grid(row=1, column=1, padx=5, pady=5)
        self.EntrySenha.grid(row=2, column=1, padx=5, pady=5)
        self.EntryConfirmacao.grid(row=3, column=1, padx=5, pady=5)
        BotaoCadastro.grid(row=4, column=0, padx=5, pady=5)
        BotaoCancelar.grid(row=4, column=1, padx=5, pady=5)
        LabelCopyright.grid(row=5, column=0, columnspan=2, padx=5, sticky=W+E)
        LabelAjuda.grid(row=6, column=0, columnspan=2, padx=5, sticky=W + E)

        # Associação de Teclas
        self.JanelaCadastro.bind('<Return>', BotaoCadastro["command"])
        self.JanelaCadastro.bind('<Escape>', BotaoCancelar["command"])

        self.EntryUsuario.focus_force()

    def Confirmar(self):
        DicionarioUsuario = DecifrarUsuarios()
        Usuario = self.EntryUsuario.get()
        Senha = self.EntrySenha.get()
        Confirmacao = self.EntryConfirmacao.get()
        if Usuario != '':  # Se o nome de usuário for diferente de vazio.
            if not (Usuario in DicionarioUsuario):  # Se o nome de usuário não existir no dicionário de usuários
                if not(' ' in Usuario):  # Se o nome de usuário não contiver espaços
                    if len(Senha) >= 4:  # Se a senha tiver pelo menos 4 caracteres
                        if Senha == Confirmacao:  # Se a senha e a confirmação forem iguais
                            DicionarioUsuario[Usuario] = (Senha, '3')
                            CriptografarDicionario(DicionarioUsuario, 'u')
                            SalvarAcao(Usuario, 'c')
                            self.JanelaCadastro.destroy()
                            messagebox.showinfo("Cadastro Efetuado", "Cadastro efetuado com sucesso.\n"
                                                                     "Faça login como "+Usuario+" para continuar.")
                        else:  # Se a senha e a confirmação não forem iguais
                            messagebox.showerror("Erro de Confirmação", "A senha e a confirmação devem ser iguais.")
                    else:  # Se a senha tiver menos de quatro caracteres
                        messagebox.showerror("Erro de Senha", "A senha deve conter pelo menos quatro caracteres")
                else:  # Se o nome de usuário contiver espaços
                    messagebox.showerror("Erro de Usuário", "Nome de usuário não pode conter espaços.")
            else:  # Se o nome de usuário já existir no dicionário de usuários
                messagebox.showerror("Erro de Usuário","Nome de usuário já existe.\n"
                                                       "Escolha um nome de usuário diferente e tente novamente.")
        else:  # Se o nome de usuário não for diferente de vazio
            messagebox.showerror("Erro de Usuário","Nome de usuário inválido.\nNome de usuário não pode ser vazio.")

    def JanelaAjuda(self, tecla):
        messagebox.showinfo("Ajuda", "O nome de usuário deve ser único.\n"
                                     "O nome de usuário não pode conter espaços.\n"
                                     "A senha deve conter pelo menos quatro caracteres.\n"
                                     "A senha e a confirmação de senha devem ser iguais.")