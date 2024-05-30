# Software Estadística

El programa permite al usuario ingresar datos numéricos por consola y luego seleccionar qué medida quiere calcular. Puede elegir entre medidas de posición, como media, mediana, moda y cuartiles, así como medidas de dispersión, como rango, varianza y desviación estándar, o también una tabla que muestra los datos del conjunto con sus respectivas frecuencias (absoluta, relativa, porcentual y sus acumuladas).
Este proyecto fue desarrollado por Agustín Bernasconi, Benjamín Briolini, Gastón Cáceres Garnica y Diego Luna, estudiantes de 2º año de la Tecnicatura de Desarrollo de Software del Instituto Superior Arturo Umberto Illia. El profesor a cargo es Luis Camposano, de la asignatura Matemática y Estadística Aplicada. El lenguaje utilizado fue Python.

## Uso

Para ejecutar este programa, sigue los siguientes pasos:
1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde su [página oficial](python.org) e instalarlo siguiendo las instrucciones proporcionadas.
2. Descarga el código fuente de este programa desde el repositorio de GitHub.
3. Abre una terminal en el directorio donde se encuentra el archivo `software_estadistica_v1.py`.
4. Ejecuta el programa utilizando el comando `python programa_estadistico.py`.
5. El programa te pedirá que ingreses los datos con los que quieres trabajar, debes ingresarlos simplemente separados por un espacio, y no de otra forma (como por ejemplo separados por coma o en formato lista).

> 1 2 3 4 5 # De esta forma SÍ

> 1, 2, 3, 4, 5 # De esta forma NO

> [1, 2, 3, 4, 5] # Así tampoco

6. Ya ingresados los datos, ingresarás al menú. Aquí, tendrás que elegir primero el tipo y luego qué medida quieres calcular, utilizando los números consignados en pantalla (1 al 4). Con el número 0 podrás volver atrás en el menú o salir del programa.
7. Cuando elijas una medida, el resultado se imprimirá en pantalla.
8. El programa permite seguir calculando otras funciones sin necesidad de iniciarlo nuevamente, por lo que puedes repetir los pasos 6 y 7 cuantas veces desees.

## Funcionamiento

A lo largo del código, se encontrarán con algunas etiquetas en formato #XXX (junto con una breve explicación de la línea o bloque), que referenciarán a una sección de este README con un desarrollo mayor para un mejor entendimiento de ciertas partes más complejas y para evitar la acumulación de tanto texto en el código fuente del programa.

#001: La librería typing en Python se utiliza para proporcionar un soporte opcional de tipo en Python 3. Aunque Python es un lenguaje de programación de tipado dinámico, lo que significa que no necesitas declarar explícitamente el tipo de una variable cuando la defines, la librería typing te permite agregar anotaciones de tipo opcional en tu código.
En este caso, la utilizamos para documentar los tipos de datos que toman las funciones como argumentos y los tipos de datos que retornan. Vale aclarar que esto se realiza con meros fines de documentación, ya que no realizan una verificación de ningún tipo.

#002: Tanto la función sorted() como el método sort() utilizan el algoritmo de ordenación Timsort, que es una combinación de Merge Sort e Insertion Sort. Timsort fue diseñado para ser rápido en datos del mundo real y ha sido el algoritmo de ordenación estándar en Python desde la versión 2.3.
El ordenamiento por inserción (o insertion sort) es una manera muy natural de ordenar para un ser humano y puede usarse fácilmente para ordenar un mazo de cartas. Es eficiente para listas pequeñas o casi ordenadas. El ordenamiento por mezcla (o merge sort) es un algoritmo de ordenación por comparación basado en el enfoque divide y vencerás. Es eficiente para listas grandes.
Se crea una lista nueva para no alterar la lista original.

#003: Se toma el cociente de la división entera de la cantidad de elementos sobre 2, independientemente de si la cantidad es par o impar. Esto se debe a que en ambos casos nos sirve el elemento alojado en ese índice. Esto se entenderá con las referencias #004 y #005.

#004: Si la lista tiene una cantidad de elementos par, la variable `mitad` toma como valor el índice de uno de los dos elementos (el del lado derecho) con los que se calcula la mediana; para acceder al otro (el del lado izquierdo), debemos calcular el índice anterior, es decir, `mitad - 1`.

