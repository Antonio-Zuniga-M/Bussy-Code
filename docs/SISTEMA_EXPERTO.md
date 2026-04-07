# Sistema Experto de Nivelación en Python: Base de Conocimiento Completa

## 1. Banco de Preguntas (Q1 a Q34)

Para que una variable `Q` sea `True`, el usuario debe seleccionar **exactamente** la combinación de respuestas marcada como *(Correcta)*. Si selecciona más, menos, o diferentes opciones, `Q = False`.

### Bloque 1: Sintaxis Básica y Control de Flujo
* **Q1: Variables y Tipos** | ¿Cuál es el valor de `x` en `x = 5 * int("2")`?
  - [A] "52" | [B] 10 | [C] Error | [D] 5.2
  - *Condición:* `Q1=True` si selecciona solo **[B]**.
* **Q2: Operadores** | Selecciona las afirmaciones verdaderas sobre operadores en Python:
  - [A] `10 // 3` devuelve `3.33` | [B] `2 ** 3` devuelve `8` | [C] `True and False` devuelve `True` | [D] `10 % 2 == 0` devuelve `True`
  - *Condición:* `Q2=True` si selecciona **[B, D]**.
* **Q3: Condicionales** | En un bloque `if/elif/else`, ¿cuántos `elif` pueden existir?
  - [A] Solo uno | [B] Ninguno | [C] Ilimitados | [D] Máximo tres
  - *Condición:* `Q3=True` si selecciona solo **[C]**.
**Q4: Bucles For** | ¿Qué imprime `for i in range(1, 4): print(i)`?
  - [A] 1, 2, 3, 4 | [B] 0, 1, 2, 3 | [C] 1, 2, 3 | [D] 2, 3, 4
  - *Condición:* `Q4=True` si selecciona solo **[C]**.
* **Q5: Bucles While** | ¿Cuál es la principal diferencia funcional entre un `for` y un `while` en Python?
  - [A] El `while` itera sobre secuencias definidas, el `for` no. | [B] El `while` se ejecuta mientras una condición sea verdadera. | [C] El `for` es infinito por defecto.
  - *Condición:* `Q5=True` si selecciona solo **[B]**.

### Bloque 2: Estructuras de Datos
* **Q6: Listas** | Dada `lista = [1, 2]`. ¿Cómo añades el número 3 al final?
  - [A] `lista.add(3)` | [B] `lista.insert(3)` | [C] `lista.append(3)` | [D] `lista + 3`
  - *Condición:* `Q6=True` si selecciona solo **[C]**.
* **Q7: Tuplas** | Identifica las características reales de una Tupla:
  - [A] Son inmutables. | [B] Se definen con llaves `{}`. | [C] Pueden contener diferentes tipos de datos. | [D] Son más lentas que las listas.
  - *Condición:* `Q7=True` si selecciona **[A, C]**.
* **Q8: Diccionarios** | ¿Cómo accedes de forma segura (sin error de llave) al valor de la clave "edad" en `dict = {"nombre": "Ana"}`?
  - [A] `dict["edad"]` | [B] `dict.get("edad")` | [C] `dict.fetch("edad")`
  - *Condición:* `Q8=True` si selecciona solo **[B]**.
* **Q9: Sets** | ¿Qué caracteriza a un Set (Conjunto) en Python? (Selecciona todas)
  - [A] Permite elementos duplicados. | [B] Mantiene el orden de inserción. | [C] Elimina duplicados automáticamente. | [D] Soporta operaciones como intersección y unión.
  - *Condición:* `Q9=True` si selecciona **[C, D]**.

### Bloque 3: Funciones y Estilo
* **Q10: Funciones** | ¿Qué ocurre si una función en Python no tiene un `return` explícito?
  - [A] Retorna `0` | [B] Arroja un `SyntaxError` | [C] Retorna `None` | [D] Retorna `False`
  - *Condición:* `Q10=True` si selecciona solo **[C]**.
* **Q11: Scope (Alcance)** | Selecciona las afirmaciones verdaderas sobre el Scope:
  - [A] Una variable definida dentro de una función puede ser leída globalmente. | [B] `global` permite modificar variables globales desde una función local. | [C] Las variables locales se destruyen al terminar la función.
  - *Condición:* `Q11=True` si selecciona **[B, C]**.
* **Q12: PEP8** | Según PEP8, ¿cómo debe nombrarse una función en Python?
  - [A] `MiFuncion` (CamelCase) | [B] `mi_funcion` (snake_case) | [C] `miFuncion` (mixedCase)
  - *Condición:* `Q12=True` si selecciona solo **[B]**.
* **Q13: Lambdas** | ¿Para qué sirve una función `lambda`?
  - [A] Para crear clases anónimas. | [B] Para crear funciones anónimas de una sola expresión. | [C] Para manejar excepciones.
  - *Condición:* `Q13=True` si selecciona solo **[B]**.
