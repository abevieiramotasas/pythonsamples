# -*- encoding: utf-8 -*-

# funções

def nome_da_funcao(*args_variaveis):
	# desempacotando dois argumentos
	# uso [:2] para limitar o unpack aos dois primeiros 
	# argumentos
	arg1, arg2 = args_variaveis[:2]
	print arg1, arg2

nome_da_funcao("Argumento 1", "Argumento 2", "Argumento 3 que não vai ser printado")

from sys import argv

script, file_name = argv[:2]

def print_all(f):
	print f.read()

# retorna o cursor para o início do arquivo
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(file_name)

print "Imprimindo todo o conteudo"

print_all(current_file)

print "Voltando o cursor"

rewind(current_file)

print "Imprimindo duas linhas"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


# funções com retorno

def add(a, b):
	return a+b


