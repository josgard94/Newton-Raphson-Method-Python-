#
#
#	Este programa realiza la aproximación de las racies de una funcion real usando el método de Newton - Raphson
#	Author: Edgard Diaz
#
#
from  NewtonRaphson import NewtonRaphsonMethod

if __name__ == '__main__':

	interaciones = 100 #Total de iteraciones para realizar una aproximación
	x0 = float(input("Punto incial: ")) #Punto inicial para la primer aproximacion
	tolerancia = float(input("Tolerancia: ")) #Tolerancia de error,  entre más pequeño el valor más cercana es la raiz aproximada

	obj = NewtonRaphsonMethod() #objeto para acceder a los metodos de la clase

	op = obj.Method(interaciones, tolerancia, x0) #invocar logica del programa

	if op == 0:
		print("El programa no logra converger")
	else:
		print("Raiz aproximada: {0:.5f}".format(obj.x1),"\nError de aproximacion: {0:.5f}".format(obj.error),"\nIteraciones realizadas: ",str(obj.iteracion))	

