def claGrade(grade):
    try:
         if grade <= 69:
             return("Aprendizaje inicial")
         elif grade <=79:
            return("Aprendizaje fundamental")
         elif grade <=89:
             return("Aprendizaje satisfactorio")
         elif grade <= 100:
             return("Aprendizaje avanzado")
    except ValueError:
        print("Ingrese la nota en numeros, no en letras")


