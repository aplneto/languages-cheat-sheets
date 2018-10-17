'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Antônio Paulino de Lima Neto (apln2); Gustavo Pimentel Fernandes de Melo (gpfm)
Email:	{apln2, gpfm}[at]cin[dot]ufpe[dot]br
Data:	2017-11-13

Script de configuração e controle das funções de usuários
'''

def DecifrarUsuarios ():
    """
    Lê e decifra os usuários criptografados no arquivo de usuários
    :return dicionario:
    """
    ArquivoUsuarios = open ("Arquivos/usuarios.txt", 'r')
    codigo = '^.^'
    dicionario = {}
    while (codigo != ''):
        codigo = ArquivoUsuarios.readline() #Caso não seja o fim do arquivo, codigo assume o valor da chave criptografada
        if (codigo != '') and (codigo != '\n'):
            num = ''
            chave = ''
            for c in codigo: #As linhas ímpares contêm as chaves do dicionário
                if (c == '@'):
                    chave += chr(int(num)-37)
                    num = ''
                elif (c != '\n'):
                    num += c
            codigo = ArquivoUsuarios.readline()
            item = ''
            senha = ''
            for c in codigo: #As linhas pares contêm os items da tupla (Senha, Nível)
                if (c=='@'):
                    item += chr(int(num)-37)#Descriptografia de um digito
                    num = ''
                elif (c=='$'): #'S' representa o fim da escrita de um nome de item
                    if (senha == ''):
                        senha = item
                        item = ''
                    else:
                        nivel = item
                        dicionario[chave] = (senha, nivel)
                elif (c != '\n'):
                    num += c #Adição de digito por digito separados por '@'
    ArquivoUsuarios.close()
    return dicionario

def ImprimirDicionarioUsuarios(dicionario):
    """
    Imprime a lista de chaves do dicionário de usuários seguidas pelo valor 0 da tupla valor, que corresponde ao nível de acesso.
    :param dicionario: dicionario a ser impresso
    :return:
    """

    arquivoimpressao = open("print.txt",'w')
    for u in dicionario:
        arquivoimpressao.write("User: %s\nLevel: %s\n" % (u, dicionario[u][1]))

def PesquisarUsuario(dicionario, usuario, nivel):
    """
    Lista todos os usuários de um nível específico ou retorna um usuário específico
    :param usuario: usuário a ser exibido ou uma string vazia, caso a busca seja por nível
    :param dicionario: dicionário contendo todos os usuários
    :param nivel: entre 0 e 3 para buscar por níveis específicos ou -1 caso a busca seja por usuário
    :return resultados: lista com as chaves de usuários correspondentes
    """
    resultados = []
    for u in dicionario:
        continuar = True
        if usuario != '' and u!=usuario:
            continuar = False
        elif nivel>=0 and dicionario[u][1]!=str(nivel):
            continuar = False

        if continuar:
            resultados.append(u)
    return resultados

def AtualizarUsuario(dicionario, usuario, nivel):
    """
    Modifica o nível de acesso de um usuário
    :param dicionario: dicionário que contem o usuário
    :param usuario: chave do dicionário
    :param nivel: novo nível do usuário
    :return dicionario: com o elemento modificado
    """
    senha = dicionario[usuario][0]
    dicionario[usuario] = (senha, str(nivel))
    return dicionario

def ModificarSenha(dicionario, usuario, senha):
    """
    Modifica a tupla correspondente a chave usuario no dicionário, alterando o valor da senha na tupla
    :param dicionario: dicionário que contem o usuário
    :param usuario: chave do dicionário cujo valor será modificado
    :param senha: nova string contendo a senha
    :return dicionario: dicionario contendo o novo valor da chave usuario
    """
    nivel = dicionario[usuario][1]
    dicionario[usuario] = (senha, nivel)
    return dicionario