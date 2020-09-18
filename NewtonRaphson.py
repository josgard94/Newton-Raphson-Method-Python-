
#
#	Autor: Edgard Diaz
#	Clase que contiene la logica del metodo Newton-Raphson 
#
#

import math as m

class NewtonRaphsonMethod:
	iteracion = 1
	error = 0
	x1 = 0
	def Funcion(self, x):

		return 2*m.sin(x)-x #Funcion a evaluar en un punto incial para aproximar una raiz

	def FuncionDerivada(selft, x):
		
		return 2*m.cos(x) - 1 #Derivada de la  función a evaluar

	def Method(self, iteraciones, tolerancia, x0): #implementación de la logica del metodo
		
		
		while(True):

			if self.iteracion > iteraciones: #criterio de paro para eviatar que el programa se cicle si no logra converger
				return 0
			else:

				self.x1 = x0 - (self.Funcion(x0)/self.FuncionDerivada(x0)) #calcular aproximación de acuerda a la ecuación del  metodo
				self.error = abs(self.x1 - x0) #Calcular  el  entre la dos aproximaciones sucesivas, entre mas pequeño es el error  más cerca se encuntra la aproximacion a la raiz real

				if self.error <= tolerancia: #criterio  de paro  si error menor a tolerancia el programa logro converger
					return 1
				else: #Si el criterio de paro no cimple entonces  incrementar el contador de iteraciones e igualar x0 al valor de x1
					x0 = self.x1
					self.iteracion = self.iteracion + 1

