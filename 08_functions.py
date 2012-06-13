# -*- encoding: utf-8 -*-

# funções

def nome_da_funcao(*args_variaveis):
	# desempacotando dois argumentos
	# uso [:2] para limitar o unpack aos dois primeiros 
	# argumentos
	arg1, arg2 = args_variaveis[:2]
	print arg1, arg2

nome_da_funcao("Argumento 1", "Argumento 2", "Argumento 3 que não vai ser printado")
