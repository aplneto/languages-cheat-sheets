'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Antônio Paulino de Lima Neto (apln2); Gustavo Pimentel Fernandes de Melo (gpfm)
Email:	{apln2, gpfm}[at]cin[dot]ufpe[dot]br
Data:	2017-10-03

Programa de Controle da Janela Principal da Interface Gráfica do Programa

Sumário
#1 Importações

'''

from JanelaLogin import Login
from JanelaCadastro import Cadastro
from Rotinas import ConfirmarLogin, CriptografarDicionario, SalvarAcao, OrdenarLog
from Elementos import *
from Usuarios import *
from tkinter import *
from tkinter import messagebox, ttk

class Keeper():
    'Classe dos objetos na Janela Principal do Programa'
    def __init__(self):
        #Configurações de Inicialização da Janela
        self.JanelaPrincipal = Tk()
        w, h = self.JanelaPrincipal.winfo_screenwidth(), self.JanelaPrincipal.winfo_screenheight()
        self.JanelaPrincipal.title("Python Vehicle Keeper")
        self.JanelaPrincipal.resizable(FALSE, FALSE)
        self.JanelaPrincipal.geometry("306x306")
        self.JanelaPrincipal.geometry("+%d+%d" % ((w/2)-153,(h/2)-153))

        self.JanelaPrincipal.bind('<FocusIn>', self.login)  # Verifica o Login sempre que o foco volta para a janela

        # Configuração do Frame Inicial
        self.FrameInicial = Frame(self.JanelaPrincipal)
        self.FrameInicial.pack(fill=Y, expand=TRUE)
        self.Foto = Label()

        # Objetos no Frame inicial
        LabelTitulo = Label(self.FrameInicial, text="Python Keeper", font="Verdana, 16")

        fileimg = ".Images\hRJou.gif"
        logo = PhotoImage(file=fileimg)
        Logotipo = Label(self.FrameInicial)
        Logotipo["image"] = logo

        BotaoLogin = Button(self.FrameInicial, text="Login", command=Login, width=10)
        BotaoCadastro = Button(self.FrameInicial, text="Cadastrar", command=Cadastro, width=10)

        LabelAuthor = Label(self.FrameInicial, text="Copyright(c) 2017 apln2")
        BotaoSair = Button(self.FrameInicial, text="Sair", command=self.JanelaPrincipal.destroy, width=10)

        #Posicionamento dos Widgets no Frame Inicial
        LabelTitulo.grid(row=0, column=0, columnspan=2, sticky=E+W)
        Logotipo.grid(row=1, column=0, columnspan=2, pady=10)
        BotaoLogin.grid(row=2, column=0, padx=5, pady=10)
        BotaoCadastro.grid(row=2, column=1, padx=5, pady=10)
        LabelAuthor.grid(row=3, column=0, columnspan=2, sticky=W+E, pady=5)
        BotaoSair.grid(row=4, column=1, sticky=S)
        BotaoSair.grid_anchor(E)

        # Associação de Teclas
        self.JanelaPrincipal.bind('<Escape>', BotaoSair["command"])

        self.JanelaPrincipal.mainloop()

    def login(self, event):
        """
        Função que confirma o verifica qual o usuário logado e garante o login
        """
        self.Usuario = ConfirmarLogin()
        if self.Usuario != '':
            self.FrameInicial.destroy()
            self.InicarPrograma()

    def logout(self):
        """
        Função que salva as alterações nos arquivos do sistema ao finalizar o programa
        """
        if messagebox.askyesno("Encerrar", "Deseja salvar as alterações e sair?"):
            SalvarAcao(self.Usuario, 's')
            config = open(".settings.txt", 'w').close()
            self.JanelaPrincipal.quit()
            CriptografarDicionario(self.Usuarios, 'u')
            CriptografarDicionario(self.Elementos, 'e')

    def InicarPrograma(self):
        """
        Inicialização da Janela Principal do Programa depois da confirmação do login
        """
        self.JanelaPrincipal.resizable(TRUE, TRUE)
        self.JanelaPrincipal.state('zoomed')  # Maximiza a janela automaticamente após o login
        self.JanelaPrincipal.protocol("WM_DELETE_WINDOW", self.logout)  # Protocolo de fechamento da Janela
        self.JanelaPrincipal.focus_force()

        # Inicialização dos dicionários
        self.Usuarios = DecifrarUsuarios()
        self.Elementos = DecifrarElementos()

        # Unbinding das teclas
        self.JanelaPrincipal.unbind('<FocusIn>')
        self.JanelaPrincipal.unbind('<Escape>')
        self.JanelaPrincipal.unbind('<F1>')

        # Barra de Ferramentas
        self.BarraFerramentas = Frame(self.JanelaPrincipal)
        self.BarraFerramentas.pack(fill=X)

        # Frame Principal
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack(fill=BOTH)

        # Configuração do menu superior
        MenuSuperior = Menu(self.JanelaPrincipal)

        # Menu do Usuário
        MenuUsuario = Menu(MenuSuperior, tearoff=0)
        MenuSuperior.add_cascade(menu=MenuUsuario, label=self.Usuario)
        MenuUsuario.add_command(label="Mudar Senha", command=self.MudarSenha)
        MenuUsuario.add_separator()
        MenuUsuario.add_command(label="Sair", command=self.logout)

        # Colocação dos Menus e Botões de Privilégio Nível 3
        BotaoPesquisar = Button(self.BarraFerramentas, text="Pesquisar", command=self.PesquisarElemento)
        BotaoImprimir = Button(self.BarraFerramentas, text="Imprimir", command=self.ImprimirElementos)
        BotaoLog = Button(self.BarraFerramentas, text="Ver Atividade", command=self.VerificarLog)

        BotaoPesquisar.pack(side=LEFT)
        BotaoImprimir.pack(side=LEFT)
        BotaoLog.pack(side=LEFT)

        MenuVeiculos = Menu(MenuSuperior, tearoff=0)
        MenuSuperior.add_cascade(menu=MenuVeiculos, label="Veículos")
        MenuVeiculos.add_command(label="Pesquisar", command=BotaoPesquisar["command"])
        MenuVeiculos.add_command(label="Imprimir", command=BotaoImprimir["command"])
        if int(self.Usuarios[self.Usuario][1])<=2:  # Posicionamento dos Menus e Botões de Privlégio Nível 2
            BotaoCadastrar = Button(self.BarraFerramentas, text="Cadastrar Veículo", command=self.CadastrarVeiculo)
            BotaoCadastrar.pack(side=LEFT)
        if int(self.Usuarios[self.Usuario][1]) <= 1:  # Posicionamento dos Menus e Botões de Privlégio Nível 1
            MenuVeiculos.add_separator()
            MenuVeiculos.add_command(label="Cadastrar Veículo", command=BotaoCadastrar["command"])
        if int(self.Usuarios[self.Usuario][1]) <= 0:  # Posicionamento dos Menus e Botões de Privlégio Nível 0
            BotaoGerenciar = Button(self.BarraFerramentas, text="Gerenciar", command=self.GerenciarUsuarios).pack(side=LEFT)
            BotaoImprimirUsuario = Button(self.BarraFerramentas, text="Usuários", command=self.ImprimirUsuarios).pack(side=LEFT)
            MenuADM = Menu(MenuSuperior, tearoff=0)
            MenuSuperior.add_cascade(menu=MenuADM, label="Administrar")
            MenuADM.add_command(label="Gerenciar Usuários", command=self.GerenciarUsuarios)
            MenuADM.add_command(label="Imprimir Usuários", command=self.ImprimirUsuarios)

        self.JanelaPrincipal.config(menu=MenuSuperior)

    def PesquisarElemento(self):
        """
        Função definida para o pressionamento do botão pesquisar veículos
        """
        self.FramePrincipal.destroy()  # Destruição do Frame anterior
        self.FramePrincipal = Frame(self.JanelaPrincipal)  # Redefinição do Frame Principal
        self.FramePrincipal.pack(fill=BOTH)

        # Elementos no Frame de Pesquisa
        LabelTitulo = Label(self.FramePrincipal, text="Pesquisar Veículos", font="Verdana, 16")
        LabelNumero = Label(self.FramePrincipal, text="Número de Ordem: ")
        LabelPlaca = Label(self.FramePrincipal, text="Placa do Veículo: ")
        LabelFabricante = Label(self.FramePrincipal, text="Fabricante: ")
        LabelCor = Label(self.FramePrincipal, text="Cor: ")
        LabelKM = Label(self.FramePrincipal, text="Quilometragem (max/min): ")
        LabelRevisao = Label(self.FramePrincipal, text="Última Revisão: ")

        self.EntryNumero = Entry(self.FramePrincipal, width=45)
        self.EntryPlaca = Entry(self.FramePrincipal, width=45)
        self.EntryFabricante = Entry(self.FramePrincipal, width=45)
        self.EntryKMmax = Entry(self.FramePrincipal, width=15)
        self.EntryKMmin = Entry(self.FramePrincipal, width=15)
        self.EntryCor = Entry(self.FramePrincipal, width=45)
        self.EntryAno = Entry(self.FramePrincipal, width=4)

        # Configurações das ComboBox
        dias = ['']
        for d in range (31):
            dias.append(str(d+1))
        self.ComboDia = ttk.Combobox(self.FramePrincipal, width=2, values=dias, state='readonly')
        mes = ['']
        for m in range (12):
            mes.append(str(m+1))
        self.ComboMes = ttk.Combobox(self.FramePrincipal, width=2, values=mes, state='readonly')

        # Configurações da listbox
        Y = Scrollbar(self.FramePrincipal, orient=VERTICAL)
        self.ListaVeiculos = Listbox(self.FramePrincipal, selectmode = SINGLE, yscrollcommand = Y)

        # Botões
        BotaoOK = Button(self.FramePrincipal, text="Pesquisar", command=self.okpesquisa, width=10)
        BotaoVer = Button(self.FramePrincipal, text="Exibir Veículo", command=self.ExibirVeiculoSelecionado, width=10)

        # Geometrização do Frame
        LabelTitulo.grid(row=0, column=0, pady=10, columnspan=5, sticky=N+S+W+E)
        self.ListaVeiculos.grid(row=1, column=0, rowspan = 6, padx=5)
        Y.grid(row=1, column=1, rowspan = 6, sticky=N+S)
        LabelNumero.grid(row=1, column=2, padx=5, pady=5)
        LabelPlaca.grid(row=2, column=2, padx=5, pady=5)
        LabelFabricante.grid(row=3, column=2, padx=5, pady=5)
        LabelKM.grid(row=4, column=2, padx=5, pady=5)
        LabelCor.grid(row=5, column=2, padx=5, pady=5)
        LabelRevisao.grid(row=6, column=2, padx=5, pady=5)
        self.EntryNumero.grid(row=1, column=3, padx=5, pady=5, columnspan=3)
        self.EntryPlaca.grid(row=2, column=3, padx=5, pady=5, columnspan=3)
        self.EntryFabricante.grid(row=3, column=3, padx=5, pady=5, columnspan=3)
        self.EntryKMmin.grid(row=4, column=3, padx=5, pady=5)
        self.EntryKMmax.grid(row=4, column=5, padx=5, pady=5)
        self.EntryCor.grid(row=5, column=3, padx=5, pady=5, columnspan=3)
        self.ComboDia.grid(row=6, column=3, padx=5, pady=5)
        self.ComboMes.grid(row=6, column=4, padx=5, pady=5)
        self.EntryAno.grid(row=6, column=5, padx=5, pady=5)
        BotaoOK.grid(row=7, column=2, columnspan=2, pady=5)
        BotaoVer.grid(row=7, column=4, columnspan=2, pady=5)

        # Associação de Teclas
        self.ListaVeiculos.bind('<Double-Button-1>', BotaoVer["command"])

    def okpesquisa(self):
        """
        Função do botão OK da janela de pesquisa
        """
        SalvarAcao(self.Usuario, 'p')
        self.ListaVeiculos.delete(0, END)
        numero = self.EntryNumero.get()
        placa = self.EntryPlaca.get()
        fabricante = self.EntryFabricante.get()
        cor = self.EntryCor.get()
        kmmin = self.EntryKMmin.get()
        kmmax = self.EntryKMmax.get()
        dia = self.ComboDia.get()
        mes = self.ComboMes.get()
        ano = self.EntryAno.get()
        resultados = PesquisarElemento(self.Elementos, numero, placa, fabricante, cor, kmmin, kmmax, dia, mes, ano)
        for veiculo in resultados:
            self.ListaVeiculos.insert(END, veiculo)
        if len(resultados) == 0:
            messagebox.showerror("Busca Finalizada","Nenhum resultado encontrado.\n"
                                                    "Verifique os filtros de busca e tente novamente.")
        elif len(resultados) == 1:
            messagebox.showinfo("Busca Finalizada","Um veículo encontrado.")
        else:
            messagebox.showinfo("Busca Finalizada", "Um total de %d veículos foram encontrados." % (len(resultados)))

    def ExibirVeiculoSelecionado(self):
        """
        Função que exibe o botão para enxergar veículos, quando algum veículo é selecionado
        """
        try:
            index = self.ListaVeiculos.curselection()[0]
            self.veiculo = self.ListaVeiculos.get(index)

            # Janela Auxiliar de exibição de Informação do Veículo Selecionado
            self.JanelaVeiculo = Toplevel(self.JanelaPrincipal)
            self.JanelaVeiculo.title(self.veiculo)
            self.JanelaVeiculo.resizable(FALSE, FALSE)
            self.JanelaVeiculo.focus_force()
            self.JanelaVeiculo.grab_set()

            LabelNumero = Label(self.JanelaVeiculo, text="Número de ordem: "+self.veiculo)
            LabelNumero.grid(row=0, column=0, columnspan=2, padx=5, sticky = W+E)
            LabelPlaca = Label(self.JanelaVeiculo, text="Placa: "+self.Elementos[self.veiculo][0])
            LabelPlaca.grid(row=1, column=0, columnspan=2, padx=5, sticky = W+E)
            LabelFabricante = Label(self.JanelaVeiculo, text="Fabricante: "+self.Elementos[self.veiculo][1])
            LabelFabricante.grid(row=2, column=0, columnspan=2, padx=5, sticky = W+E)
            LabelCor = Label(self.JanelaVeiculo, text="Cor: "+self.Elementos[self.veiculo][2])
            LabelCor.grid(row=3, column=0, columnspan=2, padx=5, sticky = W+E)
            LabelKM = Label(self.JanelaVeiculo, text="Quilometragem: "+self.Elementos[self.veiculo][3])
            LabelKM.grid(row=4, column=0, columnspan=2, padx=5, sticky = W+E)

            LabelRevisao = Label(self.JanelaVeiculo, text="Última revisão em "+self.Elementos[self.veiculo][4])
            LabelRevisao.grid(row=5, column=0, columnspan=2, padx=5, sticky = W+E)
            try:  # Esse erro acontece quando um veículo não possui uma imagem correspondente
                imagem = PhotoImage(file='.Images/%s.gif' % self.veiculo)
                w, h = imagem.width(), imagem.height()
                if (w) > (h):
                    imagem = imagem.subsample(int(w/300))
                else:
                    imagem = imagem.subsample(int(h/300))
                self.Foto = Label(self.JanelaVeiculo)
                self.Foto.grid(row=6, column=0, columnspan=2, sticky = W+E+N+S)
                self.Foto["image"] = imagem
                self.Foto.image = imagem
            except:
                pass
            finally:
                BotaoOK = Button(self.JanelaVeiculo, text='OK', command=self.JanelaVeiculo.destroy, width=10)
                BotaoOK.grid(row=7, column=0, padx=5, pady=5)
                BotaoModificar = Button(self.JanelaVeiculo, text="Modificar", width=10, state=DISABLED,
                                        command = self.ModificarVeiculo)
                BotaoModificar.grid(row=7, column=1, padx=5, pady=5)
                if int(self.Usuarios[self.Usuario][1]) <= 2:
                    BotaoModificar["state"] = NORMAL
        except IndexError:  # Esse erro acontece quando o usuário escolhe ver um veículo, mas não selecionou nenhum
            pass

    def CadastrarVeiculo(self):
        """
        Função Definida para o Frame de Cadastro de Veículos
        """
        self.FramePrincipal.destroy()
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack(fill=BOTH)

        # Declaração dos objetos no Frame do Cadastro de Elementos
        LabelTitulo = Label(self.FramePrincipal, text="Cadastrar Veículo", font="Verdana, 16")
        LabelNumero = Label(self.FramePrincipal, text="Número de Ordem: ")
        LabelPlaca = Label(self.FramePrincipal, text="Placa: ")
        LabelFabricante = Label(self.FramePrincipal, text="Frabricante: ")
        LabelCor = Label(self.FramePrincipal, text="Cor: ")
        LabelKM = Label(self.FramePrincipal, text="Quilometragem: ")

        self.EntryNumero = Entry(self.FramePrincipal)
        self.EntryPlaca = Entry(self.FramePrincipal)
        self.EntryFabricante = Entry(self.FramePrincipal)
        self.EntryCor = Entry(self.FramePrincipal)
        self.EntryKM = Entry(self.FramePrincipal)

        BotaoCadastrar = Button(self.FramePrincipal, text="Confirmar", width=10, command=self.ConfirmarCadastro)
        BotaoCancelar = Button(self.FramePrincipal, text="Cancelar", width=10)

        # Geometrização do Frame
        LabelTitulo.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        LabelNumero.grid(row=1, column=0, padx=5, pady=5)
        self.EntryNumero.grid(row=1, column=1, padx=5, pady=5)
        LabelPlaca.grid(row=2, column=0, padx=5, pady=5)
        self.EntryPlaca.grid(row=2, column=1, padx=5, pady=5)
        LabelFabricante.grid(row=3, column=0, padx=5, pady=5)
        self.EntryFabricante.grid(row=3, column=1, padx=5, pady=5)
        LabelCor.grid(row=4, column=0, padx=5, pady=5)
        self.EntryCor.grid(row=4, column=1, padx=5, pady=5)
        LabelKM.grid(row=5, column=0, padx=5, pady=5)
        self.EntryKM.grid(row=5, column=1, padx=5, pady=5)

        BotaoCadastrar.grid(row=6, column=0, padx=5, pady=10)
        BotaoCancelar.grid(row=6, column=1, padx=5, pady=10)

    def ConfirmarCadastro(self):
        """
        Função definida para o botão de confirmação de cadastro
        """
        numero = self.EntryNumero.get()
        placa = self.EntryPlaca.get()
        fabricante = self.EntryFabricante.get()
        cor = self.EntryCor.get()
        km = self.EntryKM.get()
        # Se algum dos campos for deixado em branco
        if (numero == '') or (placa == '') or (fabricante == '') or (cor == '') or (km == ''):
            messagebox.showerror("Erro de Registro", "Nenhum campo pode ser deixado em branco.\n"
                                                     "Verifique as informações e tente novamente.")
        elif numero in self.Elementos:  # Se o numero for uma chave do dicionário de elementos
            messagebox.showerror("Erro de Registro", "Já existe um veículo cadastrado com esse número de ordem.\n"
                                                     "Verifique as informações e tente novamente.")
        else:
            self.Elementos = CadastrarElemento(self.Elementos, numero, placa, fabricante, cor, km)
            SalvarAcao(self.Usuario, 'a')
            messagebox.showinfo("Cadastro Efetuado","Veículo Cadastrado com Sucesso.")
            self.EntryNumero.delete(0, END)
            self.EntryPlaca.delete(0, END)
            self.EntryFabricante.delete(0, END)
            self.EntryCor.delete(0, END)
            self.EntryKM.delete(0, END)

    def VerificarLog(self):
        """
        Função definida para o botão de vasculha de log
        """
        self.FramePrincipal.destroy()
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack(fill=BOTH)

        # Objetos no Frame de controle do log
        LabelTitulo = Label(self.FramePrincipal, text="Pesquisar Ações", font="Verdana, 16")
        LabelUsuario = Label(self.FramePrincipal, text="Usuário: ")
        LabelAcao = Label(self.FramePrincipal, text="Ação: ")
        LabelHora = Label(self.FramePrincipal, text="(HH:MM:SS): ")
        LabelData = Label(self.FramePrincipal, text="(DD/MM/AAAA)")

        acoes = ('',"Login", "Logout", "Cadastro", "Busca", "Adição", "Impressão", "Modificação", "Remoção")
        dias = ['']
        for d in range(31):
            dias.append(d+1)
        meses = ['']
        for m in range (12):
            meses.append(m+1)
        horas = ['']
        for h in range(24):
            horas.append(h)
        minutos = ['']
        for m in range(60):
            minutos.append(m)


        self.EntryUsuario = Entry(self.FramePrincipal, width=15)
        self.ComboAcao = ttk.Combobox(self.FramePrincipal, state='readonly', values=acoes, width=15)
        self.ComboDias = ttk.Combobox(self.FramePrincipal, state='readonly', values=dias, width=4)
        self.ComboMes = ttk.Combobox(self.FramePrincipal, state='readonly', values=meses, width=4)
        self.EntryAno = Entry(self.FramePrincipal, width=6)
        self.ComboHora = ttk.Combobox(self.FramePrincipal, state='readonly', values=horas, width=4)
        self.ComboMinutos = ttk.Combobox(self.FramePrincipal, state='readonly', values=minutos, width=4)
        self.ComboSegundos = ttk.Combobox(self.FramePrincipal, state='readonly', values=minutos, width=4)

        self.BotaoVerAcao = Button(self.FramePrincipal, text="Ver", width=10, command=self.OlharLog, state=DISABLED)
        BotaoPesquisa = Button(self.FramePrincipal, text="Pesquisar", width=10, command=self.PesquisaLog)

        Y = Scrollbar(self.FramePrincipal, orient=VERTICAL)
        self.ListaAcoes = Listbox(self.FramePrincipal, selectmode=SINGLE, width=40, yscrollcommand = Y)

        # Geometrização dos Objetos
        LabelTitulo.grid(row=0, column=1, columnspan=4, pady=10, sticky=W+E)

        self.ListaAcoes.grid(row=1, column=0, rowspan=5, padx=5)
        Y.grid(row=1, column=1, rowspan=5, sticky=N+S)

        LabelUsuario.grid(row=1, column=2)
        self.EntryUsuario.grid(row=1, column=3, columnspan=3)

        LabelAcao.grid(row=2, column=2)
        self.ComboAcao.grid(row=2, column=3, columnspan=3)

        LabelHora.grid(row=3, column=2)
        self.ComboHora.grid(row=3, column=3)
        self.ComboMinutos.grid(row=3, column=4)
        self.ComboSegundos.grid(row=3, column=5)

        LabelData.grid(row=4, column=2)
        self.ComboDias.grid(row=4, column=3)
        self.ComboMes.grid(row=4, column=4)
        self.EntryAno.grid(row=4, column=5)

        BotaoPesquisa.grid(row=5, column=4)
        self.BotaoVerAcao.grid(row=5, column=3)

    def PesquisaLog(self):
        self.ListaAcoes.delete(0, END)

        usuario = self.EntryUsuario.get()
        acao = self.ComboAcao.get()
        dia = self.ComboDias.get()
        mes = self.ComboMes.get()
        ano = self.EntryAno.get()
        hora = self.ComboHora.get()
        minuto = self.ComboMinutos.get()
        segundos = self.ComboSegundos.get()

        self.resultados = OrdenarLog(usuario, acao, dia, mes, ano, hora, minuto, segundos)
        if len(self.resultados)>0:
            self.BotaoVerAcao["state"] = NORMAL
            for t in self.resultados:
                self.ListaAcoes.insert(END, t[4])
        else:
            self.BotaoVerAcao["state"] = DISABLED
            messagebox.showerror("Erro de Busca", "Verifique os Filtros e tente novamente.")

    def OlharLog(self):
        acao = self.ListaAcoes.curselection()
        if len(acao) == 0:
            messagebox.showerror("Erro ao Exibir Ação","Selecione uma ação na lista a esquerda e clique"
                                                       " duas vezes, ou clique em "'"Ver"'" para visualizar"
                                                       " a ação em detalhes.")
        else:
            acaouser = self.resultados[int(acao[0])]
            JaneladeAcao = Toplevel(self.FramePrincipal)
            LabelUsuario = Label(JaneladeAcao, text=acaouser[0]).pack()
            LabelAcao = Label(JaneladeAcao, text=acaouser[1]).pack()
            data = acaouser[2][0]+"-"+acaouser[2][1]+"-"+acaouser[2][2]
            LabelData = Label(JaneladeAcao, text=data).pack()
            hora = acaouser[3][0]+":"+acaouser[3][1]+":"+acaouser[3][2]
            LabelHora = Label(JaneladeAcao, text=hora).pack()
            BotaoOK = Button(JaneladeAcao, text="OK", width=10, command=JaneladeAcao.destroy).pack()

    def ImprimirElementos(self):
        if messagebox.askyesno("Confirmar Impressão","Imprimir lista de todos os veículos?"):
            ImprimirDicionarioElementos(self.Elementos)
            messagebox.showinfo("Impressão Concluída", 'Verifique o arquivo "print.txt".')

    def ModificarVeiculo(self):
        self.JanelaVeiculo.destroy()
        self.FramePrincipal.destroy()
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack(fill=BOTH)


        # Declaração dos elementos no Frame Principal
        LabelTitulo = Label(self.FramePrincipal, text="Modificação de Veículo", font="Verdana, 16")
        LabelNumero = Label(self.FramePrincipal, text="Numero de Ordem: "+self.veiculo)
        LabelPlaca = Label(self.FramePrincipal, text="Placa: ")
        placa = Label(self.FramePrincipal, text=self.Elementos[self.veiculo][0])
        LabelFabricante = Label(self.FramePrincipal, text="Fabricante: ")
        fabricante = Label(self.FramePrincipal, text=self.Elementos[self.veiculo][1])
        LabelCor = Label(self.FramePrincipal, text="Cor: ")
        cor = Label(self.FramePrincipal, text=self.Elementos[self.veiculo][2])
        LabelKM = Label(self.FramePrincipal, text="Quilometragem: ")
        km = Label(self.FramePrincipal, text=self.Elementos[self.veiculo][3])

        self.EntryNumero = Entry(self.FramePrincipal)
        self.EntryPlaca = Entry(self.FramePrincipal)
        self.EntryFabricante = Entry(self.FramePrincipal)
        self.EntryCor = Entry(self.FramePrincipal)
        self.EntryKM = Entry(self.FramePrincipal)

        BotaoConfirmar = Button(self.FramePrincipal, text="Confirmar", width='10', command=self.ConfirmarModificacao)
        BotaoExcluir = Button(self.FramePrincipal, text="Excluir", width='10', command=self.ExcluirVeiculo)

        # Geometrização da Janela
        LabelTitulo.grid(row=0, column=0, sticky=W+E, pady=10, columnspan=2)
        LabelNumero.grid(row=1, column=0, sticky=W+E, pady=5, columnspan=2)
        LabelPlaca.grid(row=2, column=0)
        self.EntryPlaca.grid(row=2, column=1, padx=5)
        placa.grid(row=3, column=1)
        LabelFabricante.grid(row=4, column=0)
        self.EntryFabricante.grid(row=4, column=1, padx=5)
        fabricante.grid(row=5, column=1)
        LabelCor.grid(row=6, column=0)
        self.EntryCor.grid(row=6, column=1)
        cor.grid(row=7, column=1)
        LabelKM.grid(row=8, column=0)
        self.EntryKM.grid(row=8, column=1)
        km.grid(row=9, column=1)
        BotaoConfirmar.grid(row=10, column=0, padx=5, pady=10)
        BotaoExcluir.grid(row=10, column=1, padx=5, pady=10)

    def ConfirmarModificacao(self):
        placa = self.EntryPlaca.get()
        fabricante = self.EntryFabricante.get()
        cor = self.EntryCor.get()
        km = self.EntryKM.get()
        self.Elementos = ModificarElemento(self.Elementos,self.veiculo, placa, fabricante, cor, km)
        SalvarAcao(self.Usuario, 'm')
        messagebox.showinfo("Modificação Concluida", "Modificacao Concluida")

    def ExcluirVeiculo(self):
        self.Elementos = ExcluirElemento(self.Elementos, self.veiculo)
        messagebox.showinfo("Veículo Excluído","Veículo %s Excluído com sucesso." %self.veiculo)
        SalvarAcao(self.Usuario, 'r')
        self.FramePrincipal.destroy()
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack(fill=BOTH)

    def GerenciarUsuarios(self):
        self.FramePrincipal.destroy()
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack(fill=BOTH)

        niveis = ("", "Superuser", "Gerente", "Encarregado", "Mecânico")

        # Declaração dos Widgets no Frame
        LabelTitulo = Label(self.FramePrincipal, text="Gerenciamento de Usuários")
        LabelUsuario = Label(self.FramePrincipal, text="Usuário: ")
        LabelNivel = Label(self.FramePrincipal, text="Nível de Acesso: ")
        self.EntryUsuario = Entry(self.FramePrincipal)
        self.ComboNivel = ttk.Combobox(self.FramePrincipal, values=niveis, state="readonly", width=15)

        Y = Scrollbar(self.FramePrincipal, orient=VERTICAL)
        self.ListaUsuarios = Listbox(self.FramePrincipal, selectmode=SINGLE, yscrollcommand=Y)

        BotaoConfirmar = Button(self.FramePrincipal, text="Confirmar", width=10, command=self.ConfirmarAtualizacao)
        BotaoPesquisar = Button(self.FramePrincipal, text="Pesquisar", width=10, command=self.PesquisarUsuario)

        # Geometrização do Frame
        LabelTitulo.grid(row=0, column=0, sticky=W+E)

        self.ListaUsuarios.grid(row=1, column=0, sticky=N+S, rowspan=4)
        Y.grid(row=1, column=1, sticky=N+S, rowspan=4)
        LabelUsuario.grid(row=1, column=2, padx=5)
        self.EntryUsuario.grid(row=1, column=3)
        # row 2 fica livre pra inserção posterior de informações de usuários pesquisados
        LabelNivel.grid(row=3, column=2, padx=5)
        self.ComboNivel.grid(row=3, column=3)
        #row 4 fica livre pra inserção posterior de informações
        BotaoConfirmar.grid(row=5, column=1, padx=2)
        BotaoPesquisar.grid(row=5, column=2, padx=2)

    def ConfirmarAtualizacao(self):
        select = self.ListaUsuarios.curselection()
        nivel = self.ComboNivel.current()
        nivel -= 1
        if len(select)==0:
            messagebox.showerror("Erro na Modificação","Selecione um usuário a ser modificado.")
        else:
            select = select[0]
            usuario = self.ListaUsuarios.get(select)
            if usuario == "adm":
                messagebox.showerror("Erro de Usuário", "O usuário 'adm' não pode ser modificado")
            elif nivel == -1:
                messagebox.showerror("Erro de Nível", "Selecione o novo nível do usuário antes de confirmar a mudança.")
            else:
                self.Usuarios = AtualizarUsuario(self.Usuarios, usuario, nivel)
                SalvarAcao(self.Usuario, "M")
                self.ComboNivel.current(0)
                messagebox.showinfo("Atualização Concluida", "O usuário %s foi modificado com sucesso" % usuario)

    def PesquisarUsuario(self):
        self.ListaUsuarios.delete(0, END)
        usuario = self.EntryUsuario.get()
        nivel = self.ComboNivel.current()
        nivel -= 1
        resultados = PesquisarUsuario(self.Usuarios, usuario, nivel)
        for u in resultados:
            self.ListaUsuarios.insert(END, u)
        tamanho = self.ListaUsuarios.size()
        if tamanho == 0:
            self.ComboNivel.current(0)
            self.EntryUsuario.delete(0, END)
            messagebox.showerror("Erro de Busca","Nenhum resultado encontrado.\n"
                                                 "Verifique os filtros e tente novamente.")
            self.ListaUsuarios.unbind('<Double-Button-1>')
            SalvarAcao(self.Usuario, 'P')
        elif tamanho == 1:
            self.ComboNivel.current(0)
            self.EntryUsuario.delete(0, END)
            messagebox.showinfo("Busca Concluída","Um usuário encontrado.")
            self.ListaUsuarios.bind('<Double-Button-1>',self.DuploClickListaUsuarios)
            SalvarAcao(self.Usuario, 'P')
        else:
            self.ComboNivel.current(0)
            self.EntryUsuario.delete(0, END)
            messagebox.showinfo("Busca Concluida","%d usuários encontrados." % tamanho)
            self.ListaUsuarios.bind('<Double-Button-1>', self.DuploClickListaUsuarios)
            SalvarAcao(self.Usuario, 'P')

    def DuploClickListaUsuarios(self, event):
        select = self.ListaUsuarios.curselection()
        if len(select) == 0:
            pass
        else:
            select = select[0]
            usuario = self.ListaUsuarios.get(select)
            acesso = self.Usuarios[usuario][1]
            if int(acesso) == 0:
                nivel = "Superuser"
            elif int(acesso) == 1:
                nivel = "Gerente"
            elif int(acesso) == 2:
                nivel = "Encarregado"
            elif int(acesso) == 3:
                nivel = "Mecanico"
            messagebox.showinfo("%s" % usuario, "%s: %s" % (usuario, nivel))

    def ImprimirUsuarios(self):
        if messagebox.askyesno("Confirmar Impressão", "Imprimir a lista de usuários do sistema?"):
            ImprimirDicionarioUsuarios(self.Usuarios)
            SalvarAcao(self.Usuario, "u")
            messagebox.showinfo("Impressão Concluída", 'Verifique o arquivo "print.txt".')

    def MudarSenha(self):
        self.FramePrincipal.destroy()
        self.FramePrincipal = Frame(self.JanelaPrincipal)
        self.FramePrincipal.pack()

        # Declaração dos widgets no Frame
        LabelTitulo = Label(self.FramePrincipal, text="Alteração de Senha", font="Verdana, 16")
        LabelSenha = Label(self.FramePrincipal, text="Senha: ")
        LabelNovaSenha = Label(self.FramePrincipal, text="Nova senha: ")
        LabelConfirmar = Label(self.FramePrincipal, text="Confirmar senha: ")
        self.EntrySenha = Entry(self.FramePrincipal, show='*', width=15)
        self.EntryNovaSenha = Entry(self.FramePrincipal, show='*', width=15)
        self.EntryConfirmar = Entry(self.FramePrincipal, show='*', width=15)
        BotaoConfirmar = Button(self.FramePrincipal, text="Confirmar", width=10, command=self.ConfirmarMudanca)

        # Geometrização da Janela
        LabelTitulo.grid(row=0, column=0, columnspan=2)
        LabelSenha.grid(row=1, column=0, padx=5)
        LabelNovaSenha.grid(row=2, column=0, padx=5)
        LabelConfirmar.grid(row=3, column=0, padx=5)
        self.EntrySenha.grid(row=1, column=1, padx=5)
        self.EntryNovaSenha.grid(row=2, column=1, padx=5)
        self.EntryConfirmar.grid(row=3, column=1, padx=5)
        BotaoConfirmar.grid(row=4, column=0, columnspan=2)


    def ConfirmarMudanca(self):
        senha = self.EntrySenha.get()
        senhausuario = self.Usuarios[self.Usuario][0]
        novasenha = self.EntryNovaSenha.get()
        confirmar = self.EntryConfirmar.get()
        if (senha == '') or (novasenha == '') or (confirmar == ''):
            messagebox.showerror("Erro de Senha","Os campos não podem estar em baranco")
            self.EntrySenha.delete(0, END)
            self.EntryNovaSenha.delete(0, END)
            self.EntryConfirmar.delete(0, END)
        elif novasenha != confirmar:
            messagebox.showerror("Erro de Confirmação","Os campos de senha e confirmação devem ser iguais")
            self.EntrySenha.delete(0, END)
            self.EntryNovaSenha.delete(0, END)
            self.EntryConfirmar.delete(0, END)
        elif len(novasenha)<=3:
            messagebox.showerror("Erro de Senha", "A nova senha deve conter pelo menos quatro caracteres")
        elif senha != senhausuario:
            messagebox.showerror("Erro de Senha","Senha incorreta.\nVerifique sua senha e tente novamente.")
            self.EntrySenha.delete(0, END)
        else:
            self.Usuarios = ModificarSenha(self.Usuarios, self.Usuario, novasenha)
            self.EntrySenha.delete(0, END)
            self.EntryNovaSenha.delete(0, END)
            self.EntryConfirmar.delete(0, END)
            messagebox.showinfo("Atualização Concluída","Senha do usuário %s modificada" % self.Usuario)