import tkinter as tk
import tkinter.ttk as ttk
from gantt_view import Gantt
import activity_creator as ac
from editor_actividad import open_selector

window = tk.Tk()

menu = tk.Frame(window)
display = tk.Frame(window)

gantt = Gantt(display)

add_button = tk.Button(menu, text='Añadir Actividad', command=lambda: ac.open_(gantt))
edit_button = tk.Button(menu, text='Editar Actividad', command=lambda: open_selector(gantt))
gauss_button = tk.Button(menu, text='Visualizar\nDiagrama de Gantt')
pert_button = tk.Button(menu, text='Visualizar\nPERT-CPM')

menu.grid(column=1, row=0)
display.grid(column=0, row=0, sticky='NSEW')
add_button.grid(column=0, row=0, columnspan=2)
edit_button.grid(column=0, row=1, columnspan=2)
gauss_button.grid(column=0, row=2)
pert_button.grid(column=1, row=2)

window.columnconfigure(0, weight=20)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
menu.columnconfigure(0, weight=1)
menu.columnconfigure(1, weight=1)
menu.rowconfigure(0, weight=1)
menu.rowconfigure(1, weight=1)
menu.rowconfigure(2, weight=1)

display.rowconfigure(0, weight=1)
display.columnconfigure(0, weight=1)

window.mainloop()
