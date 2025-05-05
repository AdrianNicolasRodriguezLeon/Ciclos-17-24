
### TERCERA ENTREGRA ###
#  Estudiante: Adrian Nicolas Estiven Rodriguez Leon
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
       print("Opción no válida.")

