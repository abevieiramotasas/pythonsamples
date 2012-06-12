# -*- encoding: utf-8 -*-

# declaração de variável

cars = 100
car_com_underline = 20

# utilização

print "Eu tenho", cars, "sendo", car_com_underline, "fuscas"

# outra forma de imprimir
# bom para criar templates a serem preenchidos de forma variada
# as variáveis na string são preenchidas de acordo com a ordem em que aparecem
# no template e na tupla
print "Eu tenho %d sendo %s fuscas" % (cars, "20")

# outra forma 

print "Eu tenho %(num_cars)d sendo %(num_fuscas)s fuscas" % { "num_cars" : cars, "num_fuscas" : "20" }
