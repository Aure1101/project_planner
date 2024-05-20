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


def create_act(nombre, responsable, tiempo_esperado, tiempo_optimista, tiempo_mas_probable, tiempo_pesimista, tiempo_acelerado, costo_esperado, costo_acelerado, dependencias):
    print('hola')
    act = pd.read_csv('actividades.csv')
    row = pd.DataFrame({'nombre_actividad': [nombre], 
                        'responsable': [responsable], 
                        'tiempo_esperado': [tiempo_esperado], 
                        'tiempo_optimista': [tiempo_optimista], 
                        'tiempo_mas_probable':[tiempo_mas_probable], 
                        'tiempo_pesimista': [tiempo_pesimista],
                        'tiempo_acelerado': [tiempo_acelerado],
                        'fecha_inicio': [get_starting_date(dependencias)], 
                        'costo_esperado': [costo_esperado],
                        'costo_acelerado': [costo_acelerado],
                        'porcentaje_terminado': [0]})
    act = pd.concat([act,row])
    act.to_csv('actividades.csv', index=False)
    add_dependencies(nombre, dependencias)

def add_dependencies(depender, dependencias):
    dep = pd.read_csv('dependencias.csv')
    for dependee in dependencias:
        row = pd.DataFrame({'actividad': [depender],
                            'dependencia': [dependee]})
        dep = pd.concat([dep,row])
    dep.to_csv('dependencias.csv', index=False)

def delete_act():
    pass

def update_completition():
    pass

def get_activities_pertcpm():
    act = pd.read_csv('actividades.csv')
    return act[['nombre_actividad', 'responsable', 'tiempo_optimista', 'tiempo_pesimista', 'tiempo_esperado', 'fecha_inicio']].to_numpy()

def get_activities_gantt():
    act = pd.read_csv('actividades.csv')
    return act[['nombre_actividad', 'responsable','fecha_inicio', 'tiempo_esperado', 'porcentaje_terminado']].to_numpy()

def get_starting_date(dependencias):
    act = pd.read_csv('actividades.csv')
    act = act[['nombre_actividad', 'tiempo_esperado', 'fecha_inicio']]
    act = act.loc[act['nombre_actividad'].isin(dependencias)]
    start_date = max(act['tiempo_esperado'] + act['fecha_inicio'])
    return start_date

def get_dependencies(actividad):
    dep = pd.read_csv('dependencias.csv')
    mask = dep['actividad'] == actividad
    print(dep[mask].to_numpy()[:, 1])
    return dep[mask].to_numpy()[:, 1]