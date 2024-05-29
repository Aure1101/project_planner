import tkinter as tk
import data_manager as dm

class ActivityManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Actividades")

        # Crear el Listbox para las actividades
        self.activity_listbox = tk.Listbox(root)
        self.activity_listbox.pack(fill=tk.BOTH, expand=1)
        self.activity_listbox.bind("<<ListboxSelect>>", self.on_activity_select)

        # Botón para agregar una nueva actividad
        self.add_button = tk.Button(root, text="Agregar Actividad", command=lambda: self.open_activity_window())
        self.add_button.pack()

        # Inicializar el contenido del Listbox
        self.refresh_activities()

    def refresh_activities(self):
        self.activity_listbox.delete(0, tk.END)
        activities = dm.get_activities_gantt()[:, 0]  # Asumiendo que get_activities_gantt() devuelve un array 2D
        for activity in activities:
            self.activity_listbox.insert(tk.END, activity)

    def on_activity_select(self, event):
        try:
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                activity_name = event.widget.get(index)
                self.open_activity_window(activity_name)
        except Exception as e:
            print(f"Error al seleccionar la actividad: {e}")

    def open_activity_window(self, activity_name=None):
        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title('Editar Actividad' if activity_name else 'Añadir Actividad')

        #-------------------------------------------------Datos Generales------------------------------------------------------------
        datos_actividad = tk.Frame(ventana_agregar)
        datos_actividad.grid(row=0, column=0)

        act_nombre_label = tk.Label(datos_actividad, text='Actividad')
        act_nombre_label.grid(row=0, column=0)
        act_nombre = tk.StringVar()
        act_nombre_entry = tk.Entry(datos_actividad, textvariable=act_nombre)
        act_nombre_entry.grid(row=1, column=0)

        act_responsable_label = tk.Label(datos_actividad, text='Responsable')
        act_responsable_label.grid(row=0, column=1)
        act_responsable = tk.StringVar()
        act_responsable_entry = tk.Entry(datos_actividad, textvariable=act_responsable)
        act_responsable_entry.grid(row=1, column=1)

        #----------------------------------------------Datos Tiempos-------------------------------------------------------------------
        datos_tiempos = tk.LabelFrame(ventana_agregar, text='Tiempo')
        datos_tiempos.grid(row=1, column=0)

        t_esperado_label = tk.Label(datos_tiempos, text='Tiempo Esperado')
        t_esperado_label.grid(row=0, column=1)
        t_esperado = tk.StringVar()
        t_esperado_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_esperado)
        t_esperado_entry.grid(row=1, column=1)

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
        checks = [tk.Checkbutton(dependencias, text=actividad, variable=d_variables[i], offvalue='', onvalue=actividad) for i, actividad in enumerate(actividades)]

        for i, check in enumerate(checks):
            check.grid(column=0, row=i)

        if activity_name:
            # Cargar los datos de la actividad existente
            activity = dm.get_activity_by_name(activity_name)
            if activity:
                act_nombre.set(activity['nombre_actividad'])
                act_responsable.set(activity['responsable'])
                t_esperado.set(activity['tiempo_esperado'])
                t_optimista.set(activity['tiempo_optimista'])
                t_m_probable.set(activity['tiempo_mas_probable'])
                t_pesimista.set(activity['tiempo_pesimista'])
                t_acelerado.set(activity['tiempo_acelerado'])
                c_esperado.set(activity['costo_esperado'])
                c_acelerado.set(activity['costo_acelerado'])
                dependencias_list = activity['dependencias'].split(',')
                for i, actividad in enumerate(actividades):
                    if actividad in dependencias_list:
                        d_variables[i].set(actividad)

        guardar = tk.Button(ventana_agregar, text='Guardar', command=lambda: guardar_actividad(ventana_agregar, self, act_nombre.get(), act_responsable.get(), t_esperado.get(), t_optimista.get(), t_m_probable.get(), t_pesimista.get(), t_acelerado.get(), c_esperado.get(), c_acelerado.get(), list(map(lambda x: x.get() == '', d_variables)), actividades, activity_name))
        guardar.grid(row=4, column=0)

def guardar_actividad(ventana_agregar, parent, act_nombre, act_responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependencias, actividades, activity_name=None):
    dependen = []
    for i, not_checked in enumerate(dependencias):
        if not not_checked:
            dependen.append(actividades[i])
        
    if activity_name:
        # Editar actividad existente
        dm.update_act(activity_name, act_nombre, act_responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependen)
    else:
        # Crear nueva actividad
        dm.create_act(act_nombre, act_responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependen)
    
    parent.refresh_activities()
    ventana_agregar.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ActivityManager(root)
    root.mainloop()
