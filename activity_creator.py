import tkinter as tk
import data_manager as dm

#ventana_agregar = None

def open_(parent):
    ventana_agregar =  tk.Toplevel(parent)
    ventana_agregar.title('Añadir Actividad')

    #-------------------------------------------------Datos Generales------------------------------------------------------------
    datos_actividad = tk.Frame(ventana_agregar)
    datos_actividad.grid(row = 0, column = 0)

    act_nombre_label = tk.Label(datos_actividad, text='Actividad')
    act_nombre_label.grid(row=0, column=0)
    act_nombre = tk.StringVar()
    act_nombre_entry = tk.Entry(datos_actividad, textvariable=act_nombre)
    act_nombre_entry.grid(row = 1, column = 0)

    act_responsable_label = tk.Label(datos_actividad, text='Responsable')
    act_responsable_label.grid(row =0, column=1)
    act_responsable = tk.StringVar()
    act_responsable_entry = tk.Entry(datos_actividad, textvariable=act_responsable)
    act_responsable_entry.grid(row = 1, column=1)

    #----------------------------------------------Datos Tiempos-------------------------------------------------------------------
    datos_tiempos = tk.LabelFrame(ventana_agregar, text='Tiempo')
    datos_tiempos.grid(row=1, column=0)

    t_esperado_label = tk.Label(datos_tiempos, text='Tiempo Esperado')
    t_esperado_label.grid(row=0, column=1)
    t_esperado = tk.StringVar()
    t_esperado_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_esperado)
    t_esperado_entry.grid(row=1, column=1,)

    t_optimista_label = tk.Label(datos_tiempos, text='Tiempo\nOptimista')
    t_optimista_label.grid(row=2, column=0)
    t_optimista = tk.StringVar()
    t_optimista_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_optimista)
    t_optimista_entry.grid(row=3, column=0)

    t_m_probable_label = tk.Label(datos_tiempos, text='Tiempo\nMas Probable')
    t_m_probable_label.grid(row=2, column=1)
    t_m_probable = tk.StringVar()
    t_m_probable_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_m_probable)
    t_m_probable_entry.grid(row=3, column=1)

    t_pesimista_label = tk.Label(datos_tiempos, text='Tiempo\nPesimista')
    t_pesimista_label.grid(row=2, column=2)
    t_pesimista = tk.StringVar()
    t_pesimista_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_pesimista)
    t_pesimista_entry.grid(row=3, column=2)
    
    t_acelerado_label = tk.Label(datos_tiempos, text='Tiempo\nAcelerado')
    t_acelerado_label.grid(row=4, column=1)
    t_acelerado = tk.StringVar()
    t_acelerado_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_acelerado)
    t_acelerado_entry.grid(row=5, column=1)

    #-------------------------------------------------Datos Costos--------------------------------------------------
    datos_costos = tk.LabelFrame(ventana_agregar, text='Costos')
    datos_costos.grid(row=2, column=0)

    c_esperado_label = tk.Label(datos_costos, text='Costo Esperado')
    c_esperado_label.grid(row=0, column=0)
    c_esperado = tk.StringVar()
    c_esperado_entry = tk.Spinbox(datos_costos, from_=0.0, textvariable=c_esperado)
    c_esperado_entry.grid(row=1, column=0)

    c_acelerado_label = tk.Label(datos_costos, text='Costo Acelerado')
    c_acelerado_label.grid(row=0, column=1)
    c_acelerado = tk.StringVar()
    c_acelerado_entry = tk.Spinbox(datos_costos, from_=0.0, textvariable=c_acelerado)
    c_acelerado_entry.grid(row=1, column=1)

    #------------------------------------------------Dependencias-------------------------------------------------
    dependencias = tk.LabelFrame(ventana_agregar, text='Dependencias')
    dependencias.grid(row=3, column=0)

    actividades = dm.get_activities_gantt()[:, 0]

    d_variables = [tk.StringVar() for _ in range(len(actividades))]
    checks = [tk.Checkbutton(dependencias, text=actividad, variable=d_variables[i], offvalue='', onvalue=actividad) for i, actividad in enumerate(actividades) ]

    for i, check in enumerate(checks):
        check.grid(column=0, row=i)

    agregar = tk.Button(ventana_agregar, text='agregar', command=lambda: agregar_actividad(parent, act_nombre.get(), act_responsable.get(), t_esperado.get(), t_optimista.get(), t_m_probable.get(), t_pesimista.get(), t_acelerado.get(), c_esperado.get(), c_acelerado.get(), list(map(lambda x: x.get() == '', d_variables)), actividades, ventana_agregar))
    agregar.grid(row = 4, column = 0)


def agregar_actividad(parent, act_nombre, act_responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependencias, actividades, window):
    dependen = []
    for i, not_checked in enumerate(dependencias):
        if not not_checked:
            dependen.append(actividades[i])
        
    dm.create_act(act_nombre, act_responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependen)
    parent.refresh_activities()
    window.destroy()
