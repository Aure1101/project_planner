from tkinter import *
import data_manager as dm

def get_gauss_frame(window):
    gauss_frame = Frame(window)
    activities = dm.get_act()
    act_label = Label(gauss_frame, text='Actividad')
    resp_label = Label(gauss_frame, text='Responsable')
    time_label = Label(gauss_frame, text='Tiempo')
    
    max_time = max(activities[:,2] + activities[:,3])

    act_label.grid(row=0, column=0, rowspan=2, sticky='SNEW')
    resp_label.grid(row=0, column=1, rowspan=2, sticky='SNEW')
    time_label.grid(row=0, column=2, columnspan=max_time, sticky='SNEW')

    labels_time = {}
    for i in range(max_time):
        labels_time[i] = Label(gauss_frame, text=i)
        labels_time[i].grid(row = 1, column=i+2, sticky='W')

    actividades_rows = {}
    colores = ['red', 'blue', 'yellow', 'pink', 'purple']
    
    for i, actividad in enumerate(activities):
        act = Label(gauss_frame, text=actividad[0])
        resp = Label(gauss_frame, text=actividad[1])
        tiempo = Frame(gauss_frame, bg = colores[i%5])
        act.grid(row=i+2, column=0)
        resp.grid(row=i+2, column=1)
        tiempo.grid(row=i+2, column=actividad[2]+2, columnspan=actividad[3], sticky='SNEW')
        actividades_rows[i] = [act, resp, tiempo]
    
    for column in range(gauss_frame.grid_size()[0]):
        gauss_frame.columnconfigure(column, weight=1)

    for row in range(gauss_frame.grid_size()[1]):
        gauss_frame.rowconfigure(row, weight=1)

    gauss_frame.grid(column=0, row=0, sticky='SNEW')


a = Tk()
a.columnconfigure(0, weight=1)
a.rowconfigure(0, weight=1)
get_gauss_frame(a)


a.mainloop()