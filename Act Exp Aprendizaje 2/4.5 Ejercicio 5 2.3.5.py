"""La pizzeria Cesar’s Pizza, contiene una variada gama de pizzas para
escoger. La pizzeria se caracteriza por tener una atención rápida y
mantener sus precios más bajos que la competencia.
La gerencia le solicita realizar un programa que permita calcular los
costos del pedido con sus respectivos valores del neto, impuesto y total.
El algoritmo es el siguiente. Una vez que usted lo terminó, se da cuenta
que podría mejorar el código de la asignación de los valores de las
pizzas, puesto que hay varias pizzas con el mismo precio."""

print("")
print("Bienvenido a Cesar's Pizza")
print("Menu:")
print("1.- PEPPERONI")
print("2.- QUESO")
print("3.- JAMÓN")
print("4.- 4N1")
print("5.- HULA HAWAIIAN")
print("6.- ULTIMATE SUPREME")
print("7.- VEGGIE")
print("8.- 3 MEAT TREAT")
print("9.- SUPER CHEESE 4N1")
print("10.- CHICKEN BBQ")
print("")
opcion = input("Elija su pizza. Ingrese el número de la pizza deseada: ")
cantidad = int(input("¿Cuantas pizzas desea?: "))

if opcion == "1":
    precio1 = 6000
    pizza1 = precio1 * cantidad
    ivapizza1 = pizza1 *1.19
    total1 = pizza1 + ivapizza1

    print(f"Precio neto: {pizza1}")
    print(f"Precio iva: {ivapizza1}")
    print(f"Total: {total1}")

elif opcion == "2":
    precio2 = 7000
    pizza2 = precio2 * cantidad
    ivapizza2 = pizza2 *1.19
    total2 = pizza2 + ivapizza2

    print(f"Precio neto: {pizza2}")
    print(f"Precio iva: {ivapizza2}")
    print(f"Total: {total2}")

elif opcion == "3":
    precio3 = 8000
    pizza3 = precio3 * cantidad
    ivapizza3 = pizza3 *1.19
    total3 = pizza3 + ivapizza3

    print(f"Precio neto: {pizza3}")
    print(f"Precio iva: {ivapizza3}")
    print(f"Total: {total3}")

elif opcion == "4":
    precio4 = 10000
    pizza4 = precio4 * cantidad
    ivapizza4 = pizza4 *1.19
    total4 = pizza4 + ivapizza4

    print(f"Precio neto: {pizza4}")
    print(f"Precio iva: {ivapizza4}")
    print(f"Total: {total4}")

elif opcion == "5":
    precio5 = 9000
    pizza5 = precio5 * cantidad
    ivapizza5 = pizza5 *1.19
    total5 = pizza5 + ivapizza5

    print(f"Precio neto: {pizza5}")
    print(f"Precio iva: {ivapizza5}")
    print(f"Total: {total5}")

elif opcion >= "6":
    precio6 = 11000
    pizza6 = precio6 * cantidad
    ivapizza6 = pizza6 *1.19
    total6 = pizza6 + ivapizza6

    print(f"Precio neto: {pizza6}")
    print(f"Precio iva: {ivapizza6}")
    print(f"Total: {total6}")

elif opcion >= "7":
    precio7 = 12250
    pizza7 = precio7 * cantidad
    ivapizza7 = pizza7 *1.19
    total7 = pizza7 + ivapizza7

    print(f"Precio neto: {pizza7}")
    print(f"Precio iva: {ivapizza7}")
    print(f"Total: {total7}")

elif opcion >= "8":
    precio8 = 13000
    pizza8 = precio8 * cantidad
    ivapizza8 = pizza8 *1.19
    total8 = pizza8 + ivapizza8

    print(f"Precio neto: {pizza8}")
    print(f"Precio iva: {ivapizza8}")
    print(f"Total: {total8}")

elif opcion >= "9":
    precio9 = 14500
    pizza9 = precio9 * cantidad
    ivapizza9 = pizza9 *1.19
    total9 = pizza9 + ivapizza9

    print(f"Precio neto: {pizza9}")
    print(f"Precio iva: {ivapizza9}")
    print(f"Total: {total9}")

elif opcion >= "10":
    precio10 = 6000
    pizza10 = precio10 * cantidad
    ivapizza10 = pizza10 *1.19
    total10 = pizza10 + ivapizza10

    print(f"Precio neto: {pizza10}")
    print(f"Precio iva: {ivapizza10}")
    print(f"Total: {total10}")