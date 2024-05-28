# Definición de funciones

from typing import List, Tuple, Dict

def media(lista: List[float]) -> float:
    suma = sum(lista)
    res_media = suma / len(lista)
    res_media_redondeado = round(res_media, 4)

    return res_media_redondeado

def mediana(lista: List[float]) -> float:
    lista_ordenada = sorted(lista)
    v_central = len(lista_ordenada) // 2

    if len(lista_ordenada) % 2 == 0:
        res_mediana = (lista_ordenada[v_central - 1] + lista_ordenada[v_central]) / 2
    else:
        res_mediana = lista_ordenada[v_central]

    return res_mediana
    
def moda(lista: Dict[float, int], lista_ordenada: Dict[float, int]) -> Tuple[List[float], float]:
    max_frecuencia = max(lista.values())
    
    if list(lista.values()).count(max_frecuencia) == len(lista):
        return None, None
    else:
        res_moda = [numero for numero, frecuencia in lista_ordenada.items() if frecuencia == max_frecuencia]
        return res_moda, max_frecuencia

def rango(lista: List[float]) -> float:
    lista_ordenada = sorted(lista)
    minimo = lista_ordenada[0]
    maximo = lista_ordenada[len(lista_ordenada) - 1]
    res_rango = maximo - minimo

    return res_rango

def varianza(lista: List[float]) -> float:
    sumatoria = 0
    for numero in lista:
        termino = (numero - media(lista)) ** 2
        sumatoria += termino

    res_varianza = sumatoria / (len(lista) - 1)
    res_varianza_redondeado = round(res_varianza, 4)

    return res_varianza_redondeado

def desviacion_estandar(lista: List[float]) -> float:
    res_desviacion_estandar = varianza(lista) ** 0.5
    res_desviacion_estandar_redondeado = round(res_desviacion_estandar, 4)

    return res_desviacion_estandar_redondeado

def cuartiles(lista: List[float]) -> Tuple[float, float, float]:
    lista_ordenada = sorted(lista)
    mitad = len(lista_ordenada) // 2

    if len(lista_ordenada) % 2 == 0:
        nros_izq = lista_ordenada[:mitad]
    else:
        nros_izq = lista_ordenada[:mitad+1]
    res_Q1 = mediana(nros_izq)

    res_Q2 = mediana(lista_ordenada)

    nros_der = lista_ordenada[mitad:]
    res_Q3 = mediana(nros_der)

    return res_Q1, res_Q2, res_Q3

def frecuencias(lista_ordenada: dict) -> list:
    can = sum(lista_ordenada.values())
    frecuencia_abs_acumulada = 0
    frecuencia_rel_acumulada = 0
    frecuencia_por_acumulada = 0
    filas = []

    for numero, frecuencia in lista_ordenada.items():
        frecuencia_relativa = (frecuencia / can)
        frecuencia_porcentual = (frecuencia / can) * 100
        frecuencia_abs_acumulada += frecuencia
        frecuencia_rel_acumulada += frecuencia_relativa
        frecuencia_por_acumulada += frecuencia_porcentual
        fila = f"{numero:10} | {frecuencia:2}  | {frecuencia_relativa:7.4f} | {frecuencia_porcentual:7.4f}% | {frecuencia_abs_acumulada:3}  | {frecuencia_rel_acumulada:7.4f}  | {frecuencia_por_acumulada:7.4f}%"
        filas.append(fila)

    return filas

# Funciones de validación de entrada

def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def input_float_list(prompt: str) -> List[float]:
    while True:
        try:
            input_data = input(prompt)
            return [float(x) for x in input_data.split()]
        except ValueError:
            print("Entrada inválida. Por favor, ingrese una lista de números separados por espacios.")

# Definición de variables globales

conteo = {}
conteo_ordenado = {}
nros = []

# Lógica principal

nros = input_float_list("Ingrese los datos separados por espacios: ")

for i in nros:
            if i in conteo:
                conteo[i] += 1
            else:
                conteo[i] = 1

claves_ordenadas = list(conteo.keys())
claves_ordenadas.sort()
for clave in claves_ordenadas:
     conteo_ordenado[clave] = conteo[clave]

while True:
    opcion_a = input_int("""\nSeleccione qué tipo de medida quiere calcular:
                       
    0 = Salir
    1 = Medidas de posición         
    2 = Medidas de dispersión  
                                        
Opción elegida: """)

    if opcion_a == 0:
        print("Cerrando aplicación")
        break

    elif opcion_a == 1:

        opcion_b = input_int("""\nSeleccione qué medida de posición quiere calcular:
                       
    0 = Volver
    1 = Media         
    2 = Mediana
    3 = Moda                           
                                        
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

            if res_moda is None:
                print("El conjunto no tiene moda, todos los valores tienen la misma frecuencia")
                input("Presione enter para continuar ")
            else:
                for valor in res_moda:
                    print("Moda:", valor)

                print("\nFrecuencia:", max_frecuencia)
                input("Presione enter para continuar ")

        else:
            print("Opción no válida, por favor seleccione una opción válida.")

    elif opcion_a == 2:

        opcion_b = input_int("""\nSeleccione qué medida de dispersión quiere calcular:
                       
    0 = Volver
    1 = Rango         
    2 = Varianza
    3 = Desviación estándar
    4 = Cuartiles
    5 = Tabla de frecuencias                       
                                        
Opción elegida: """)
        
        if opcion_b == 1:
            
            res_rango = rango(nros)
            print("\nRango:", res_rango)
            input("Presione enter para continuar ")

        elif opcion_b == 2:
            
            res_varianza = varianza(nros)
            print("\nVarianza:", res_varianza)
            input("Presione enter para continuar ")

        elif opcion_b == 3:
            
            res_desviacion_estandar = desviacion_estandar(nros)
            print("\nDesviación estándar:", res_desviacion_estandar)
            input("Presione enter para continuar ")

        elif opcion_b == 4:

            res_Q1, res_Q2, res_Q3 = cuartiles(nros)
            print("\nQ1 (25%):", res_Q1)
            print("Q2 (50%, mediana):", res_Q2)
            print("Q3 (75%):", res_Q3)
            input("Presione enter para continuar ")

        elif opcion_b == 5:

            tabla = "\nFrecuencias:" +\
                "\n   Número  | fi  |   fri   |  fri%    |  Fi  |   Fri    |   Fri%" +\
                "\n-------------------------------------------------------------------"
            print(tabla)

            filas = frecuencias(conteo_ordenado)
            for fila in filas:
                print(fila)

            input("\nPresione enter para continuar ")
        
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

    else:
        print("Opción no válida, por favor seleccione una opción válida.")