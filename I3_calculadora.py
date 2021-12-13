#Tarea1: Añadir funcion para sumar, 
#y modificar el diccionario 'procesar' para que el 1er elemento
#invoque a la funcion sumar con los parámetros correctos.

#Tarea2: Añadir funcion para restar
#y modificar el diccionario 'procesar' para que el 2º elemento
#invoque a la funcion restar con los parámetros correctos.

#Tarea3: Añadir función para multiplicar
#y modificar el diccionario 'procesar' para que el 3er elemento
#invoque a la funcion multipliar con los parámetros correctos.

#Tarea4: Añadir función para dividir
#y modificar el diccionario 'procesar' para que el 3er elemento
#invoque a la funcion dividir con los parámetros correctos.

#Tarea5: Modificar el programa para que el usuario pueda realizar
#tantas operaciones como quiera, hasta que indique que no necesita más.

#Tarea6: añadir la función 'prepara_operación', que lee los operandos
#n1 y n2, y muestra el menú en pantalla.
# recuerda que una función puede devolver varios valores: 
# return (a,b) #al final de la función
# c,f = prepara_operacion()	#en la llamada a la función


#Programa calculadora

print("Bienvenido al programa calculador.")

n1 = float( input("Introduce el primer número: ") )
n2 = float( input("Introduce el segundo número: ") )

#Muestra menú de opciones
	
print("Éstas son las opciones: ")
print("1) Sumar", n1, "+", n2,"")
print("2) Restar", n1, "-", n2,"")
print("3) Multiplicar", n1, "*", n2,"")
print("4) Dividir", n1, "/", n2,"")

#Asegura que introduce opción válida
opcion=0
while (opcion<1 or opcion>4):
	opcion = int( input("Introduce una opción entre 1 y 4: "))


#Según la opción introducida, realiza el cálculo correcto

print("\nHa elegido la opción", opcion, "->")

#En python no existe estructura SEGÚN como en pseudocodigo

#Creamos un diccionario (dict) para realizar la operación correcta
#cada elemento del diccionario es una pareja clave: valor
#las claves del diccionario serán los números de las opciones 1-4
#los valores del diccionario será la expresión a ejecutar 
procesar = { 
			1: '"{}+{}={}".format(n1, n2, n1+n2)',
			2: '"{}-{}={}".format(n1, n2, n1-n2)',
			3: '"{}*{}={}".format(n1, n2, n1*n2)',
			4: '"{}/{}={}".format(n1, n2, n1/n2)'
		}

#la función eval() ejecuta la instrucción contenida en el texto 
#que se le pasa como argumento
#En este caso, prepara el texto con el resultado de la operación
mensaje = eval(procesar[opcion])
print(mensaje)
