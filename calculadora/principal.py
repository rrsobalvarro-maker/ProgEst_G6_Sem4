import aritmetica as arit

def menu():
    print("Bienvenido a Mi calucaldora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Division")
    print("0. Salir")

    op = int(input("Digita el # de la opcion que desea usar: "))
    return op

def showAdd(num1, num2):
        print(f"La suma de {num1} + {num2} es {arit.add(num1, num2)}")

    
def showsSub(num1, num2):
        print(f"La diferencia de {num1} - {num2} es {arit.sub(num1, num2)}")

    
def showMult(num1, num2):
        print(f"El producto de {num1} * {num2} es {arit.mult(num1, num2)}")

    
def showDiv(num1, num2):
        print(f"La division de {num1} / {num2} es {arit.div(num1, num2)}")

def ReadValues():
       num1=float(input("Digita el primer valor: "))
       num2=float(input("Digita el segundo valor: "))
       return num1, num2

def ChooseOp(op):
       if op == 1:
              num1, num2 = ReadValues()
              showAdd(num1, num2)
       elif op == 2:
              num1, num2 = ReadValues()
              showsSub(num1, num2)
       elif op == 3:
              num1, num2 = ReadValues()
              showMult(num1, num2)
       elif op == 4:
              num1, num2 = ReadValues()
              showDiv(num1, num2)
       elif op == 0: 
              print("Adios...")
              
       else:
              print("Opcion Invalida")

def main():
       while True:
              op = menu()
              ChooseOp(op)
              if op == 0: break
main()
