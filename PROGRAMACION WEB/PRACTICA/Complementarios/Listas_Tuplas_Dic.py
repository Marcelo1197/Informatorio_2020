# PRIMERA PARTE

# EJERCICIO b 
"""
lista = []

for i in range(0, 5):
	lista.append(int(input("Ingrese un elemento en la lista:\n\t")))

lista = [elemento**2 for elemento in lista]
print(lista)
"""

# EJERCICIO c
"""
lista = []
elemento = 0

while elemento != 999:
	elemento = int(input("Ingrese un numero o 999 para salir:\n\t"))
	lista.append(elemento)

print(lista, "\n\n")

for i in range(len(lista)):
	if lista[i] < 0:
		lista[i] = 0

print(lista)
"""

# EJERCICIO d
"""
def eliminar_numero(listaP, numeroP): # Este método es invocando a la misma función de forma recursiva.
	if numeroP in listaP:
		indice = listaP.index(numeroP)
		del listaP[indice]
		eliminar_numero(listaP, numeroP) #La funcion se va a invocar hasta que la condicion if numeroP in listaP sea FALSA.
"""
"""
def eliminar_numero(listaP, numeroP):
	bandera = True
	while bandera:
		if numeroP in listaP:
			del listaP[listaP.index(numeroP)] # A través del metodo index(), obtengo la posición del número y lo puedo eliminar con "del".
		else:
			bandera = False


lista = []
elemento = 0

while elemento != 999:
	elemento = int(input("Ingrese un numero o 999 para salir:\n\t"))
	if elemento == 999:
		break
	lista.append(elemento)

print("\nLista cargada: ", lista, "\n\n")
numero = int(input("Ingrese un numero a eliminar de la lista:\n\t"))

eliminar_numero(lista, numero)
print("\nNueva lista: ", lista, "\n\n")
"""

# EJERCICIO g

"""
cantidad_elementos = int(input("¿Cuantos elementos desea cargar en las LISTAS?:\n\t"))
lista1 = []
lista2 = []
lista3 = []

for i in range(cantidad_elementos):
	lista1.append(input("Ingrese el elemento: "))
lista3.extend(lista1)
print("Primera lista: ", lista1)

for i in range(cantidad_elementos):
	lista2.append(input("Ingrese el elemento: "))
lista3.extend(lista2)
print("Segunda lista: ", lista2)

print(lista3.sort())
print("Nueva lista ordenada y compuesta por las anteriores:\n", lista3)
"""

# EJERCICIO H
"""
lista = []
numero_control = -1
suma = 0

while numero_control != 0:
	numero_control = int(input("Ingrese un numero o 0 para salir:\n\t"))
	lista.append(numero_control)

for elemento in lista:
	if elemento%2 == 0:
		suma += elemento

print("\n\nSuma de todos los elementos pares de la lista: ", suma)
"""

# Ejercicio i

"""
lista = list(range(30, 46))
print("Lista de 15 números: ", lista)

lista2 = [elemento*2 for elemento in lista if elemento%2 == 0]
print("\n\nNueva lista: ", lista2)
"""

# Ejercicio k
"""
lista = []
lista2 = []
numero_control = -1

while numero_control != "0":
	numero_control = input("Ingrese un elemento para la primer lista o 0 para salir:\n\t")
	lista.append(numero_control)
	if numero_control == "0":
		lista.remove("0")

numero_control = -1

while numero_control != "0":
	numero_control = input("Ingrese un elemento para la segunda lista o 0 para salir:\n\t")
	lista2.append(numero_control)
	if numero_control == "0":
		lista2.remove("0")

lista = [elemento for elemento in lista2]

print("Lista 1 actualizada con los elementos de la segunda y no de la primera:\n\n", lista)
"""

# UN POCO MAS COMPLICADO
# Ejercicio A
"""
lista = []
lista_auxiliar = []
palabra_control = 0
palindromo_contador = 0

print("Ingreso de palabras caracter por caracter:\n\n")
while palabra_control != "0":
	palabra_control = input("Ingrese el caracter correspondiente o 0 para salir:\n\t")
	lista.append(palabra_control)
	if palabra_control == "0":
		lista.remove("0")

lista_auxiliar.extend(lista) # Utilizo la lista_auxiliar para conservar la lista original
lista.reverse() # Y luego procedo a invertir la lista

print("Palabra normal: ", lista_auxiliar)
print("Palabra invertida: ", lista)

for i in range(len(lista)):
	if lista_auxiliar[i] == lista[i]: # Comparo caracter por caracter la lista normal (auxiliar) con la invertida
		palindromo_contador += 1 

if palindromo_contador == len(lista): # Si es palíndromo el contador debe ser igual a la longitud de la lista, ya que si fallaba una comparación de caracteres, no se contaba.
	print("Es una palabra palíndroma")
else:
	print("No es una palabra palíndroma")
"""