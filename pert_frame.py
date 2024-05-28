import data_manager as dm
from math import sqrt
from scipy.stats import norm
import pandas as pd
import tkinter as tk
from tkinter import ttk

def calcular_varianza(t_optimista, t_pesimista):
    return ((t_pesimista - t_optimista) / 6) ** 2

def obtener_actividades_con_varianza():
    activities = dm.get_activities_gantt()
    act_df = pd.read_csv('actividades.csv')
    
    actividades_con_varianza = []
    
    for activity in activities:
        nombre = activity[0]
        responsable = activity[1]
        fecha_inicio = activity[2]
        tiempo_esperado = activity[3]
        porcentaje_terminado = activity[4]
        
        act_row = act_df[act_df['nombre_actividad'] == nombre].iloc[0]
        
        tiempo_optimista = act_row['tiempo_optimista']
        tiempo_pesimista = act_row['tiempo_pesimista']
        
        varianza = calcular_varianza(tiempo_optimista, tiempo_pesimista)
        
        actividades_con_varianza.append((nombre, responsable, fecha_inicio, tiempo_esperado, porcentaje_terminado, varianza))
    
    return actividades_con_varianza

def calcular_probabilidad(tiempo_objetivo, actividades_con_varianza):
    tiempo_esperado_proyecto = sum(act[3] for act in actividades_con_varianza)
    varianza_proyecto = sum(act[5] for act in actividades_con_varianza)
    desviacion_estandar_proyecto = sqrt(varianza_proyecto)
    
    Z = (tiempo_objetivo - tiempo_esperado_proyecto) / desviacion_estandar_proyecto
    probabilidad = norm.cdf(Z)
    
    return probabilidad

def calculate_times(act_df):
    act_df['ES'] = 0
    act_df['EF'] = act_df['tiempo_esperado']
    for i in range(1, len(act_df)):
        act_df.at[i, 'ES'] = act_df.at[i-1, 'EF']
        act_df.at[i, 'EF'] = act_df.at[i, 'ES'] + act_df.at[i, 'tiempo_esperado']

    max_ef = act_df['EF'].max()
    act_df['LF'] = max_ef
    act_df['LS'] = act_df['LF'] - act_df['tiempo_esperado']
    for i in range(len(act_df) - 2, -1, -1):
        act_df.at[i, 'LF'] = act_df.at[i+1, 'LS']
        act_df.at[i, 'LS'] = act_df.at[i, 'LF'] - act_df.at[i, 'tiempo_esperado']

    return act_df

def calculate_holgura(act_df):
    act_df['Holgura'] = act_df['LS'] - act_df['ES']
    return act_df

def display_in_tkinter(act_df, probability):
    root = tk.Tk()
    root.title("Datos de Actividades")

    tree = ttk.Treeview(root, columns=('Nombre', 'Responsable', 'Fecha Inicio', 'Tiempo Esperado', 'Porcentaje Terminado', 'ES', 'EF', 'LS', 'LF', 'Holgura', 'Varianza'), show='headings')
    
    tree.heading('Nombre', text='Nombre')
    tree.heading('Responsable', text='Responsable')
    tree.heading('Tiempo Esperado', text='Tiempo Esperado')
    tree.heading('ES', text='ES')
    tree.heading('EF', text='EF')
    tree.heading('LS', text='LS')
    tree.heading('LF', text='LF')
    tree.heading('Holgura', text='Holgura')
    tree.heading('Varianza', text='Varianza')

    for index, row in act_df.iterrows():
        tree.insert('', tk.END, values=(row['nombre_actividad'], row['responsable'], row['fecha_inicio'], row['tiempo_esperado'], row['porcentaje_terminado'], row['ES'], row['EF'], row['LS'], row['LF'], row['Holgura'], row['Varianza']))

    for col in tree['columns']:
        tree.column(col, width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    probability_label = tk.Label(root, text=f"Probabilidad de completar el proyecto en el tiempo objetivo: {probability:.2%}")
    probability_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    activities = dm.get_activities_gantt()
    act_df = pd.DataFrame(activities, columns=['nombre_actividad', 'responsable', 'fecha_inicio', 'tiempo_esperado', 'porcentaje_terminado'])
    
    act_df = calculate_times(act_df)
    act_df = calculate_holgura(act_df)
    
    actividades_con_varianza = obtener_actividades_con_varianza()
    
    for activity in actividades_con_varianza:
        act_df.loc[act_df['nombre_actividad'] == activity[0], 'Varianza'] = activity[5]

    max_time = 12 
    #"max(act_df['fecha_inicio'] + act_df['tiempo_esperado'])
    probabilidad = calcular_probabilidad(max_time, actividades_con_varianza)

    display_in_tkinter(act_df, probabilidad)

