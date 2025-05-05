
### TERCERA ENTREGRA ###
#  Estudiante: Adrian Nicolas Estiven Rodriguez Leon
print ("  ")
print("18. Suma de 100 números")
print(" ")
numero = int(input("Ingresa un número entero: "))
i = 1
suma = 0
while i <= 100:
    suma += numero + i
    i += 1
print("La suma de los 100 números siguientes a", numero,  "es:", suma)
print ("  ")
print("19. Conversion")
print(" ")
tasa_conversion = 1.14  
opcion = int(input("Escribe 1 para convertir euros a dólares: "))
while opcion == 1:
    euros = float(input("Ingresa la cantidad en euros: "))
    dolar = euros * tasa_conversion
    print ( "los " , euros,  "euros equivalen a", dolar, "dólares.")
    opcion = int(input("¿Deseas convertir otra cantidad? escribe 1 si quieres continuar: "))
    if opcion != 1:
       print("Cerrando Programa 'Convertidor'... .")

print(" ")
print("20. Area de un rectángulo")
print(" ")
opcion = 1

while opcion == 1:
    altura = float(input("Ingresa la altura del rectángulo: "))
    anchura = float(input("Ingresa la anchura del rectángulo: "))
    area = altura * anchura
    print("El área del rectángulo es: ", area)
    opcion = input(" Escribe '1' si deseas calcular otravez el area del rectangulo: ")
    if opcion != 1:
        print("Cerrando Programa 'Area'...")
print(" ")
print("21. Comparacion de dos numeros")
print(" ")
opcion = 1
while opcion == 1:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    if num1 > num2:
        print("El mayor es: ",num1)
        print("El menor es: ",num2)
    if num2 > num1:
        print("El mayor es:" ,num2)
        print("El menor es: ", num1)
    if num1 == num2:
        print("Ambos números son iguales.")
    opcion = int(input("Escribe '1' si deseas comparar otro par de números: "))
    if opcion != 1:
        print("Cerrando Programa 'Comparador'...")
print(" ")
print("22. Numeros Impares")
print(" ")
numero2 = int(input("Ingresa un número entero: "))

print("Números impares menores que ", numero2, ":")
for i in range(1, numero2, 2):
    print(i)
print("Cerrando Programa 'Impares'...")

print(" ")
print("23. Algoritmo de Euclides")
print(" ")
opcion = 1
while opcion == 1:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    original_a, original_b = a, b  
    while b != 0:
        a, b = b, a % b
    print("El máximo común divisor de ", original_a, "y ", original_b, " es: ", a)
    opcion = input("Escribe '1' si deseas calcular el MCD de otros  números: ")
print("Cerrando Programa Eculides ...")
print(" ")
print("24. Ecuación cuadrática")
print(" ")
opcion = 1
while opcion == 1:
        a = float(input("Ingresa el coeficiente a diferente de 0): "))
        if a != 0:

            b = float(input("Ingresa el coeficiente b: "))
            c = float(input("Ingresa el coeficiente c: "))

            discriminante = b**2 - 4 * a * c

            if discriminante > 0:
                x1 = (-b + discriminante**0.5) / (2 * a)
                x2 = (-b - discriminante**0.5) / (2 * a)
                print("Dos soluciones reales: x1 = ", x1 , x2 )
            if discriminante == 0:
                x = -b / (2 * a)
                print("Una única solución real: x = ", x)
            if discriminante < 0:
                print("No tiene soluciones reales.")
                
        else:
            print("El coeficiente 'a' no puede ser 0 en una ecuación cuadrática.")

        opcion = int(input(" Escribe '1' si deseas calcular otra ecuación cuadrática: "))
