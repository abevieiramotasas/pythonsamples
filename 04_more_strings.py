# -*- encoding: utf-8 -*-

# %s converte o valor a ele associado utilizando o método str()
# %r converte o valor a ele associado utilizando o método repr()
a = "c %s c"
b = "c %r c"
teste = "teste"
print a % teste
print a % teste

# concatenação

right = "direita né"
left = "esquerda"
print right + " " + left

# repetição

print "a"*10

# vírgula ao fim do print faz com que ele adicione um caractere de espaço e não de quebra de linha 
print "a" + "b",
print "elardo"

# uso como template

template = "nome = %(nome)s\ne-mail = %(email)s\n%(erro)s"

print template % { "nome" : "Abelardo", "email" : "abevieiramota at gmail dot com", "erro" : "" }
print template % { "nome" : "Ta tudo errado", "email" : "mel dels", "erro" : "Tem coisa errada ai" }

# strings formatadas

HTML_DOIDO = """
<input type="text" />

<inpyt type="password" />
"""

print HTML_DOIDO
