import tkinter as tk
import data_manager as dm
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Pert(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.refresh_activities()

    def refresh_activities(self):
        self.grid_forget()
        self.fig = Figure()

        ax = self.fig.add_subplot()

        niveles = {}
        counter = 0

        dependencias = [(actividad[0], dm.get_dependencies(actividad[0]), actividad[2], actividad[3]) for actividad in dm.get_activities_gantt()]
        already = []
        while dependencias != [] and counter<10:
            print(dependencias)
            niveles[counter] = ([],[])
            to_delete = []
            aux = []
            for i, dep in enumerate(dependencias):
                if counter != 0:
                    if dep[1].all() in already:
                        niveles[counter][0].append(dep[0])
                        aux.append(dep[0])
                        niveles[counter][1].append(dep[2]+dep[3])
                        to_delete.append(i)
                else:
                    if len(dep[1]) == 0:
                        niveles[counter][0].append(dep[0])
                        aux.append(dep[0])
                        niveles[counter][1].append(dep[2]+dep[3])
                        to_delete.append(i)

            for i, index in enumerate(to_delete):
                del dependencias[index-i]
            counter += 1
            already += aux
        
        ubicaciones = {}

        for i, nivel in niveles.items():
            ub_nivel = {nivel[0][i]: (x, i) for i, x in enumerate(nivel[1])}
            ubicaciones.update(ub_nivel)

        for h in ubicaciones.keys():
            dependencias = dm.get_dependencies(h)
            print('h', dependencias)
            if len(dependencias) == 0:
                ax.plot([0, ubicaciones[h][0]], [0, ubicaciones[h][1]], color = 'black')
                ax.text((ubicaciones[h][0]/2), ubicaciones[h][1] + 0.1, h)

            else:
                for i, dep in enumerate(dependencias):
                    if i == 0:
                        act_0 = (ubicaciones[dep][0], ubicaciones[dep][1])
                        ax.plot([ubicaciones[dep][0], ubicaciones[h][0]], [ubicaciones[dep][1], ubicaciones[h][1]], linestyle = '-', color = 'black')
                        ax.text((ubicaciones[h][0] + ubicaciones[dep][0])/2, ubicaciones[h][1] + 0.1, h)
                    else:
                        ax.plot([ubicaciones[dep][0], act_0[0]], [ubicaciones[dep][1], act_0[1]], linestyle = '--', color = 'black')

                    #plt.plot([])

        ax.scatter(0,0, color = 'black')

        for i, nivel in niveles.items():
            ax.scatter(nivel[1], np.arange(len(nivel[1])), color = 'black')

        ax.get_yaxis().set_visible(False)

        self.canvas = FigureCanvasTkAgg(self.fig, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0,column=0)

        self.grid(row=0, column=0, sticky='NSEW')
