import pandas as pd
import os.path


if not os.path.exists('actividades.csv'):
    act = pd.DataFrame({'nombre_actividad':[],
                        'responsable': [],
                        'tiempo_esperado': [],
                        'tiempo_optimista': [],
                        'tiempo_mas_probable':[],
                        'tiempo_pesimista': [],
                        'tiempo_acelerado': [],
                        'fecha_inicio': [],
                        'costo_esperado': [],
                        'costo_acelerado': [],
                        'porcentaje_terminado': []})
    act.to_csv('actividades.csv', index=False)
else:
    act = pd.read_csv('actividades.csv')


if not os.path.exists('dependencias.csv'):
    dep = pd.DataFrame({'actividad':[],
                        'dependencia': []})
    dep.to_csv('dependencias.csv', index=False)
else:
    dep = pd.read_csv('dependencias.csv')


def create_act(nombre, responsable, tiempo_esperado, tiempo_optimista, tiempo_mas_probable, tiempo_pesimista, tiempo_acelerado, fecha_inicio, costo_esperado, costo_acelerado):
    print('hola')
    act = pd.read_csv('actividades.csv')
    row = pd.DataFrame({'nombre_actividad': [nombre], 
                        'responsable': [responsable], 
                        'tiempo_esperado': [tiempo_esperado], 
                        'tiempo_optimista': [tiempo_optimista], 
                        'tiempo_mas_probable':[tiempo_mas_probable], 
                        'tiempo_pesimista': [tiempo_pesimista],
                        'tiempo_acelerado': [tiempo_acelerado],
                        'fecha_inicio': [fecha_inicio], 
                        'costo_esperado': [costo_esperado],
                        'costo_acelerado': [costo_acelerado],
                        'porcentaje_terminado': [0]})
    act = pd.concat([act,row])
    act.to_csv('actividades.csv', index=False)

def add_dependencies(depen):
    dep = pd.read_csv('dependencias.csv')
    for depender, dependee in depen:
        row = pd.DataFrame({'actividad': [depender],
                            'dependencia': [dependee]})
        dep = pd.concat([dep,row])
    dep.to_csv('dependencias.csv', index=False)

def delete_act():
    pass

def update_completition():
    pass

def get_activities_gantt():
    act = pd.read_csv('actividades.csv')
    return act[['nombre_actividad', 'responsable','fecha_inicio', 'tiempo_esperado', 'porcentaje_terminado']].to_numpy()
