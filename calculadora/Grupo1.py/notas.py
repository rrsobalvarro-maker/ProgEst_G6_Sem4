import funciones as fun

def menu():
    print("Bienvenido a registro")
    print("1. Ingresar nota")
    print("2. Mostrar todas las notas")
    print("3. Salir")

    op = int(input("Ingrese la opcion # que quiere usar: "))
    return op

def showGrade(grade):
    print(f"Su nota {grade} representa un {fun.claGrade(grade)}")

def readGrades():
    grade = float(input("Ingrese la nota obtenida: "))
    return grade


def ChooseOp(op, grades):
    try:
        if op == 1: 
            grade = readGrades()
            grades.append(grade)
            showGrade(grade)
        elif op == 2:
            print("Nota registrada")
            if len(grades) == 0:
                print("No hay notas registradas")
            else:
                for grade in grades:
                    print(grade)
        elif op == 3:
            print("Gracias por usar, adios...")
        else:
            print("Opcion invalida")
    except ValueError:
        print("Ingrese la opcion en numeros, no en letra.")

def main():
    grades = []
    while True:
        op = menu()
        ChooseOp(op, grades)
        if op == 3: break
main()