import pandas as pd
import os.path

if not os.path.exists('actividades.csv'):
    act = pd.DataFrame({'nombre_actividad':[],
                        'responsable': [],
                        'fecha_inicio': [],
                        'duracion': [],
                        'porcentaje_terminado': []})
    act.to_csv('actividades.csv', index=False)
else:
    act = pd.read_csv('actividades.csv')


def create_act(act, nombre, responsable, fecha_inicio, duracion):
    print(type(act))
    row = pd.DataFrame({'nombre_actividad': [nombre], 'responsable': [responsable], 'fecha_inicio': [fecha_inicio], 'duracion': [duracion], 'porcentaje_terminado': [0]})
    act = pd.concat([act,row])
    act.to_csv('actividades.csv', index=False)

def delete_act():
    pass

def update_completition():
    pass

def get_activities_gantt():
    return act.to_numpy()
