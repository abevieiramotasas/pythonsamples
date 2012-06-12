# -*- encoding: utf-8 -*-

# importa argv(variável de argumento)
from sys import argv

# unpack
# o primeiro valor é o nome do script
# os demais são os parâmetros passados ao script, na ordem em que foram passados
script, pri, seg, ter = argv

print "script se chama", script
print "primeira variável", pri
print "segunda variável", seg
print "terceira variável", ter