* **Q14: Map/Filter** | ¿Qué hace `filter(lambda x: x > 2, [1, 2, 3])`?
  - [A] Retorna `[3]` (o un iterador con el 3) | [B] Retorna `[False, False, True]` | [C] Da error
  - *Condición:* `Q14=True` si selecciona solo **[A]**.
* **Q15: Comprehensions** | Selecciona la sintaxis correcta para crear una lista de números pares del 0 al 4:
  - [A] `[x for x in range(5) if x % 2 == 0]` | [B] `[if x % 2 == 0 for x in range(5)]`
  - *Condición:* `Q15=True` si selecciona solo **[A]**.

### Bloque 4: Programación Orientada a Objetos (POO)
* **Q16: Clases e Init** | El parámetro `self` en los métodos de instancia hace referencia a:
  - [A] La clase padre. | [B] Las variables globales. | [C] La instancia específica del objeto llamador.
  - *Condición:* `Q16=True` si selecciona solo **[C]**.
* **Q17: Atributos y Métodos de Clase** | ¿Qué decorador se usa para que un método pertenezca a la clase y no a la instancia, recibiendo `cls` como primer argumento?
  - [A] `@staticmethod` | [B] `@classmethod` | [C] `@abstractmethod`
  - *Condición:* `Q17=True` si selecciona solo **[B]**.
* **Q18: Herencia** | ¿Para qué sirve la función `super()` en POO?
  - [A] Para acceder a los métodos de la clase hija. | [B] Para llamar a métodos de la clase padre (como `__init__`). | [C] Para crear superusuarios.
  - *Condición:* `Q18=True` si selecciona solo **[B]**.
* **Q19: Dunder Methods** | ¿Qué método mágico (Dunder) debes sobreescribir para definir cómo se imprime un objeto con `print(obj)`?
  - [A] `__print__` | [B] `__string__` | [C] `__str__` | [D] `__init__`
  - *Condición:* `Q19=True` si selecciona solo **[C]**.

### Bloque 5: Manejo de Errores, Archivos y Entorno
* **Q20: Excepciones** | ¿Qué bloque se ejecuta SIEMPRE al final de un `try/except`, haya o no error?
  - [A] `else` | [B] `finally` | [C] `catch` | [D] `always`
  - *Condición:* `Q20=True` si selecciona solo **[B]**.
* **Q21: Raise** | ¿Qué palabra clave se usa para forzar/disparar un error manualmente en Python?
  - [A] `throw` | [B] `error` | [C] `raise` | [D] `trigger`
  - *Condición:* `Q21=True` si selecciona solo **[C]**.
* **Q22: Archivos** | ¿Por qué es mejor abrir archivos usando `with open("x.txt") as f:` en lugar de solo `f = open()`?
  - [A] Es más rápido. | [B] Cierra el archivo automáticamente incluso si hay un error. | [C] Evita inyección SQL.
  - *Condición:* `Q22=True` si selecciona solo **[B]**.
* **Q23: Git** | Selecciona los comandos correctos del flujo básico de Git:
  - [A] `git init` | [B] `git save` | [C] `git commit` | [D] `git push`
  - *Condición:* `Q23=True` si selecciona **[A, C, D]**.
* **Q24: Entornos Virtuales** | ¿Para qué sirve crear un entorno virtual (`venv`)?
  - [A] Para ejecutar Python en un navegador. | [B] Para aislar las dependencias y librerías de un proyecto específico del sistema global.
  - *Condición:* `Q24=True` si selecciona solo **[B]**.

### Bloque 6: Python Avanzado
* **Q25: Decoradores** | Selecciona las afirmaciones correctas sobre decoradores:
  - [A] Modifican el comportamiento de una función. | [B] Reciben una función como parámetro y retornan una función (o callable). | [C] Se aplican usando el símbolo `&`.
  - *Condición:* `Q25=True` si selecciona **[A, B]**.
* **Q26: Iterables vs Iteradores** | ¿Qué función nativa avanza un iterador al siguiente elemento?
  - [A] `advance()` | [B] `next()` | [C] `step()` | [D] `__iter__()`
  - *Condición:* `Q26=True` si selecciona solo **[B]**.
* **Q27: Generadores** | ¿Qué palabra clave convierte una función normal en un Generador que evalúa valores de forma perezosa (lazy evaluation)?
  - [A] `generate` | [B] `async` | [C] `yield` | [D] `return`
  - *Condición:* `Q27=True` si selecciona solo **[C]**.
* **Q28: Context Managers** | Para crear un Context Manager personalizado utilizable con la sintaxis `with`, tu clase debe implementar:
  - [A] `__with__` y `__end__` | [B] `__enter__` y `__exit__` | [C] `__open__` y `__close__`
  - *Condición:* `Q28=True` si selecciona solo **[B]**.