#005: Si la lista tiene una cantidad de elementos impar, la variable `mitad` toma como valor el índice del valor central, es decir que este es la mediana misma.

#006: `list(lista.values()).count(max_frecuencia) == len(lista)` Se crea una lista con los valores del diccionario, para poder aplicarle el método count que cuenta las veces que figura un elemento con valor igual al pasado como parámetro, en este caso `max_frecuencia`. Si este número es igual a la longitud de la lista, o dicho de otra manera, si todos los números tienen la misma frecuencia, no hay moda y la función devuelve None.

#007: `[numero for numero, frecuencia in lista_ordenada.items() if frecuencia == max_frecuencia]` Se crea una lista por comprension cuyos elementos son el número o números guardados en el diccionario, que tienen la máxima frecuencia.

#008, #009: se utiliza la técnica de slicing, que tiene como formato `secuencia[inicio:fin:paso]`. Vale aclarar que el inicio está incluido, pero el fin queda excluido, por ende debemos sumarle 1 si queremos tenerlo en cuenta.
Para calcular Q1, si la longitud es par, hacemos slicing del inicio hasta la mitad (no incluida), por lo que queda perfectamente dividida en dos. Pero si la longitud es impar, debemos asegurarnos de incluir la mitad (mediana) para poder calcular correctamente.

#010: para calcular Q3, hacemos slicing desde el valor `mitad` hasta el final. El valor `mitad` sirve para cuando es par o impar, ya que en el primer caso, cuenta desde el valor siguiente a la mitad (recordemos que los índices arrancan a contar desde cero), y en el segundo caso, cuenta desde la mediana.

#011: se hace de esta manera para que si queremos trabajar con los datos de una línea de la tabla por separado, sea más fácil acceder a ellos.

#012: Las f-strings (formatted string literals) son una manera concisa y eficiente de incluir expresiones dentro de cadenas de texto en Python. Se introdujeron en Python 3.6 y permiten insertar variables y expresiones en una cadena, precedida por la letra f o F.
Las f-strings también permiten formatear valores utilizando una notación específica dentro de las llaves, lo que es muy útil para presentar datos de manera alineada o con un formato específico. La notación básica es `{valor:formato}`.
Cuando usamos `valor:x` como en numero:10, estamos pidiendo que el valor de número ocupe al menos x espacios.
Cuando usamos `valor:x.yf` como en frecuencia_relativa:7.4f, estamos pidiendo que el valor de frecuencia_relativa tenga 4 dígitos decimales y que ocupe 7 espacios.

#013: La función `input_int` recibe un argumento `prompt` que es un mensaje que se muestra al usuario. Se inicia un bucle `while True` para seguir solicitando entradas al usuario hasta que ingrese un número válido.
Luego, se comienza una secuencia try except. Esto se utiliza para manejar excepciones (errores) que puedan ocurrir durante la ejecución de un programa. El código dentro del bloque try se ejecuta normalmente, mientras que Python monitorea cualquier excepción que pueda ocurrir dentro de este bloque. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except, que especifica cómo manejar la excepción.
En este caso, cuando ingresa al bloque try, muestra el `prompt` al usuario y lee la entrada con `input()`. Luego, intenta convertir la entrada a un entero con `int()`. Si puede convertirlo, la función devuelve dicho número entero. En el caso de no poder convertirlo, sucede un `ValueError`, se le avisa al usuario mediante un mensaje en pantalla y el bucle comienza nuevamente, volviendo a pedirle que ingrese otro valor.

#014: La función `input_float_list` también recibe un argumento `prompt`. La lógica es similar que en la función anterior pero cambia el tipo de variable que se quiere devolver. En este caso, el usuario debe ingresar los números con los que desea trabajar, separados por espacios.
Luego, mediante el método `split()`, se divide el string ingresado utilizando el carácter ` ` (espacio) y se crea una lista de strings donde cada string es uno de los números. Ahora, intenta convertir cada elemento de la lista a un número flotante, utilizando una lista por comprensión. Si puede convertir **todos** los elementos de la lista, devuelve la lista de flotantes. Caso contrario, muestra el mensaje de error y vuelve a inicar el ciclo.