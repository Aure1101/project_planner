import data_manager as dm # Imprtar el archivo data_manager
import numpy as np # Importar la biblioteca numpy
from scipy.stats import norm

actividades = dm.get_activities_gantt() # Instanciar el objeto para las actividades

def calcular_varianza(actividades): # Metodo para calcular la varianza 
    varianzas = [] # Arreglo para almacenar los datos 
    for actividad in actividades: # Iteracion de cada fila de las actividades 
        TO = actividad['tiempo_optimista'] # Guardar en una variable el tiempo Optimista 
        TP = actividad['tiempo_pesimista'] # Guardar en una variable el tiempo pesimista 
        varianza = ((TP - TO) / 6) ** 2 # Calculo de la varianza 
        varianzas.append(varianza) # Agregar al calculo al arreglo
    varianza_total = np.sum(varianzas) # SUmar los datos del arreglo
    return varianza_total # Retornar el calculo

def calcular_tiempo_esperado_total(actividades):
    tiempo_esperado_total = actividades['tiempo_esperado'].sum()
    return tiempo_esperado_total

def calcular_probabilidad(tiempo_esperado_total, varianza_total, fecha_limite):
    desviacion_estandar_total = np.sqrt(varianza_total)
    Z = (fecha_limite - tiempo_esperado_total) / desviacion_estandar_total
    probabilidad = norm.cdf(Z)
    return probabilidad
 
