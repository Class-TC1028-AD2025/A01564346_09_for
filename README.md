 
# Bucle `for` en Python

El bucle `for` en Python en una herramienta fundamental para automatizar tareas repetitivas en tus programas.

## ¿Qué es el bucle `for`?

El bucle `for` se usa para **iterar** sobre una secuencia de elementos. Piensa en él como una forma de decirle a tu programa: "para cada elemento en esta lista, haz algo". Las secuencias pueden ser listas, tuplas, diccionarios, cadenas de texto, o incluso un rango de números.

### Sintaxis básica

La sintaxis del bucle `for` es muy simple y fácil de leer:

``` Python
for elemento in secuencia:
    # Código que se ejecutará en cada iteración
    # Este bloque debe estar indentado
```

* **`for`**: Palabra clave que inicia el bucle.

* **`elemento`**: Una variable temporal que toma el valor de cada ítem en la secuencia durante cada iteración.

* **`in`**: Palabra clave que especifica la secuencia sobre la cual se iterará.

* **`secuencia`**: La colección de elementos (lista, tupla, etc.) que el bucle recorrerá.

***

## 5 Ejemplos Prácticos

### Ejemplo 1: Iterando sobre una lista de números

Este es el uso más común. Aquí, el bucle `for` recorre cada número en la lista `calificaciones` y lo imprime en pantalla.

``` Python
calificaciones = [85, 92, 78, 100, 88]

print("Mis calificaciones son:")
for calificacion in calificaciones:
    print(calificacion)

```

***

### Ejemplo 2: Iterando sobre una cadena de texto

Una cadena de texto (`string`) es una secuencia de caracteres. Puedes usar `for` para procesar cada carácter de un mensaje.

``` Python
mensaje = "Hola Mundo"

print("Separando el mensaje:")
for caracter in mensaje:
    print(caracter)

```

***

### Ejemplo 3: Usando `range()` para iterar un número específico de veces

La función `range()` es muy útil para generar una secuencia de números. Esto te permite ejecutar un bloque de código un número fijo de veces.

* **`range(5)`**: Genera una secuencia de 0 a 4 (excluyendo el 5).

* **`range(2, 7)`**: Genera una secuencia de 2 a 6.

* **`range(10, 0, -2)`**: Genera una secuencia descendente de 10 a 2, en pasos de 2.

``` Python
# Contando de 1 a 5
print("Contando de 1 a 5:")
for i in range(1, 6):
    print(i)

```

***

### Ejemplo 4: Bucle `for` con un condicional `if`

Puedes combinar un bucle `for` con una sentencia `if` para tomar decisiones dentro de la iteración. Imagina que quieres encontrar los números pares en una lista.

``` Python
numeros = [12, 5, 8, 23, 16]

print("Números pares encontrados:")
for num in numeros:
    if num % 2 == 0:  # El operador '%' (módulo) da el residuo de una división
        print(num)

```

***

### Ejemplo 5: Imprimir números pares en un rango

Puedes usar un tercer argumento en `range()` para especificar el "paso" o incremento.

```
# Imprimir números pares del 0 al 10 (incluido)
print("Números pares del 0 al 10:")
for num in range(0, 11, 2):
    print(num)

```

***

### Ejemplo 6: Bucle `for` descendente

Puedes hacer que `range()` vaya en reversa usando un paso negativo.

``` Python
# Cuenta regresiva desde 5
print("Cuenta regresiva:")
for i in range(5, 0, -1):
    print(i)

print("¡Despegue!")

```

***

### Ejemplo 7: Usando `for` con `range()` para un cálculo

El bucle `for` es perfecto para realizar cálculos repetitivos. Este ejemplo calcula la suma de los primeros 100 números enteros.

``` Python
suma = 0

# Sumar números del 1 al 100
for num in range(1, 101):
    suma = suma + num

print(f"La suma de los primeros 100 números es: {suma}")

```

***
