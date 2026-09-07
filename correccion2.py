def calcular_comision(venta):  # venta es el parámetro
    return venta * 0.05


comision = calcular_comision(8000)  # 8000 es el argumento
print(comision)

def aplicar_aumento(precio):
    precio = precio + 100
    print("Precio dentro:", precio)


precio_producto = 500
aplicar_aumento(precio_producto)

print("Precio fuera:", precio_producto)

def agregar_producto(inventario, producto):
    inventario.append(producto)


productos = ["arroz", "aceite"]
agregar_producto(productos, "café")

print(productos)