import tkinter as tk
from tkinter import Menu, simpledialog, messagebox
import data_manager as dm

#ventana_editar = None

def open_(parent):
    ventana_editar =  tk.Toplevel(parent)
    ventana_editar.title('Editar Actividad')
    
    menu = Menu(root, tearoff=0)
    menu.add_command(label="Editar", command=editar_actividad(parent))
    menu.add_command(label="Borrar", command=delete_activity(parent))
     # Crear la lista de actividades
    activity_listbox = tk.Listbox(root)
    activity_listbox.pack(fill=tk.BOTH, expand=1)
    activity_listbox.bind("<Button-3>", show_context_menu(parent))





def show_context_menu(self, event):
        try:
            self.selected_activity = self.activity_listbox.get(self.activity_listbox.curselection())
            self.menu.post(event.x_root, event.y_root)
        except tk.TclError:
            pass


def delete_activity(self):
    if self.selected_activity:
        del self.activities[self.selected_activity]
        self.refresh_activities()

def editar_actividad(parent, act_nombre, act_responsable, t_esperado, t_optimista, t_m_probable, t_pesimista, t_acelerado, c_esperado, c_acelerado, dependencias, actividades):
    # Encontrar las actividades de las que depende esta actividad
    dependen = []
    for i, not_checked in enumerate(dependencias):
        if not not_checked:
            dependen.append(actividades[i])

    # Obtener la actividad existente
    actividad = dm.get_act_by_name(act_nombre)
    
    if actividad:
        # Actualizar los datos de la actividad
        actividad.responsable = act_responsable
        actividad.t_esperado = t_esperado
        actividad.t_optimista = t_optimista
        actividad.t_m_probable = t_m_probable
        actividad.t_pesimista = t_pesimista
        actividad.t_acelerado = t_acelerado
        actividad.c_esperado = c_esperado
        actividad.c_acelerado = c_acelerado
        actividad.dependencias = dependen

        # Guardar los cambios en el gestor de datos
        dm.update_act(actividad)
    else:
        print(f"Actividad '{act_nombre}' no encontrada")

    # Refrescar la lista de actividades en la interfaz
    parent.refresh_activities()


