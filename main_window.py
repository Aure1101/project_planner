import tkinter as tk
import tkinter.ttk as ttk
from gantt_view import Gantt
import activity_creator as ac


window = tk.Tk()

menu = tk.Frame(window)
display = tk.Frame(window)

gantt = Gantt(display)

add_button = tk.Button(menu, text = 'Añadir Actividad', command=lambda:ac.open_(window))
#En lugar de estos botones podriamos usar pestañas para cambiar entre las vistas
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

#ventana_agregar =  tk.Toplevel(window)
#ventana_agregar.title('Añadir Actividad')

#-------------------------------------------------Datos Generales------------------------------------------------------------
#datos_actividad = ttk.Frame(ventana_agregar).grid(row = 0, column = 0)

#act_nombre_label = ttk.Label(datos_actividad, text='Actividad').grid(row=0, column=0)
#act_nombre = tk.StringVar()
#act_nombre_entry = ttk.Entry(datos_actividad, textvariable=act_nombre).grid(row = 1, column = 0)
#
#act_responsable_label = ttk.Label(datos_actividad, text='Responsable').grid(row =0, column=1)
#act_responsable = tk.StringVar()
#act_responsable_entry = ttk.Entry(datos_actividad, textvariable=act_responsable).grid(row = 1, column=1)
#
##----------------------------------------------Datos Tiempos-------------------------------------------------------------------
#datos_tiempos = tk.LabelFrame(ventana_agregar, text='Tiempo').grid(row=1, column=0)
#
#t_esperado_label = tk.Label(datos_tiempos, text='Tiempo Esperado').grid(row=0, column=1)
#t_esperado = tk.StringVar()
#t_esperado_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_esperado).grid(row=1, column=1,)
#
#t_optimista_label = tk.Label(datos_tiempos, text='Tiempo\nOptimista').grid(row=2, column=0)
#t_optimista = tk.StringVar()
#t_optimista_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_optimista).grid(row=3, column=0)
#
#t_m_probable_label = tk.Label(datos_tiempos, text='Tiempo\nMas Probable').grid(row=2, column=1)
#t_m_probable = tk.StringVar()
#t_m_probable_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_m_probable).grid(row=3, column=1)
#
#t_pesimista_label = tk.Label(datos_tiempos, text='Tiempo\nPesimista').grid(row=2, column=2)
#t_pesimista = tk.StringVar()
#t_pesimista_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_pesimista).grid(row=3, column=2)
#
#t_acelerado_label = tk.Label(datos_tiempos, text='Tiempo\nAcelerado').grid(row=4, column=1)
#t_acelerado = tk.StringVar()
#t_acelerado_entry = tk.Spinbox(datos_tiempos, from_=1, to=100, textvariable=t_acelerado).grid(row=4, column=1)
#
##-------------------------------------------------Datos Costos--------------------------------------------------
#datos_costos = tk.LabelFrame(ventana_agregar, text='Costos').grid(row=2, column=0)
#
#c_esperado_label = tk.Label(datos_costos, text='Costo Esperado').grid(row=0, column=0)
#c_esperado = tk.StringVar()
#c_esperado_entry = tk.Spinbox(datos_costos, from_=0.0, textvariable=c_esperado).grid(row=1, column=0)
#
#c_acelerado_label = tk.Label(datos_costos, text='Costo Acelerado').grid(row=0, column=1)
#c_acelerado = tk.StringVar()
#c_acelerado_entry = tk.Spinbox(datos_costos, from_=0.0, textvariable=c_acelerado).grid(row=1, column=1)
#
##------------------------------------------------Dependencias-------------------------------------------------
#dependencias = tk.LabelFrame(ventana_agregar).grid(row=3, column=0)
#
#print(ventana_agregar.grid_size())
#
window.mainloop()