* **Q29: Testing** | En la librería `unittest`, ¿qué método verifica que dos valores sean idénticos?
  - [A] `assertEqual` | [B] `assert_equals` | [C] `check_equal`
  - *Condición:* `Q29=True` si selecciona solo **[A]**.

### Bloque 7: Nivel Experto
* **Q30: Asincronismo** | Identifica las reglas de `asyncio`:
  - [A] Solo puedes usar `await` dentro de una función definida con `async def`. | [B] `await` bloquea el hilo principal globalmente. | [C] El código asíncrono mejora el rendimiento en operaciones I/O (Red, Base de datos).
  - *Condición:* `Q30=True` si selecciona **[A, C]**.
* **Q31: Threading vs Multiprocessing** | Selecciona la afirmación correcta respecto al modelo de ejecución en Python:
  - [A] Threading es mejor para CPU-bound, Multiprocessing para I/O-bound. | [B] Multiprocessing evade el GIL usando procesos separados, siendo ideal para tareas intensivas de CPU.
  - *Condición:* `Q31=True` si selecciona solo **[B]**.
* **Q32: GIL (Global Interpreter Lock)** | ¿Qué es el GIL en CPython?
  - [A] Un sistema de seguridad de red. | [B] Un bloqueo de un solo hilo que impide que múltiples hilos nativos ejecuten bytecodes de Python en paralelo.
  - *Condición:* `Q32=True` si selecciona solo **[B]**.
* **Q33: Metaclases** | ¿Qué clase predeterminada en Python es la Metaclase por defecto para construir clases?
  - [A] `object` | [B] `class` | [C] `type` | [D] `meta`
  - *Condición:* `Q33=True` si selecciona solo **[C]**.
* **Q34: Optimización / C-Extensions** | Identifica métodos reales para optimizar masivamente el rendimiento y la memoria en Python:
  - [A] Compilar código crítico con Cython. | [B] Usar variables globales para todo. | [C] Modificar el comportamiento del `gc` (Garbage Collector).
  - *Condición:* `Q34=True` si selecciona **[A, C]**.

---

## 2. Base de Reglas de Inferencia (R1 a R45)

*Nota: Los rangos están ordenados siendo 3 el nivel más bajo (novato) y 1 el más alto dentro de la liga.*

### Fase 1: Reglas de Asignación de Bloque (Filtro Dinámico)
* **R1:** SI (`Q1`=False O `Q2`=False) ENTONCES Bloque = `Nulo`
* **R2:** SI (`Q1`=True Y `Q10`=False) ENTONCES Bloque = `Basico`
* **R3:** SI (`Q10`=True Y `Q16`=False) ENTONCES Bloque = `Funcional`
* **R4:** SI (`Q16`=True Y `Q25`=False) ENTONCES Bloque = `POO_Avanzado`
* **R5:** SI (`Q25`=True Y `Q30`=False) ENTONCES Bloque = `Python_Senior`
* **R6:** SI (`Q30`=True) ENTONCES Bloque = `Arquitecto`

### Fase 2: Asignación Final - Bloque Nulo y Básico
* **R7:** SI (Bloque = `Nulo`) ENTONCES Rango = `Bronce 3`
* **R8:** SI (Bloque = `Basico` Y `Q3`=False) ENTONCES Rango = `Bronce 3`
* **R9:** SI (Bloque = `Basico` Y `Q3`=True Y `Q4`=False Y `Q5`=False) ENTONCES Rango = `Bronce 2`
* **R10:** SI (Bloque = `Basico` Y (`Q4`=True O `Q5`=True) Y `Q6`=False) ENTONCES Rango = `Bronce 1`
* **R11:** SI (Bloque = `Basico` Y `Q6`=True Y `Q8`=False) ENTONCES Rango = `Bronce 1`
* **R12:** SI (Bloque = `Basico` Y `Q6`=True Y `Q8`=True Y `Q9`=False) ENTONCES Rango = `Plata 3`
* **R13:** SI (Bloque = `Basico` Y `Q9`=True) ENTONCES Rango = `Plata 3`

### Fase 3: Asignación Final - Bloque Funcional
* **R14:** SI (Bloque = `Funcional` Y `Q11`=False) ENTONCES Rango = `Plata 2`
* **R15:** SI (Bloque = `Funcional` Y `Q11`=True Y `Q13`=False) ENTONCES Rango = `Plata 1`
* **R16:** SI (Bloque = `Funcional` Y `Q13`=True Y `Q15`=False) ENTONCES Rango = `Plata 1`
* **R17:** SI (Bloque = `Funcional` Y `Q15`=True Y `Q12`=False) ENTONCES Rango = `Oro 3`
* **R18:** SI (Bloque = `Funcional` Y `Q15`=True Y `Q12`=True Y `Q14`=False) ENTONCES Rango = `Oro 3`
* **R19:** SI (Bloque = `Funcional` Y `Q14`=True Y `Q15`=False) ENTONCES Rango = `Oro 2`
* **R20:** SI (Bloque = `Funcional` Y `Q15`=True Y `Q14`=True) ENTONCES Rango = `Oro 2`

