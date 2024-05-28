import tkinter as tk
from tkinter import Menu, simpledialog, messagebox

class ActivityManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Actividades")
        self.activities = {}  # Diccionario para almacenar actividades por nombre

        # Crear el menú
        self.menu = Menu(root, tearoff=0)
        self.menu.add_command(label="Editar", command=self.edit_activity)
        self.menu.add_command(label="Borrar", command=self.delete_activity)
        
        # Crear la lista de actividades
        self.activity_listbox = tk.Listbox(root)
        self.activity_listbox.pack(fill=tk.BOTH, expand=1)
        self.activity_listbox.bind("<Button-3>", self.show_context_menu)

        # Botón para agregar una nueva actividad
        self.add_button = tk.Button(root, text="Agregar Actividad", command=self.add_activity)
        self.add_button.pack()

    def show_context_menu(self, event):
        try:
            self.selected_activity = self.activity_listbox.get(self.activity_listbox.curselection())
            self.menu.post(event.x_root, event.y_root)
        except tk.TclError:
            pass

    def add_activity(self):
        name = simpledialog.askstring("Nombre de Actividad", "Ingrese el nombre de la actividad:")
        if name:
            self.activities[name] = {
                "responsable": "",
                "t_esperado": 0,
                "t_optimista": 0,
                "t_m_probable": 0,
                "t_pesimista": 0,
                "t_acelerado": 0,
                "c_esperado": 0,
                "c_acelerado": 0,
                "dependencias": []
            }
            self.refresh_activities()

    def edit_activity(self):
        if self.selected_activity:
            # Aquí puedes agregar un diálogo para editar los detalles de la actividad
            responsible = simpledialog.askstring("Editar Responsable", "Ingrese el responsable:", initialvalue=self.activities[self.selected_activity]['responsable'])
            self.activities[self.selected_activity]['responsable'] = responsible
            self.refresh_activities()

    def delete_activity(self):
        if self.selected_activity:
            del self.activities[self.selected_activity]
            self.refresh_activities()

    def refresh_activities(self):
        self.activity_listbox.delete(0, tk.END)
        for name in self.activities:
            self.activity_listbox.insert(tk.END, name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ActivityManager(root)
    root.mainloop()
