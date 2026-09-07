def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)


calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
# print(pago)

ventas_registradas = 0


def registrar_venta():
    global ventas_registradas
    ventas_registradas += 1
    print("Venta registrada")


registrar_venta()
registrar_venta()

print("Total de ventas:", ventas_registradas)

def procesar_venta(subtotal):
    def calcular_iva():
        return subtotal * 0.15

    iva = calcular_iva()
    return subtotal + iva


total = procesar_venta(2000)
print("Total: C$", total)

# calcular_iva() no está disponible fuera de procesar_venta.

saldo = 5000

def mostrar_saldo():
    saldo = 1200
    print(saldo)

mostrar_saldo()
print(saldo)