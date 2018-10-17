#==================================================================#
# Universidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informática -- CIn (http://www.cin.ufpe.br)
# Graduandas em Sistemas de Informação
# IF968 -- Programação 1
#
# Autores: Antônio Paulino de Lima Neto; Gustavo Pimentel Fernandes de Melo
# Emails: apln2@cin.ufpe.br; gpfm@cin.ufpe.br
# Data: 12/11/2017
#
# Descrição:
# O Python Vehicle Keeper é um programa para gerenciamento de veículos em oficinas, tem por objetivo melhor controlar
# a quilometragem dos veículos, data das revisões assim como classficação por características.
#==================================================================#
'''
Sumário
#1. Importações
#2. Definição de Constantes
#3. Funções Auxiliares
    #3.1. Tokenizar
    #3.2. Função 02
    #3.3. Função 03
#4. Funções Principais
    #4.1. Gravar no Arquivo
    #4.2. Função 02
    #4.3. Função 03
#5. Programa (User Interface)
'''
#1. Importações
from JanelaPrincipal import Keeper

#2 Definição de Constantes
__author__ = "Antônio Paulino de Lima Neto"
__coauthor__ = "Gustavo Pimentel Fernandes de Melo"
__version__ = "beta"
__emails__ = "apln2@cin.ufpe.br","gpfm@cin.ufpe.br"
__data__ = "2017-10-05"

print_file = "print.txt"
log_file = "Arquivos/log.txt"
element_file = "Arquivos/elementos.txt"
user_file = "Arquivos/usuarios.txt"

#3 Funções Auxiliares
    #3.1 Rotinas
        #3.1.1 Criptografar Dicionário
        #3.1.2 Salvar Ação
        #3.1.3 Confirmar Login
        #3.1.4 Ordenar Log
#4 Funções Principais
    #4.1 Elementos
        #4.1.1 Decifrar Elementos
        #4.1.2 Pesquisar Elemento
        #4.1.3 Cadastrar Elemento
        #4.1.4 Imprimir Dicionário de Elementos
        #4.1.5 Modificar Elemento
        #4.1.6 Excluir Elemento
    #4.2 Usuários
        #4.2.1 Decifrar Usuários
        #4.2.2 Imprimir Dicionário de Usuários
        #4.2.3 Pesquisar Usuário
        #4.2.4 Atualizar Usuário
        #4.2.5 Modificar Senha
#5 Programa (User Interface)
    #5.1 Janela de Login
        #5.1.1 __init__
        #5.1.2 Verificar Login
    #5.2 Janela de Cadastro
        #5.2.1 __init__
        #5.2.2 Confirmar
        #5.2.3 Janela de Ajuda
    #5.3 Janela Principal (Keeper)
        #5.3.1 __init__
        #5.3.2 Login
        #5.3.3 Logout
        #5.3.4 Iniciar Programa
        #5.3.4 Frame de Pesquisa
        #5.3.5 Pesquisar Elemento
        #5.3.6 Janela Auxiliar de Exibição de Veículos Pesquisados
        #5.3.7 Frame de Cadastro de Veículo
        #5.3.8 Cadastro de Veículo
        #5.3.9 Frame de Verificação de Log
        #5.3.10 Pesquisa de Log
        #5.3.10 Exibição das Ações resultado da Pesquisa
        #5.3.11 Impressão de Veículos para o Arquivo
        #5.3.12 Frame de Modificação de Veículo
        #5.3.13 Modificação de Veículo
        #5.3.14 Exclusão de Veículo
        #5.3.15 Frame de Gerenciamento de Usuários
        #5.3.16 Modificação de Nível de Usuário
        #5.3.17 Pesquisa de Usuários
        #5.3.18 Exibir Informações de Usuários Pesquisados
        #5.3.19 Impressão de Usuários e Níveis
        #5.3.20 Frame de Mudar Senha
        #5.3.21 Mudança de Senha

Keeper()