## Pedir un número y calcular su factorial.

numero = int(input("Dime de qué número quieres el factorial: "))
# Contador.
fact = 1
# Variable.
texto= f"{numero}!"
# Recorrido de cuenta atrás.
for i in range(numero, 0, -1):
    fact *= i
# Cadena de texto de la operación.
    if i == numero:
        texto += f" = {i}"
    else:
        texto += f" X {i}"
# Termino del bucle e impresión.
else:
    texto += f" = {fact}"
    print(texto)