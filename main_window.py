import tkinter as tk
import tkinter.ttk as ttk
from gantt_view import Gantt
import activity_creator as ac
from pert_view import Pert

window = tk.Tk()

menu = tk.Frame(window)
display = tk.Frame(window)

in_use = Gantt(display)
add_button = tk.Button(menu, text = 'Añadir Actividad', command=lambda:ac.open_(in_use))

def set_pert():
    global in_use
    display.grid_forget()
    in_use = Pert(display)
    display.rowconfigure(0, weight=1)
    display.columnconfigure(0, weight=1)
    display.grid(column=0, row=0, sticky='NSEW')


def set_gantt():
    global in_use, display
    display.grid_forget()
    in_use = Gantt(display)
    display.rowconfigure(0, weight=1)
    display.columnconfigure(0, weight=1)
    display.grid(column=0, row=0, sticky='NSEW')



gauss_button = tk.Button(menu, text = 'Visualizar\nDiagrama de Gantt', command = set_gantt)
pert_button = tk.Button(menu, text = 'Visualizar\nPERT-CPM', command = set_pert)

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


