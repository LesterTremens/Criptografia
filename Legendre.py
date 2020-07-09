# coding=utf-8
# Símbolo de Legendre
import math

# Dados a y p, calcula el símbolo de Legendre.
def simbolo (a,p):
	val = (a**((p-1)/2))
	val = val%p
	return val

# Calcula el símbolo de Legendre utilizando el símbolo de Jacobi.
def Jacobi (a,primos,n):
	legendre = 1
	for p,b in primos:
		print("Procesando: ", p , b)
		temp = simbolo (a,p)
		print("termina simbolo")
		temp = temp%n
		temp = temp**b
		temp = temp%n
		legendre *= temp
		legendre = legendre%n
		# print(legendre)

	return legendre;


# Algoritmo extendido de Euclides.
def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

# Auxiliar
def abs (a,b):
	while (a < 0):
		a += b
	return a


if __name__ == '__main__':
	print("Liz bebé :3")
	"""
	n = 643590535502220839951864707825089693615082777917210823151199409440412309104
	e = 101
	# x0 Da el inverso multiplicativo 
	b, x0, y0 = xgcd(e,n)
	x0 = abs(x0,n)
	print(b,x0,y0)
	""" 
	n = 330760674675552500004362908731
	a = 2
	primos = [(127151072740801,1),(3,1),(7,1),(131,1),(62003,1),(15250727,1)]
	print(Jacobi(a,primos,n)																																																																																																																																																																																																																																																																																																																																																															)
