from tkinter import *
from tkinter import ttk
import gauss_frame as gf

window = Tk()

main_menu = Frame(window)

def change_gauss():
    main_menu.grid_forget()
    gf.get_gauss_frame(window)

add_button = Button(main_menu, text = 'Añadir Actividad')
gauss_button = Button(main_menu, text = 'Visualizar Diagrama de Gauss', command=change_gauss)
pert_button = Button(main_menu, text = 'Visualizar PERT-CPM')

main_menu.grid(column=0, row=0)
add_button.grid(column=0, row=0, columnspan=2)
gauss_button.grid(column=0, row=1)
pert_button.grid(column=1, row=1)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
main_menu.columnconfigure(0, weight=1)
main_menu.columnconfigure(1, weight=1)
main_menu.rowconfigure(0, weight=1)
main_menu.rowconfigure(1, weight=1)

window.mainloop()


