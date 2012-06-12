# -*- encoding: utf-8 -*-

from sys import argv
from os.path import exists

# recupera o nome do arquivo a ser aberto em filename
script, filename = argv

# abre o arquivo
file_ = open(filename)

print "O arquivo %s possui o conteudo:" % filename
# imprime o arquivo
print file_.read()

# fecha arquivo
file_.close()

file_ = open(filename)

# imprime apenas uma linha e avança o cursor

print file_.readline()

print file_.readline()

# criar e escrever em arquivo

file_.close()

# verificando se o arquivo já existe
print "O arquivo 'teste.txt' existe?\n%s" % exists("teste.txt")

file_ = open("teste.txt", 'w')
# obs: cuidado, o método de abertura 'w' apaga o arquivo de nome igual ao primeiro parâmetro do open, caso já exista

# limpa o arquivo
# obs: não necessário após abertura de arquivo com método 'w'
file_.truncate()

# escrevendo no arquivo

# lê do usuário

o_que = raw_input("Diz ai o que tu quer\n> ")

file_.write(o_que)

file_.close()
