conteo = {}
conteo_ordenado = {}
nros = []

def mediana(lista: set) -> float:
    lista.sort()
    v_central = len(lista) // 2

    if len(lista) % 2 == 0:
        res = (lista[v_central - 1] + lista[v_central]) / 2
    else:
        res = lista[v_central]

    return res
    
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
    opcion = int(input("""\nSeleccione qué desea realizar:
    0 = Salir
    1 = Frecuencias                   
    2 = Media
    3 = Mediana
    4 = Moda
    5 = Cuartiles                   
Opción elegida: """))

    if opcion == 0:
        print("Cerrando aplicación")
        break

    elif opcion == 1:
        frecuencia_abs_acumulada = 0
        frecuencia_rel_acumulada = 0
        frecuencia_por_acumulada = 0

        print("\nFrecuencias:")
        print(" Número | fi  |   fri   |  fri%    |  Fi  |   Fri    |   Fri%  ")
        print("--------------------------------------------------------------")

        for numero, frecuencia in conteo_ordenado.items():
                  frecuencia_relativa = (frecuencia / can) 
                  frecuencia_porcentual = (frecuencia / can) * 100 
                  frecuencia_abs_acumulada += frecuencia 
                  frecuencia_rel_acumulada += frecuencia_relativa 
                  frecuencia_por_acumulada += frecuencia_porcentual 
                  print(f"{numero:6}  | {frecuencia:2}  | {frecuencia_relativa:7.4f} | {frecuencia_porcentual:7.4f}% | {frecuencia_abs_acumulada:3}  | {frecuencia_rel_acumulada:7.4f}  | {frecuencia_por_acumulada:7.4f}%")

        input("Presione enter para continuar ")      
            
    elif opcion == 2:

        suma = sum(nros)
        media = suma / can
        print("\nLa media de estos datos es de " + str(media))
        input("Presione enter para continuar ")

    elif opcion == 3:  
        res_mediana = mediana(nros)

        print("\nLa mediana es " + str(res_mediana))
        input("Presione enter para continuar ")

    elif opcion == 4:
        moda = []
        # Se calcula cual es el valor más alto
        max_frecuencia = max(conteo.values())

        # Se hace un for en el diccionario buscando cuales son los números con mayor frecuencia.

        # Forma N*1
        moda = [numero for numero, frecuencia in conteo_ordenado.items() if frecuencia == max_frecuencia]

        print("\nLa moda es", moda, "\nLa frecuencia es:", max_frecuencia)
        input("Presione enter para continuar ")

    elif opcion == 5:
        nros.sort()
        mitad = can // 2

        # Calcular Q1
        if can % 2 == 0:
            nros_izq = nros[:mitad]
        else:
            nros_izq = nros[:mitad+1]
    
        Q1 = mediana(nros_izq)   

        # Calcular Q2 (Mediana)
        Q2 = mediana(nros)

        # Calcular Q3
        nros_der = nros[mitad:]

        Q3 = mediana(nros_der)

        print(f"\nQ1 (25%): {Q1}")
        print(f"Q2 (50%, mediana): {Q2}")
        print(f"Q3 (75%): {Q3}")
        input("Presione enter para continuar ")

    elif opcion == 6: # Desvio estandar, varianza, rango...
        pass
    
    else:
        print("Opción no válida, por favor seleccione una opción válida.")
        