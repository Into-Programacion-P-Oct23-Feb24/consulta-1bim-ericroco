#Para usar condicionales es mucho mas sencillo que en java si seguimos el siguiente formato
num = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
if num > num2:
    print("El numero 1 es mayor que el numero 2")
else:
    print("El numero 2 es mayor que el numero 1")
#Tambien podemos utilizar el else if por si queremos agregar otra condicion
dia = input("¿Que tal estuvo tu dia? ")
dia.lower()
if (dia == "bien"):
    print("me alegro")
elif (dia == "normal"):
    print("por lo menos no fue peor")
elif (dia == "mal"):
    print("espero que mañana sea mejor")