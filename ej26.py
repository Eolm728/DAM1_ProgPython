cesta_compra = input("Ingrese los productos de la cesta de compra separados por comas: ")
productos = cesta_compra.split(',')
for producto in productos:
    print(producto.strip())