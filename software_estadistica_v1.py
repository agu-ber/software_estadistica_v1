# Definición de funciones

from typing import List, Tuple, Dict #001: se importa la librería typing para documentar mejor las funciones

def media(lista: List[float]) -> float: # La función recibe una lista de números flotantes y devuelve un número flotante
    suma = sum(lista) # Suma los elementos de la lista
    res_media = suma / len(lista)
    res_media_redondeado = round(res_media, 4) # Redondea a 4 decimales

    return res_media_redondeado # Retorna la media redondeada

def mediana(lista: List[float]) -> float:
    lista_ordenada = sorted(lista) #002: se crea una lista nueva con los elementos ordenados 
    mitad = len(lista_ordenada) // 2 #003: se toma la división entera de la longitud de la lista por 2

    if len(lista_ordenada) % 2 == 0: # Si la cantidad de elementos de la lista es par
        res_mediana = (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2 #004: La mediana es la suma de los elementos centrales dividido 2
    else: # Si la cantidad de elementos es impar
        res_mediana = lista_ordenada[mitad] #005: La mediana es el valor central

    return res_mediana # Retorna la mediana
    
def moda(lista: Dict[float, int], lista_ordenada: Dict[float, int]) -> Tuple[List[float], float]: # La función recibe dos diccionarios con claves flotantes y valores enteros, y devuelve una tupla que contiene una lista de flotantes y un flotante
    max_frecuencia = max(lista.values()) # Se calcula la frecuencia absoluta máxima de los números de la lista
    
    if list(lista.values()).count(max_frecuencia) == len(lista): #006: si todos los valores tienen la misma frecuencia
        res_moda = None # No existe la moda, es decir, es igual a vacío
    else: # Si existe moda (ya sea simple o múltiple)
        res_moda = [numero for numero, frecuencia in lista_ordenada.items() if frecuencia == max_frecuencia] #007: Se calcula una lista con la moda o modas
    
    return res_moda, max_frecuencia # Retorna el valor o los valores de la moda con su respectiva frecuencia absoluta
    
def cuartiles(lista: List[float]) -> Tuple[float, float, float]: # La función recibe una lista de flotantes y devuelve una tupla de tres flotantes
    lista_ordenada = sorted(lista)
    mitad = len(lista_ordenada) // 2 # Bajo la misma lógica que en la mediana, se calcula el medio

    if len(lista_ordenada) % 2 == 0:
        nros_izq = lista_ordenada[:mitad] #008: se toma la mitad izquierda del conjunto
    else:
        nros_izq = lista_ordenada[:mitad+1] #009: se toma la mitad izquierda más la mediana
    res_Q1 = mediana(nros_izq) # Para Q1, se calcula la mediana de este subconjunto

    res_Q2 = mediana(lista_ordenada) # Q2 es el mismo valor que la mediana

    nros_der = lista_ordenada[mitad:] #010: se toma la mitad derecha del conjunto (se incluye la mediana si la longitud es impar)
    res_Q3 = mediana(nros_der) # Para Q3, se calcula la mediana de este subconjunto

    return res_Q1, res_Q2, res_Q3 # Retorna los valores de los cuartiles

def rango(lista: List[float]) -> float:
    lista_ordenada = sorted(lista)
    minimo = lista_ordenada[0] # El valor mínimo es el primero de la lista
    maximo = lista_ordenada[len(lista_ordenada) - 1] # El valor máximo es el último de la lista
    res_rango = maximo - minimo

    return res_rango # Retorna el valor del rango

def varianza(lista: List[float]) -> float:
    sumatoria = 0
    for numero in lista:
        termino = (numero - media(lista)) ** 2 # Calcula el cuadrado de Xi menos la media
        sumatoria += termino

    if len(lista) != 1:
        res_varianza = sumatoria / (len(lista) - 1) # n-1
        res_varianza_redondeado = round(res_varianza, 4)
    else: # Si hay solo un elemento, no hay varianza
        res_varianza_redondeado = None

    return res_varianza_redondeado # Retorna la varianza redondeada

def desviacion_estandar(lista: List[float]) -> float:
    if len(lista) != 1:
        res_desviacion_estandar = varianza(lista) ** 0.5 # Calcula la raíz cuadrada de la varianza
        res_desviacion_estandar_redondeado = round(res_desviacion_estandar, 4)
    else: # Si hay un solo elemento, no hay desviación
        res_desviacion_estandar_redondeado = None

    return res_desviacion_estandar_redondeado # Retorna la desviación estándar redondeada

def frecuencias(lista_ordenada: dict) -> list:
    can = sum(lista_ordenada.values()) # Calcula la cantidad de elementos
    frecuencia_abs_acumulada = 0
    frecuencia_rel_acumulada = 0
    frecuencia_por_acumulada = 0
    filas = [] #011: creo una lista para almacenar cada fila de la tabla

    for numero, frecuencia in lista_ordenada.items(): # Se calculan los distintos tipos de frecuencias
        frecuencia_relativa = (frecuencia / can)
        frecuencia_porcentual = (frecuencia / can) * 100
        frecuencia_abs_acumulada += frecuencia
        frecuencia_rel_acumulada += frecuencia_relativa
        frecuencia_por_acumulada += frecuencia_porcentual
        #012: se crea el formato para cada línea usando f-strings
        fila = f"{numero:10} | {frecuencia:2}  | {frecuencia_relativa:7.4f} | {frecuencia_porcentual:7.4f}% | {frecuencia_abs_acumulada:3}  | {frecuencia_rel_acumulada:7.4f}  | {frecuencia_por_acumulada:7.4f}%"
        filas.append(fila) # Se agrega cada línea a la lista

    return filas # Retorna la lista con las líneas de la tabla

# Funciones de validación de entrada

def input_int(prompt: str) -> int: #013: Función que verifica que se ingrese un entero en la sección del menú
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def input_float_list(prompt: str) -> List[float]: #014: Función que verifica que se ingrese una lista de flotantes al inicio
    while True:
        try:
            input_data = input(prompt)
            return [float(x) for x in input_data.split()]
        except ValueError:
            print("Entrada inválida. Por favor, ingrese una lista de números separados por espacios.")

# Definición de variables globales

# Estas tres variables serán las utilizadas a lo largo de todo el programa y las que recibirán las funciones
conteo = {} # Diccionario con los números y sus respectivas frecuencias
conteo_ordenado = {} # Ordenado de forma ascendente
nros = [] # Lista con los números ingresados por el usuario

# Lógica principal

nros = input_float_list("Ingrese los datos separados por espacios: ")

for i in nros: # Cuenta la frecuencia absoluta de cada número
            if i in conteo:
                conteo[i] += 1
            else:
                conteo[i] = 1

claves_ordenadas = list(conteo.keys()) # Crea una lista con las claves del diccionario 'conteo'
claves_ordenadas.sort()
for clave in claves_ordenadas:
     conteo_ordenado[clave] = conteo[clave] # A cada número le asigna su frecuencia

while True: # Mientras no se rompa el ciclo
    opcion_a = input_int("""\nSeleccione qué tipo de medida quiere calcular:
                       
    0 = Salir
    1 = Medidas de posición         
    2 = Medidas de dispersión
    3 = Tabla de frecuencias  
                                        
Opción elegida: """)

    if opcion_a == 0:
        print("Cerrando aplicación")
        break # Se rompe el ciclo while

    elif opcion_a == 1:

        opcion_b = input_int("""\nSeleccione qué medida de posición quiere calcular:
                       
    0 = Volver
    1 = Media         
    2 = Mediana
    3 = Moda
    4 = Cuartiles                          
                                        
Opción elegida: """)
        
        if opcion_b == 1:

            res_media = media(nros) 
            print("\nMedia:", res_media)
            input("Presione enter para continuar ")

        elif opcion_b == 2:

            res_mediana = mediana(nros)
            print("\nMediana:", res_mediana)
            input("Presione enter para continuar ")

        elif opcion_b == 3:

            res_moda, max_frecuencia = moda(conteo, conteo_ordenado)
            print("")

            if res_moda == None: # Si no hay moda
                print(f"El conjunto no tiene moda, todos los valores tienen frecuencia {max_frecuencia}")
                input("Presione enter para continuar ")
            else:
                for valor in res_moda:
                    print("Moda:", valor)

                print("\nFrecuencia:", max_frecuencia)
                input("Presione enter para continuar ")
        
        elif opcion_b == 4:

            res_Q1, res_Q2, res_Q3 = cuartiles(nros)
            print("\nQ1 (25%):", res_Q1)
            print("Q2 (50%, mediana):", res_Q2)
            print("Q3 (75%):", res_Q3)
            input("Presione enter para continuar ")

        else:
            print("Opción no válida, por favor seleccione una opción válida.")

    elif opcion_a == 2:

        opcion_b = input_int("""\nSeleccione qué medida de dispersión quiere calcular:
                       
    0 = Volver
    1 = Rango         
    2 = Varianza
    3 = Desviación estándar                       
                                        
Opción elegida: """)
        
        if opcion_b == 1:
            
            res_rango = rango(nros)
            print("\nRango:", res_rango)
            input("Presione enter para continuar ")

        elif opcion_b == 2:
            
            res_varianza = varianza(nros)

            if res_varianza:
                print("\nVarianza:", res_varianza)
            else:
                print("\nEl conjunto no tiene varianza")
            input("Presione enter para continuar ")

        elif opcion_b == 3:
            
            res_desviacion_estandar = desviacion_estandar(nros)

            if res_desviacion_estandar:
                print("\nDesviación estándar:", res_desviacion_estandar)
            else:
                print("\nEl conjunto no tiene desviación estándar")
            input("Presione enter para continuar ")
        
        else:
            print("Opción no válida, por favor seleccione una opción válida.")
    
    elif opcion_a == 3:

        # Se crean las columnas de la tabla
        tabla = "\nFrecuencias:" +\
            "\n   Número  | fi  |   fri   |  fri%    |  Fi  |   Fri    |   Fri%" +\
            "\n-------------------------------------------------------------------"
        print(tabla)

        filas = frecuencias(conteo_ordenado)
        for fila in filas:
            print(fila) # Se imprime cada valor de la lista, o sea cada línea de la tabla

        input("\nPresione enter para continuar ")

    else:
        print("Opción no válida, por favor seleccione una opción válida.")