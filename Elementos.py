'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor:	Antônio Paulino de Lima Neto (apln2); Gustavo Pimentel Fernandes de Melo (gpfm)
Email:	{apln2, gpfm}[at]cin[dot]ufpe[dot]br
Data:	2017-11-11

Script com as funções relacionadas aos elementos
'''
import time

def DecifrarElementos():
    """
    Resgata os elementos atualmente salvos no arquivo elemento.txt
    :return:
    """
    arquivoelementos = open("Arquivos/elementos.txt", 'r')
    dicionarioelementos = {}
    codigo = '=)'
    while codigo != '':  # Enquanto a linha não for vazia, ou seja, enquanto o arquivo não chegar ao fim
        codigo = arquivoelementos.readline()
        if codigo != '':
            num = ''
            numerodeordem = ''
            for c in codigo:  # Leitura do item que será usado como chave para o dicionário de elementos
                if (c != '@'):
                    num += c
                else:  # Sempre que um '@' for encontrado, significa a leitura de um caracter
                    numerodeordem += chr(int(num)-37)
                    num = ''
            codigo = arquivoelementos.readline()  # Depois da leitura da chave, é a vez de ler a tupla correspondente
            contador = 0  # Contador auxiliar que ajuda a ordenar a leitura dos itens
            item = ''  # Variavel auxiliar de recepção dos caracteres decifrados
            for c in codigo:
                if (c != '@') and (c!= '$'):
                    num += c
                elif c == '@':
                    item += chr(int(num)-37)
                    num = ''
                elif c == '$':
                    if contador == 0:
                        placa = item
                    elif contador == 1:
                        fabricante = item
                    elif contador == 2:
                        cor = item
                    elif contador == 3:
                        km = item
                    elif contador == 4:
                        ultimarevisao = item
                    contador += 1
                    item = ''
            dicionarioelementos[numerodeordem] = (placa, fabricante, cor, km, ultimarevisao)
    arquivoelementos.close()
    return dicionarioelementos

def PesquisarElemento(dicionario, numero, placa, fabricante, cor, kmmin, kmmax, dia, mes, ano):
    """
    Pesquisa nos dicionarios de veiculos os elementos que contenham todos os parametros inseridos
    :param dicionario: dicionario de veículos
    :param numero: número de ordem do veículo
    :param placa: placa do veículo
    :param fabricante: fabricante do veículo
    :param cor: cor do veículo
    :param kmmin: quilometragem mínima do veículo
    :param kmmax: quilometragem máxima do veículo
    :param dia: dia da última revisão
    :param mes: mês da última revisão
    :param ano: ano da última revisão
    :return resultados: lista de veículos encontrados que contem os parâmetros
    """
    resultados = []
    if numero != '':  # Se o número de ordem não estiver vazio o usuário procura por um veículo específico
        if numero in dicionario:  # Se o número de ordem estiver cadastrado no dicionário
            resultados.append(numero)
            return resultados
        else:  # Se o número de ordem não estiver cadastrado no dicionário
            return resultados
    else:  # Se o número de ordem não estiver vazio o usuário poderá olhar entre a lista
        for veiculo in dicionario:  # Para cada veículo cadastrado
            if placa != '':  # Se o filtro placa foi fornecido o usuário procura um veículo específico
                if dicionario[veiculo][0] == placa:  # Se a palaca corresponde a placa do veículo cadastrado
                    resultados.append((veiculo))
            else:  # Se o filtro placa não foi fornecido pelo usuário
                continuar = True
                if (fabricante != '') and (dicionario[veiculo][1] != fabricante):
                    continuar = False
                if (cor != '') and (dicionario[veiculo][2] != cor):
                    continuar = False
                if (kmmax!= '') and (int(kmmax)> int(dicionario[veiculo][3])):
                    continuar = False
                if (kmmin != '') and (int(kmmin)<int(dicionario[veiculo][3])):
                    continuar = False
                DIA = dicionario[veiculo][4][0]+dicionario[veiculo][4][1]  # A data da ultima revisão é uma string no formato DD-MM-AAAA
                if (dia != '') and (dia != DIA):
                    continuar = False
                MES = dicionario[veiculo][4][3]+dicionario[veiculo][4][4]  # A data da ultima revisão é uma string no formato DD-MM-AAAA
                if (mes != '') and (mes != MES):
                    continuar = False
                ANO = dicionario[veiculo][4][6]+dicionario[veiculo][4][7]+dicionario[veiculo][4][8]+dicionario[veiculo][4][9]
                if (ano != '') and (ano != ANO):
                    continuar = False
                if continuar:
                    resultados.append(veiculo)
        return resultados

def CadastrarElemento(dicionario, numero, placa, fabricante, cor, km):
    """
    Adiciona um novo veículo ao dicionário de veículos fornecido como parametro contendo as demais informações e também a
    data como sendo da ultima revisão
    :param dicionario: dicionario de elementos contendo os veículos já resgistrados
    :param numero: numero de ordem do veiculo
    :param placa: placa do veículo
    :param fabricante: fabricante do veículo
    :param cor: cor do veículo
    :param km: quilometragem do veículo
    :return dicionario: retorna o dicionário com o veículo já cadastrado
    """
    momento = time.localtime()
    dia = str(momento[2]) + "-" + str(momento[1]) + "-" + str(momento[0])
    dicionario[numero] = (placa, fabricante, cor, km, dia)
    return dicionario

def ImprimirDicionarioElementos(dicionario):
    """
    Imprime os elementos de um dicionário ordenados a partir dos valores de suas chaves em um arquivo
    :param dicionario: dicionário a ser impresso no arquivo
    :return: arquivo "print.txt" é modificado para receber todos os arquivos no dicionário
    """
    impressao = open("print.txt",'w')
    chaves = list(dicionario.keys())
    while len(chaves)>0:
        veiculo = min(chaves)
        placa = dicionario[min(chaves)][0]
        fabricante = dicionario[min(chaves)][1]
        cor = dicionario[min(chaves)][2]
        km = dicionario[min(chaves)][3]
        revisao = dicionario[min(chaves)][4]
        impressao.write("N. Ordem: %s\n" % (veiculo))
        impressao.write("%s(%s)\n" % (fabricante, placa))
        impressao.write("Cor: %s " % (cor))
        impressao.write("Quilometragem: %s " % km)
        impressao.write("Ultima revisao em %s\n" % revisao)
        chaves.remove(min(chaves))

def ModificarElemento(dicionario, veiculo, placa, fabricante, cor, km):
    """
    Atualiza as informações de um veículo, substituindo-as pelas informações fornecidas
    a data e hora da informação "última revisão" são modificados para o momento em que essa função é executada
    Se alguma informação for deixada em branco (string vazia), a informação anterior permanecerá inalterada
    :param dicionario: dicionario contendo o veículo a ser modificado
    :param veiculo: veiculo cuas informações serão modificadas
    :param placa: nova placa
    :param fabricante: novo fabricante
    :param cor: nova cor
    :param km: nova km
    :return dicionario: dicionario contendo as novas informações do veículo
    """
    if placa == "":
        novaplaca = dicionario[veiculo][0]
    else:
        novaplaca = placa

    if fabricante == "":
        novofabricante = dicionario[veiculo][1]
    else:
        novofabricante = fabricante

    if cor == "":
        novacor = dicionario[veiculo][2]
    else:
        novacor = cor

    if km == "":
        novakm = dicionario[veiculo][3]
    else:
        novakm = km

    momento = time.localtime()

    novarevisao = str(momento[2]) + "-" + str(momento[1]) + "-" + str(momento[0])

    dicionario[veiculo] = (novaplaca, novofabricante, novacor, novakm, novarevisao)
    return dicionario

def ExcluirElemento(dicionario, elemento):
    """
    Exclui o elemento indicado do dicionário de elementos
    :param dicionario: dicionário que contem os elementos
    :param elemento: elemento
    :return dicionario: dicionario agora sem o elemento excluido
    """
    dicionario.pop(elemento)
    return dicionario