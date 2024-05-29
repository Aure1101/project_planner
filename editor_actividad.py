import tkinter as tk
import data_manager as dm

class ActivityEditor:
    def __init__(self, master, gantt, activity_values):
        self.master = master
        self.gantt = gantt
        self.activity_values = activity_values
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Editar Actividad")

        labels = [
            "Nombre", "Responsable", "Tiempo Esperado", "Tiempo Optimista",
            "Tiempo Más Probable", "Tiempo Pesimista", "Tiempo Acelerado",
            "Fecha Inicio", "Costo Esperado", "Costo Acelerado", "Porcentaje Terminado"
        ]

        self.entries = []

        for i, label in enumerate(labels):
            tk.Label(self.master, text=label).grid(row=i, column=0)
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1)
            entry.insert(0, self.activity_values[i])
            self.entries.append(entry)

        tk.Button(self.master, text="Guardar", command=self.save_changes).grid(row=len(labels), column=0, columnspan=2)

    def save_changes(self):
        new_values = [entry.get() for entry in self.entries]

        # Actualizar el DataFrame con los nuevos valores
        df = dm.get_all_activities()
        activity_index = df.index[df['nombre_actividad'] == self.activity_values[0]].tolist()[0]
        df.loc[activity_index] = new_values
        dm.update_activities_dataframe(df)

        # Actualizar el Gantt con los nuevos datos
        if self.gantt:
            self.gantt.refresh_activities()

        self.master.destroy()

class ActivitySelector:
    def __init__(self, master, gantt):
        self.master = master
        self.gantt = gantt
        self.activities = None  # Inicializar como None
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Seleccionar Actividad")

        tk.Label(self.master, text="Seleccione una actividad para editar").pack()

        self.activity_listbox = tk.Listbox(self.master)
        self.activity_listbox.pack()

        # Cargar actividades desde el DataFrame
        self.activities = dm.get_all_activities()  # Guardar las actividades en el atributo de instancia
        for _, row in self.activities.iterrows():
            self.activity_listbox.insert(tk.END, row['nombre_actividad'])

        tk.Button(self.master, text="Editar", command=self.edit_activity).pack()

    def edit_activity(self):
        selected_index = self.activity_listbox.curselection()
        if selected_index:
            activity_name = self.activity_listbox.get(selected_index[0])
            activity_row = self.activities[self.activities['nombre_actividad'] == activity_name].iloc[0].tolist()  # Obtener la fila correspondiente a la actividad
            editor_window = tk.Toplevel(self.master)
            ActivityEditor(editor_window, self.gantt, activity_row)

def open_selector(gantt):
    selector_window = tk.Toplevel()
    ActivitySelector(selector_window, gantt)

if __name__ == "__main__":
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Administrador de Actividades")

    # Agregar un botón para abrir el selector de actividades
    tk.Button(root, text="Seleccionar Actividad para Editar", command=lambda: open_selector(None)).pack()

    # Ejecutar el loop principal de Tkinter
    root.mainloop()
