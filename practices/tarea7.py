#Integrantes del equipo: 
#Charly Joshua Sandoval Hernández.
#Edgar Axel Sandoval Hernández.
# Diccionario que representa un programa en el que cada clave es una instrucción con su contenido
programa = {
    0: "cargar 1, 2",
    1: "sumar 1, 2, 3",
    2: "imprimir 3"
}

# Diccionario que almacena las variables y sus valores inicializados en 0
variables = {
    "a": 0,
    "b": 0,
    "c": 0
}

# Lista de instrucciones que se ejecutarán secuencialmente
instrucciones = [
    "cargar 1, 2",
    "sumar 1, 2, 3",
    "imprimir 3"
]

# Bucle que recorre cada instrucción en la lista de instrucciones
for instruccion in instrucciones:
    # Verifica si la instrucción es del tipo "cargar"
    if instruccion.startswith("cargar"):
        # Divide la instrucción en una lista separada por espacio
        instruccion = instruccion.split(" ")
        # Verifica que haya más de una parte después de dividir
        if len(instruccion) > 1:
            # Divide los argumentos de la instrucción por la coma
            args = instruccion[1].split(",")
            # Verifica que haya exactamente dos argumentos
            if len(args) == 2:
                # Limpia los espacios en blanco alrededor de los argumentos
                arg1, arg2 = args[0].strip(), args[1].strip()
                # Convierte el primer argumento en entero y lo asigna como valor de la variable indicada por el segundo argumento
                variables[arg2] = int(arg1)
    # Verifica si la instrucción es del tipo "sumar"
    elif instruccion.startswith("sumar"):
        # Divide la instrucción en una lista separada por espacio
        instruccion = instruccion.split(" ")
        # Verifica que haya más de una parte después de dividir
        if len(instruccion) > 1:
            # Divide los argumentos de la instrucción por la coma
            args = instruccion[1].split(",")
            # Verifica que haya exactamente tres argumentos
            if len(args) == 3:
                # Limpia los espacios en blanco alrededor de los argumentos
                arg1, arg2, arg3 = args[0].strip(), args[1].strip(), args[2].strip()
                # Suma los valores de las dos primeras variables y asigna el resultado a la tercera
                variables[arg3] = variables[arg1] + variables[arg2]
    # Verifica si la instrucción es del tipo "imprimir"
    elif instruccion.startswith("imprimir"):
        # Divide la instrucción en una lista separada por espacio
        instruccion = instruccion.split(" ")
        # Verifica que haya más de una parte después de dividir
        if len(instruccion) > 1:
            # Obtiene el nombre de la variable a imprimir
            variable = instruccion[1].strip()
            # Verifica si la variable existe en el diccionario de variables
            if variable in variables:
                # Imprime el valor de la variable
                print(variables[variable])

# Imprime los valores finales de todas las variables
print("\nResultados finales de las variables:")
for var, value in variables.items():
    # Imprime cada variable con su valor final
    print(f"{var}: {value}")

