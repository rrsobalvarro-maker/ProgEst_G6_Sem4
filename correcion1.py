def calcular_pago(horas, tarifa):
    global pago #Hay que definir la variable pago como global
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)


calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
# print(pago)