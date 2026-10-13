import math
datos = [ 
{"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True}, 
{"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True}, 
{"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True}, 
{"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False}, 
{"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False}, 
{"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False}, 
{"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True}, 
{"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}] 


def calcular_ganancia_foil(p0, n0, p1, n1):
    # Si la nueva condición NO cubre ningún positivo (p1 es 0), 
    
    if p1 == 0:
        return -1.0
    
    # 1. Calculamos las probabilidades antes y despues:
    prob_previa = p0 / (p0 + n0)
    prob_posterior = p1 / (p1 + n1)
    
    # 2. Aplicamos la formula matematica de ganancia:
    ganancia = p1 * (math.log2(prob_posterior) - math.log2(prob_previa))
    return ganancia
#Paso 1: Separás positivos y negativos → esto te da p0 y n0.


lista_de_positivos= [p for p in datos if p["en_formacion"]] 
lista_de_negativos= [n for n in datos if not n["en_formacion"]]
p0=len(lista_de_positivos)
n0=len(lista_de_negativos)
#Paso 2: Generás candidatos recorriendo todos los datos → sacás los valores únicos de cada atributo.
def generar_candidatos(datos):
    # comprension de listas que recorre los datos y almaceno solo donde dice edad
    edades = {persona["edad"] for persona in datos}
    #creamos una lista de tuplas edad<= e donde e toma cada valor de edades previamente separados
    candidatos_edad = [("edad", "<=", e) for e in edades]

    # departamentos únicos → condiciones tipo "departamento == valor"
    departamentos = {persona["departamento"] for persona in datos}
    candidatos_departamento = [("departamento", "==", d) for d in departamentos]

    # niveles educativos únicos → condiciones tipo "nivel_educativo == valor"
    niveles = {persona["nivel_educativo"] for persona in datos}
    candidatos_nivel = [("nivel_educativo", "==", n) for n in niveles]

    # juntar todos los candidatos en una sola lista
    return candidatos_edad + candidatos_departamento + candidatos_nivel

#la funcion de arriba devuelve esto:
"""[
  ('edad', '<=', 35),
  ('edad', '<=', 38),
  ('edad', '<=', 22),
  ('edad', '<=', 23),
  ('edad', '<=', 24),
  ('edad', '<=', 40),
  ('edad', '<=', 29),
  ('edad', '<=', 21),
  ('departamento', '==', 'Finanzas'),
  ('departamento', '==', 'RRHH'),
  ('departamento', '==', 'IT'),
  ('nivel_educativo', '==', 'maestría'),
  ('nivel_educativo', '==', 'universitario'),
  ('nivel_educativo', '==', 'terciario')
]
"""


def mejor_regla(datos, positivos, negativos, p0, n0):
    candidatos = generar_candidatos(datos)
    mejor = None
    mejor_ganancia = float("-inf")#esto es para que cualquier ganancia sea mejor 

    for atributo, operador, valor in candidatos:
        # Filtrar positivos y negativos según el candidato
        if operador == "==":
            p1 = len([p for p in positivos if p[atributo] == valor])
            n1 = len([n for n in negativos if n[atributo] == valor])
        elif operador == "<=":
            p1 = len([p for p in positivos if p[atributo] <= valor])
            n1 = len([n for n in negativos if n[atributo] <= valor])
        else:
            p1, n1 = 0, 0
            """Si el operador es "==": cuenta cuántos positivos y negativos cumplen la condición de igualdad.

                      Si el operador es "<=": cuenta cuántos cumplen la condición de menor o igual.

                   Si no es ninguno de esos operadores, asigna p1, n1 = 0, 0.

                    Esto te da los valores p1 y n1 para cada candidato."""

        # Calcular FOIL Gain
        ganancia = calcular_ganancia_foil(p0, n0, p1, n1)

        # Guardar la mejor regla encontrada
        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor = (atributo, operador, valor, ganancia)

    return mejor

mejor = mejor_regla(datos, lista_de_positivos, lista_de_negativos, p0, n0)

atributo, operador, valor, ganancia = mejor
print(f"La mejor regla encontrada es: {atributo} {operador} {valor} con ganancia FOIL = {ganancia:.2f}")

