import tkinter as tk
import data_manager as dm


class Gantt(tk.Frame):
    def __init__(self, parent, color_pallete = ['red', 'blue', 'yellow', 'pink', 'purple']):
        super().__init__(parent)
        self.color_pallete = color_pallete
        self.refresh_activities()
        self.grid(row=0, column=0, sticky='NSEW')



    def refresh_activities(self):
        self.grid_forget()
        activities = dm.get_activities_gantt()

        max_time = max(activities[:,2] + activities[:,3])

        act_label = tk.Label(self, text='Actividad').grid(row=0, column=0, rowspan=2, sticky='SNEW')
        resp_label = tk.Label(self, text='Responsable').grid(row=0, column=1, rowspan=2, sticky='SNEW')
        time_label = tk.Label(self, text='Tiempo').grid(row=0, column=2, columnspan=max_time, sticky='SNEW')
        weeks = [tk.Label(self, text=i).grid(row = 1, column=i+2, sticky='E') for i in range(1, max_time)]

        activity_rows = [(tk.Label(self, text=activity[0]).grid(row=i+2, column=0), tk.Label(self, text=activity[1]).grid(row=i+2, column=1), tk.Frame(self, bg = self.color_pallete[i%5]).grid(row=i+2, column=activity[2]+3, columnspan=activity[3], sticky='SNEW')) for i, activity in enumerate(activities)]

        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)

        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)
