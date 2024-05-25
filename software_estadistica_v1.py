# Definición de funciones

def frecuencias(lista_ordenada: dict) -> set:
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
        fila = f"{numero:6} | {frecuencia:2}  | {frecuencia_relativa:7.4f} | {frecuencia_porcentual:7.4f}% | {frecuencia_abs_acumulada:3}  | {frecuencia_rel_acumulada:7.4f}  | {frecuencia_por_acumulada:7.4f}%"
        filas.append(fila)

    return filas

def media(lista: list) -> float:
    suma = sum(lista)
    res_media = suma / len(lista)
    res_media_redondeado = round(res_media, 4)

    return res_media_redondeado

def mediana(lista: list) -> float:
    lista.sort()
    v_central = len(lista) // 2

    if len(lista) % 2 == 0:
        res = (lista[v_central - 1] + lista[v_central]) / 2
    else:
        res = lista[v_central]

    return res
    
def moda(lista: dict, lista_ordenada: dict) -> list:
    max_frecuencia = max(lista.values())
    res_moda = [numero for numero, frecuencia in lista_ordenada.items() if frecuencia == max_frecuencia]

    return res_moda, max_frecuencia

def cuartiles(lista: list) -> float:
    lista.sort()
    mitad = len(lista) // 2

    if len(lista) % 2 == 0:
        nros_izq = lista[:mitad]
    else:
        nros_izq = lista[:mitad+1]
    Q1 = mediana(nros_izq)

    Q2 = mediana(lista)

    nros_der = lista[mitad:]
    Q3 = mediana(nros_der)

    return Q1, Q2, Q3

# Definición de variables globales

conteo = {}
conteo_ordenado = {}
nros = []

# Lógica principal

can = int(input("Ingrese la cantidad de datos que quiere usar: "))
for i in range(can):
        nro = float(input("Ingrese el dato: "))
        nros.append(nro)

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
    opcion_a = int(input("""\nSeleccione qué tipo de medida quiere calcular:
                       
    0 = Salir
    1 = Medidas de posición         
    2 = Medidas de dispersión  
                                        
Opción elegida: """))

    if opcion_a == 0:
        print("Cerrando aplicación")
        break

    elif opcion_a == 1:

        opcion_b = int(input("""\nSeleccione qué medida de posición quiere calcular:
                       
    0 = Salir
    1 = Media         
    2 = Mediana
    3 = Moda                           
                                        
Opción elegida: """))
        
        if opcion_b == 1:

            res_media = media(nros) 
            print("\nLa media de estos datos es de " + str(res_media))
            input("Presione enter para continuar ")

        elif opcion_b == 2:

            res_mediana = mediana(nros)
            print("\nLa mediana es " + str(res_mediana))
            input("Presione enter para continuar ")

        elif opcion_b == 3:

            res_moda, max_frecuencia = moda(conteo, conteo_ordenado)
            print("")
            for valor in res_moda:
                print("Moda:", valor)

            print("\nFrecuencia:", max_frecuencia)
            input("Presione enter para continuar ")

        else:
            print("Opción no válida, por favor seleccione una opción válida.")

    elif opcion_a == 2:

        opcion_b = int(input("""\nSeleccione qué medida de dispersión quiere calcular:
                       
    0 = Salir
    1 = Rango         
    2 = Varianza
    3 = Desviación estándar
    4 = Cuartiles
    5 = Tabla de frecuencias                       
                                        
Opción elegida: """))
        
        if opcion_b == 1:
            pass # hacer rango

        elif opcion_b == 2:
            pass # hacer varianza

        elif opcion_b == 3:
            pass # hacer desviación

        elif opcion_b == 4:

            res_Q1, res_Q2, res_Q3 = cuartiles(nros)
            print(f"\nQ1 (25%): {res_Q1}")
            print(f"Q2 (50%, mediana): {res_Q2}")
            print(f"Q3 (75%): {res_Q3}")
            input("Presione enter para continuar ")

        elif opcion_b == 5:

            tabla = "\nFrecuencias:" +\
                "\nNúmero | fi  |   fri   |  fri%    |  Fi  |   Fri    |   Fri%" +\
                "\n---------------------------------------------------------------"
            print(tabla)

            filas = frecuencias(conteo_ordenado)
            for fila in filas:
                print(fila)

            input("\nPresione enter para continuar ")
        
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

    else:
        print("Opción no válida, por favor seleccione una opción válida.")





        
    
