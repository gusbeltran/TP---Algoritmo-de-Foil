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

#1. Separar los ejemplos positivos (en_formacion == True) y negativos (en_formacion == False). 

lista_de_positivos= [p for p in datos if p["en_formacion"]] 
lista_de_negativos= [n for n in datos if not n["en_formacion"]]
p0=len(lista_de_positivos)
n0=len(lista_de_negativos)

#2. Para cada atributo, identificar los valores que aparecen en los pos pero no en los neg 
def comparacion(positivos,negativos):
    regla={}

    atributos = ["edad", "departamento", "nivel_educativo"]

    for i in atributos:
        #se hacen conjuntos con "set" sin que se repitan
        conjuntoPos = set(v[i] for v in positivos)
        conjuntoNeg = set(v[i] for v in negativos)
        diferenciaDeConjuntos = conjuntoPos-conjuntoNeg

        regla[i]=diferenciaDeConjuntos

        
    return regla


print(" ¿Qué valores de departamento aparecen solo en los positivos? ")
print(comparacion(lista_de_positivos, lista_de_negativos)["departamento"])
print(" ¿Qué niveles educativos son comunes en los positivos pero no en los negativos? ")
print(comparacion(lista_de_positivos,lista_de_negativos)["nivel_educativo"])
print("¿Qué edades aparecen solo en los positivos?  ")
print(comparacion(lista_de_positivos,lista_de_negativos)["edad"])



"""a) Desarrollar un programa en Python que obtenga el cálculo del FOIL Gain para la condición 
nivel_educativo == 'terciario', con la siguiente salida: """

#funcion pos y neg con nivel terciario
def nivel(pos,neg,atributo):
    lista_pos_terciario=[p for p in pos if p[atributo]=="terciario"]
    p1=len(lista_pos_terciario)
    lista_neg_terciario = [n for n in neg if n[atributo] == "terciario"]
    n1=len(lista_neg_terciario)
    return p1,n1

#c) Desarrollar un programa en Python que obtenga el cálculo del FOIL Gain para la condición edad ≤ 23
#se hace la funcion pero mas generica para que puedas incluir cualquier limite
def edad_condicion(pos, neg, atributo, limite):
    lista_pos = [e for e in pos if e[atributo] <= limite]
    lista_neg = [e for e in neg if e[atributo] <= limite]
    p1 = len(lista_pos)
    n1 = len(lista_neg)
    return p1, n1


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
limites = [21, 22, 23, 24]


while True:
    valorEdad = int(input("Ingrese un número de filtro por edad entre estos: 21-22-23-24 "))
    if valorEdad in limites:
        edadG=o1,b1=edad_condicion(lista_de_positivos,lista_de_negativos,"edad",valorEdad)
        print(f"Ganancia FOIL para edad {valorEdad} : ", edadG)
        break
    else:
        print("valor incorrecto, son 4 numeros nada mas para elegir bldo/a, proba otra vez")
        


p1, n1 = nivel(lista_de_positivos, lista_de_negativos, "nivel_educativo")
ganancia = calcular_ganancia_foil(p0, n0, p1, n1)

print("Ganancia FOIL para nivel_educativo == 'terciario':", ganancia)



