import data_manager as dm
from math import sqrt
from scipy.stats import norm
import pandas as pd

def calcular_varianza(t_optimista, t_pesimista):
    return ((t_pesimista - t_optimista) / 6) ** 2

def obtener_actividades_con_varianza():
    # Obtener actividades utilizando el método de data_manager
    activities = dm.get_activities_gantt()
    
    # Leer actividades completas desde el CSV
    act_df = pd.read_csv('actividades.csv')
    
    actividades_con_varianza = []
    
    for activity in activities:
        nombre = activity[0]
        responsable = activity[1]
        fecha_inicio = activity[2]
        tiempo_esperado = activity[3]
        porcentaje_terminado = activity[4]
        
        # Obtener los datos completos de la actividad desde el DataFrame
        act_row = act_df[act_df['nombre_actividad'] == nombre].iloc[0]
        
        tiempo_optimista = act_row['tiempo_optimista']
        tiempo_pesimista = act_row['tiempo_pesimista']
        
        # Calcular la varianza
        varianza = calcular_varianza(tiempo_optimista, tiempo_pesimista)
        
        # Añadir los datos a la lista
        actividades_con_varianza.append((nombre, responsable, fecha_inicio, tiempo_esperado, porcentaje_terminado, varianza))
    
    return actividades_con_varianza

def calcular_probabilidad(tiempo_objetivo, actividades_con_varianza):
    # Calcular el tiempo esperado total del proyecto
    tiempo_esperado_proyecto = sum(act[3] for act in actividades_con_varianza)
    
    # Calcular la varianza total del proyecto
    varianza_proyecto = sum(act[5] for act in actividades_con_varianza)
    
    # Calcular la desviación estándar del proyecto
    desviacion_estandar_proyecto = sqrt(varianza_proyecto)
    
    # Calcular la probabilidad utilizando la distribución normal
    Z = (tiempo_objetivo - tiempo_esperado_proyecto) / desviacion_estandar_proyecto
    probabilidad = norm.cdf(Z)
    
    return probabilidad

if __name__ == "__main__":
    actividades_con_varianza = obtener_actividades_con_varianza()
    tiempo_objetivo = 12  # Define tu tiempo objetivo
    probabilidad = calcular_probabilidad(tiempo_objetivo, actividades_con_varianza)
    
    print("Actividades con varianza:")
    for act in actividades_con_varianza:
        print(act)
    
    print(f"Probabilidad de completar el proyecto en {tiempo_objetivo} días: {probabilidad * 100:.2f}%")
