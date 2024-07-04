#Ejercicio 2: empresa de ventas de productos tecnológicos “Chispa Divertida”

print("Ingrese los siguientes datos para realizar su compra. \nTodos los datos son obligatorios.")
while True:
    nom = input("Ingrese su nombre: ")
    telef = input("Ingrese su número de telefono o celular: ")
    print("Ingrese producto y cantidad")
    product = input("Nombre del producto: ")
    Cantidad = input("Cantidad: ")

    print(input("¿Esta seguro que desea pagar?  ('s' o 'n')").lower())
    if nom == "" or telef == "" or product == "" or Cantidad == "":
        print("Faltan datos por ingresar. Por favor chequee la información ingresada.")
        print(f"Nombre: {nom}")
        print(f"Teléfono: {telef}")
        print(f"Producto: {product}")
        print(f"Cantidad: {Cantidad}")
        print("")
        print("Vuelva a comenzar")
    else:
        print("")
        print("La compra se ha realizado con éxito. Muchas gracias por su compra.")
        print("")
    

    

