''''
El Operador Ternario también conocido como expresión condicional en Python,
nos permite acceder a una de dos opciones a partir de una condición
Su sintaxis es a siguiente: opcion_1 if condición else opcion_2
'''

''' 
El truco o magia es evaluar primero la condicion si es verdadera será la opcion_1 
caso contrario sera la opcion_2
'''
edad = 18
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)


num1 = 10
num2 = 15
maximo = num1 if num1 > num2 else num2
print(maximo)


numero = 7
resultado = "par" if numero % 2 == 0 else "impar"
print(f"El número {numero} es {resultado}.")


sexo = "M"
respuesta_sexo = "Masculino" if (sexo == "M") else "Femenino"
print(f"Soy {sexo}")


numero = -10
resultado = "positivo" if numero >= 0 else "negativo"
print(f"El número {numero} es {resultado}.")


calificacion = 75
resultado = "Aprobado" if calificacion >= 60 else "Reprobado"
print(f"El estudiante ha {resultado} con una calificación de {calificacion}.")
