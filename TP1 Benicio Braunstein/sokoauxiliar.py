

lista = [list("###$#")]
aux = lista[0][4] 
lista[0][4] = lista[0][3] 
lista[0][3] = aux
lista[0][0] = "*"
print(lista)
