'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Antônio Paulino de Lima Neto (apln2); Gustavo Pimentel Fernandes de Melo (gpfm)
Email:	{apln2, gpfm}[at]cin[dot]ufpe[dot]br
Data:	2017-10-21

Script com as principais funções genéricas do sistema.
------------------------------------- Indice de funções do script -------------------------------------
CriptografarDicionario(Dicionario, tipo)
DecifrarUsuario()
SalvarAcao()
ConfirmarLogin()
DecifrarElementos()
'''
import time

def CriptografarDicionario (dicionario, tipo):
    """
    Criptografa as informações de um dicionario (composto por chaves (strings) e valores (tuplas) para um arquivo.
    :param dicionario:
    :param tipo:
    :param dicionario:
    :param tipo:
    :return:
    """
    if tipo == 'u':  # caracter 'u' determina que o tipo de dicionário a ser salvo é de usuários
        arquivo = open("Arquivos/usuarios.txt", 'w')
    elif tipo == 'e':  # caracter 'e' determina que o tipo de dicionário a ser salvo é de elementos
        arquivo = open("Arquivos/elementos.txt", 'w')
    else:
        return
    criptografia = ''
    for chave in dicionario:  # Esse for acessa cada chave do dicionário
        for c in chave:  # Esse for acessa cada caracter da string que compõe a chave
            criptografia+= str(ord(c)+37)+"@"
        arquivo.write(criptografia+'\n')  # Depois de ler todos os caracteres da chave, a chave é criptografada e salva
        criptografia = ''
        for item in dicionario[chave]:  # Esse for acessa cada item nas tupla acossiadas as chaves do dicionário
            for c in item:
                criptografia+= str(ord(c)+37)+"@"
            arquivo.write(criptografia+'$')  # Os itens nas listas são salvos e separados por '$'
            criptografia = ''
        arquivo.write('\n')  # Depois de ler toda uma lista, os arquivos nela são salvos e o cursos segue para a proxima linha
    arquivo.close()
    return

def SalvarAcao(usuario, option, info=''):
    """
    Marca a data, hora, nome do usuário e ação desempenhada no arquivo de logs no formato abaixo:
    DD-MM-AAA HH:MM:SS
    @usuario: <ação>
    :return:
    """
    symbol = ''
    if (option == 'l'):
        acao = "efetuou login com sucesso."
        symbol = '@'
    elif (option == 'c'):
        acao = "cadastrou-se com sucesso."
        symbol = '&'
    elif (option == 's'):
        acao = "saiu."
        symbol= '#'
    elif (option == 'p'):
        acao = "fez uma pesquisa de veiculos."
        symbol = '$'
    elif (option == 'P'):
        acao = "fez uma pesquisa de usuarios."
        symbol = '$'
    elif (option == 'a'):
        acao = "adcionou um novo veiculo."
        symbol='+'
    elif (option == 'i'):
        acao = "imprimiu a lista de veiculos."
        symbol='!'
    elif (option == 'r'):
        acao = "removeu um veiculo."
        symbol = '-'
    elif (option == 'm'):
        acao = "modificou um veiculo."
        symbol = '%'
    elif (option == 'M'):
        acao = "modificou o nível de acesso de um usuário."
        symbol = '%'
    elif (option == 'u'):
        acao = "imprimiu a lista de usuários do sistema."
        symbol = '!'
    else:
        return
    ArquivoLogs = open("Arquivos/log.txt",'a')
    momento = time.localtime()
    Data = str(momento[2]) + "-" + str(momento[1]) + "-" + str(momento[0])
    Hora = str(momento[3]) + ":" + str(momento[4]) + ":" + str(momento[5])
    ArquivoLogs.write(symbol+Data+' '+Hora+'\n'+usuario+": "+acao+'\n')
    ArquivoLogs.close()
    return

def ConfirmarLogin():
    """
    Confirmação de Login, retorna uma string contendo o nome do usuário escrito no arquivo de controle
    :return usuario: string contendo o nome do usuário, caso o login tenha sido confirmado ou uma string vazia
    """
    configuracoes = open(".settings.txt",'r')
    usuario = configuracoes.readline()
    configuracoes.close()
    return usuario

def OrdenarLog(user, tipo, dia, mes, ano, hora, minuto, segundo):
    """
    Retorna um dicionario tendo as datas como chave e contendo as ações dos usuários como valor
    :param user: usuário que tenha executado as ações
    :param tipo: tipo específico de ação
    :param dia: dia em que a ação foi executada
    :param mes: mês em que a ação foi executada
    :param ano: ano em que a ação foi executada
    :param hora: hora em que a ação foi executada
    :param minuto: minuto em que a ação foi executada
    :param segundo: segundo em que a ação foi executada
    :return resultados: lista de tuplas contendo as informações (usuario, data, hora, ação)
    """
    arquivolog = open('Arquivos/log.txt', 'r')
    listadeacoes = []
    resultados = []
    codigo = ':p'
    while codigo != '':
        codigo = arquivolog.read(1)
        if codigo != '':
            if codigo == '@':
                acao = "Login"
            elif codigo == '&':
                acao = "Cadastro"
            elif codigo == '#':
                acao = "Logout"
            elif codigo == '$':
                acao = "Busca"
            elif codigo == '+':
                acao = "Adição"
            elif codigo == '!':
                acao = "Impressão"
            elif codigo == '-':
                acao = "Remoção"
            elif codigo == '%':
                acao = "Modificação"
            codigo = arquivolog.readline()
            temp = ''
            DD = ''
            hh = ''
            for c in codigo:
                if c!='-' and c!=':' and c!=' ' and c!= '\n':
                    temp += c
                elif c=='-' and DD=='':
                    DD = temp
                    temp = ''
                elif c=='-' and DD!='':
                    MM = temp
                    temp = ''
                elif c==' ':
                    AAAA = temp
                    temp = ''
                elif c==':' and hh=='':
                    hh = temp
                    temp = ''
                elif c==':' and hh!='':
                    mm = temp
                    temp = ''
                elif c=='\n':
                    ss = temp
            codigo = arquivolog.readline()
            temp = ''
            for c in codigo:
                if c!=':' and c!= '\n':
                    temp += c
                elif c==':':
                    usuario = temp
                    temp = ''
                elif c=='\n':
                    texto = temp
            data = (DD, MM, AAAA)
            momento = (hh,mm,ss)
            listadeacoes.append((usuario, acao, data, momento, str(usuario+texto)))
    for t in listadeacoes:  # Comparação dos parametros com cada item da tupla
        continuar = True
        if user != '' and t[0] != user:
            continuar = False
        elif tipo != '' and t[1]!= tipo:
            continuar = False
        elif dia != '' and t[2][0] != dia:
            continuar = False
        elif mes != '' and t[2][1] != mes:
            continuar = False
        elif ano != '' and t[2][2] != ano:
            continuar = False
        elif hora != '' and t[3][0] != hora:
            continuar = False
        elif minuto != '' and t[3][1] != minuto:
            continuar = False
        elif segundo != '' and t[3][2]!= segundo:
            continuar = False
        if continuar:
            resultados.append(t)
    return tuple(resultados)