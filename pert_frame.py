import data_manager as dm 
import numpy as np
from scipy.stats import norm

def calcular_varianza(actividades):
    varianzas = []
    for actividad in actividades:
        TO = actividad[3]  # tiempo_optimista
        TP = actividad[5]  # tiempo_pesimista
        varianza = ((TP - TO) / 6) ** 2
        varianzas.append(varianza)
    varianza_total = np.sum(varianzas)
    return varianza_total

def probar_calculos():
    # Obtener las actividades desde el data_manager
    actividades = dm.get_activities_gantt()

    # Calcular la varianza
    varianza_total = calcular_varianza(actividades)

    # Imprimir el resultado
    print("Varianza total:", varianza_total)

'''
def calcular_heuristica(actividades):
    # Calculamos los tiempos de inicio más temprano (TIT), tiempos finales más tempranos (TFT),
    # tiempos de inicio más tardíos (TAT) y tiempos finales más tardíos (TFT) para cada actividad.
    TIT = np.zeros(len(actividades))
    TFT = np.zeros(len(actividades))
    TAT = np.zeros(len(actividades))
    TTT = np.zeros(len(actividades)) # Tiempo de termino temprano
    TIT[0] = 0
    for i in range(len(actividades)):
        TFT[i] = TIT[i] + actividades[i]['tiempo_esperado']
        for dependencia in actividades[i]['dependencias']:
            if TFT[i] > TIT[int(dependencia)]:
                TIT[int(dependencia)] = TFT[i]
    for i in range(len(actividades)-1, -1, -1):
        TAT[i] = TTT[i] - TFT[i]
        for dependiente in actividades[i]['dependientes']:
            if TTT[int(dependiente)] == 0:
                TTT[int(dependiente)] = TFT[i]
            elif TTT[int(dependiente)] > TFT[i]:
                TTT[int(dependiente)] = TFT[i]
    heuristica = TTT - TIT
    return heuristica

def calcular_probabilidad(varianza_total, fecha_limite, tiempo_esperado_total):
    desviacion_estandar_total = np.sqrt(varianza_total)
    Z = (fecha_limite - tiempo_esperado_total) / desviacion_estandar_total
    probabilidad = norm.cdf(Z)
    return probabilidad'''

# Llamar a la función de prueba
probar_calculos()