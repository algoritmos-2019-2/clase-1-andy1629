#! /usr/bin/env python2.7
  
print("determinar si el numero ingresado es primo")

def primo(z):
	x= int(2)
	band = "T"

	while((band == "T") and (x < z)):
        	if((z % x) == 0):
               	   band = "F"
        	else:
               	 x = x + 1
	if(band == "T"):
        	print("numero es primo")
	else:
        	print("numero no es primo")

primo(int(input("introduzca numero")))			

print(" genere los numeros primos menores o iguales que pertenecen a los naturales")

def primo_menorigual(n):
	print( "numero",n)
	primo(n)  
        
	x = int(2)	
	if n > 0:
	
		for i in range(2,n) :
			creciente = 2
			esprimo = True
			while esprimo and creciente < i:
				if i % creciente == 0:
					esprimo = False
				else:
					creciente += 1
		
			if esprimo:
				print(i,"es primo")
	else:
		print("el numero no es primo")
primo_menorigual((int(input("numero"))))


print("programa numeros gemelos")

def numero_gemelo(x, y):
	comprobar = True
	
	a = 0
	if x > 0 and y > 0 and x != y:
		comprobar = False
	if x > y:
		x ^= y
		x ^= y
		x ^= y
	i = x
	while i <= y:
		creciente = 2
		esprimo = True
		while esprimo and creciente < i:
			if i % creciente == 0:
				esprimo = False
			else:
				 creciente += 1
		if esprimo and not a:
			a = i
		elif esprimo and a:
			b = i
			if b-a ==2:
				print(a,"y",b,"son gemelos")
			a = i
		i += 1
	else:
		if x == y:
			print("los numeros son iguales prueba con otros")

numero_gemelo((int(input("numero"))), int(input("numero")))

print("programa regrese una lista con la descompensacion en potencias de primos")

lista=[]
def primo(r):

	for x in range (1,r):
		if (r%x==0 and x!=r and x!=1):
			return False
	return r

def lista_primos(t):
	
	for x in range(2,t):
		if primo(x)!=False:
			lista.append(x)
	return lista

def divisible(lista,j):
	for numero in lista:
		if j%numero==0:
			factores.append(numero)
	return factores

def factorx(lista, numero, factores_finales):

	divisibles=[]
	

	while True:
		salida1 = primo(numero)
		if salida1!=False:
			factores_finales.append(salida1)
			break

		else:
			lista_primos(numero)	
			divisibles=divisible(lista, numero) 

			factores_finales.append(divisibles[len(divisibles)-1])
			numero=numero/divisibles[len(divisibles)-1]
	return factores_finales
		



factores_finales=[1]
lista=[]
factores=[]
numero=input("Ingrese un numero: ")
print factorx(lista, numero, factores_finales)

print("preguntas funciones")

print("1 para poder hacer pequenos programas y despues mandarlos a llamar en otro programa con el nombre dado")
print("cuando pones el nombre y dos parentesis")

print("2 el enunciado es def y dos parentesis")

print("3 la funcion es el programa como tal, la llamada de funcion es cuando lo ejecutas")


print("4 puede a ver las variables que sean tanto globales como locales pero estas variables solo pueden ser una de estas")

print("5h")

print("6 la variable de retorno es para regresar inmediatamente a esta funcion y use la siguiente expresion como un valor de retorno")

print("7 no devuelve valores de la funcion")
print("8 le pones el nombre de la variable y antes de este global")
print("9 es el que sirve para inicilaizar una variable previa o para introduzir una variable como comodin")
print("10 la declaracion import random sirve para llamar la biblioteca con nombre random")
print("11 para llamar a esta funcion tenemos que poner random.randint(x,y)")



print("maximo comun divisor")

def maximo(x, y):

	resto = 0
	while(y > 0):
		resto = y
		y = x % y
		x = resto
	return x

n1 = int(input("numero"))
n2 = int(input("numero"))

print(maximo(n1, n2))

print("minimo comun multiplo")

def minimo(x, y):

	if x > y:
		mayor = x
	else:
		mayor = y
	while(True):
		if((mayor % x == 0) and (mayor % y == 0)):
			minimo = mayor
			break
		mayor += 1
	return minimo

n1 = int(input("numero"))
n2 = int(input("numero"))
print(minimo(n1, n2))
