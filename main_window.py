import tkinter as tk
from gantt_view import Gantt
import activity_creator as ac


window = tk.Tk()

menu = tk.Frame(window)
display = tk.Frame(window)

gantt = Gantt(display)


add_button = tk.Button(menu, text = 'Añadir Actividad', command=lambda:ac.open(window))
gauss_button = tk.Button(menu, text = 'Visualizar\nDiagrama de Gauss')
pert_button = tk.Button(menu, text = 'Visualizar\nPERT-CPM')

menu.grid(column=1, row=0)
display.grid(column=0, row=0, sticky='NSEW')
add_button.grid(column=0, row=0, columnspan=2)
gauss_button.grid(column=0, row=1)
pert_button.grid(column=1, row=1)

window.columnconfigure(0, weight=20)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
menu.columnconfigure(0, weight=1)
menu.columnconfigure(1, weight=1)
menu.rowconfigure(0, weight=1)
menu.rowconfigure(1, weight=1)

display.rowconfigure(0, weight=1)
display.columnconfigure(0, weight=1)

window.mainloop()


