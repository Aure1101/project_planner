import data_manager as dm # Imprtar el archivo data_manager
import numpy as np # Importar la biblioteca numpy

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

def calcular_probabilidad(varianza_total):

    
    pass

