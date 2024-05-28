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
                        'fecha_inicio': [get_starting_date(dependencias) if dependencias != [] else 0], 
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

def delete_activity(self):
        
        if self.selected_activity:
            del self.activities[self.selected_activity]
            self.refresh_activities()


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

def get_activity_by_name(name):
    act = pd.read_csv('actividades.csv')
    activity = act[act['nombre_actividad'] == name]
    if activity.empty:
        return None
    return activity.iloc[0].to_dict()

def update_act(old_name, new_name, responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependencias):
    act = pd.read_csv('actividades.csv')
    idx = act[act['nombre_actividad'] == old_name].index
    if not idx.empty:
        idx = idx[0]
        act.at[idx, 'nombre_actividad'] = new_name
        act.at[idx, 'responsable'] = responsable
        act.at[idx, 'tiempo_esperado'] = t_esperado
        act.at[idx, 'tiempo_optimista'] = t_optimista
        act.at[idx, 'tiempo_mas_probable'] = t_m_probable
        act.at[idx, 'tiempo_pesimista'] = t_pesimista
        act.at[idx, 'tiempo_acelerado'] = t_acelerado
        act.at[idx, 'costo_esperado'] = c_esperado
        act.at[idx, 'costo_acelerado'] = c_acelerado
        act.at[idx, 'dependencias'] = ','.join(dependencias)
        act.to_csv('actividades.csv', index=False)