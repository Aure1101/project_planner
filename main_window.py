from tkinter import *
from tkinter import ttk

window = Tk()


def main_menu():
    add_button = Button(window, text = 'Añadir Actividad')
    gauss_button = Button(window, text = 'Visualizar Diagrama de Gauss')
    pert_button = Button(window, text = 'Visualizar PERT-CPM')


    add_button.grid(column=0, row=0, columnspan=2)
    gauss_button.grid(column=0, row=1)
    pert_button.grid(column=1, row=1)

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)

main_menu()

window.mainloop()