### Fase 4: Asignación Final - Bloque POO Avanzado
* **R21:** SI (Bloque = `POO_Avanzado` Y `Q17`=False) ENTONCES Rango = `Oro 1`
* **R22:** SI (Bloque = `POO_Avanzado` Y `Q17`=True Y `Q18`=False) ENTONCES Rango = `Oro 1`
* **R23:** SI (Bloque = `POO_Avanzado` Y `Q18`=True Y `Q19`=False) ENTONCES Rango = `Platino 3`
* **R24:** SI (Bloque = `POO_Avanzado` Y `Q19`=True Y `Q20`=False) ENTONCES Rango = `Platino 3`
* **R25:** SI (Bloque = `POO_Avanzado` Y `Q20`=True Y `Q21`=False) ENTONCES Rango = `Platino 2`
* **R26:** SI (Bloque = `POO_Avanzado` Y `Q21`=True Y `Q22`=False) ENTONCES Rango = `Platino 2`
* **R27:** SI (Bloque = `POO_Avanzado` Y `Q22`=True Y `Q23`=False) ENTONCES Rango = `Platino 2`
* **R28:** SI (Bloque = `POO_Avanzado` Y `Q22`=True Y `Q24`=False) ENTONCES Rango = `Platino 2`
* **R29:** SI (Bloque = `POO_Avanzado` Y `Q23`=True Y `Q24`=True) ENTONCES Rango = `Platino 1`

### Fase 5: Asignación Final - Bloque Python Senior
* **R30:** SI (Bloque = `Python_Senior` Y `Q26`=False) ENTONCES Rango = `Platino 1`
* **R31:** SI (Bloque = `Python_Senior` Y `Q26`=True Y `Q27`=False) ENTONCES Rango = `Diamante 3`
* **R32:** SI (Bloque = `Python_Senior` Y `Q27`=True Y `Q28`=False) ENTONCES Rango = `Diamante 3`
* **R33:** SI (Bloque = `Python_Senior` Y `Q28`=True Y `Q29`=False) ENTONCES Rango = `Diamante 2`
* **R34:** SI (Bloque = `Python_Senior` Y `Q29`=True) ENTONCES Rango = `Diamante 1`

### Fase 6: Asignación Final - Bloque Arquitecto
* **R35:** SI (Bloque = `Arquitecto` Y `Q31`=False) ENTONCES Rango = `Maestro 3`
* **R36:** SI (Bloque = `Arquitecto` Y `Q31`=True Y `Q32`=False) ENTONCES Rango = `Maestro 3`
* **R37:** SI (Bloque = `Arquitecto` Y `Q32`=True Y `Q33`=False) ENTONCES Rango = `Maestro 2`
* **R38:** SI (Bloque = `Arquitecto` Y `Q33`=True Y `Q34`=False) ENTONCES Rango = `Maestro 1`
* **R39:** SI (Bloque = `Arquitecto` Y `Q34`=True) ENTONCES Rango = `Code Predator`

### Fase 7: Reglas de Seguridad (Anti-Trampas / Prioridad Absoluta)
Estas reglas se disparan si el usuario tiene una incoherencia grave (acierta en algo de nivel Maestro, pero falla en algo de nivel Bronce). Sobrescriben los resultados anteriores.
* **R40:** SI (`Q34`=True Y `Q1`=False) ENTONCES Rango = `Bronce 3` *(Adivinó C-Extensions pero no sabe declarar variables)*
* **R41:** SI (`Q30`=True Y `Q10`=False) ENTONCES Rango = `Bronce 2` *(Adivinó asincronismo pero no sabe qué es un return)*
* **R42:** SI (`Q25`=True Y `Q3`=False) ENTONCES Rango = `Bronce 3` *(Adivinó decoradores pero no sabe usar if/else)*
* **R43:** SI (`Q16`=True Y `Q6`=False) ENTONCES Rango = `Bronce 1` *(Adivinó clases pero no sabe usar una lista)*
* **R44:** SI (`Q29`=True Y `Q10`=False) ENTONCES Rango = `Bronce 2` *(Adivinó testing pero falla en funciones básicas)*
* **R45:** SI (`Q24`=True Y `Q2`=False) ENTONCES Rango = `Bronce 3` *(Adivinó entornos virtuales pero falla en operadores)*