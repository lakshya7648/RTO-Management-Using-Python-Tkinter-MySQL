import tkinter as tk
import matplotlib
import pymysql as sql

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class licenseanalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Data Analysis')
        p='PERMANENT LICENSE'
        d='LEARNING LICENSE'
        vp=0
        vf=0

        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select License_type from license"
        cur = conn.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        for row in data:
            for col in row:
                if col == 'Permanent License':
                    vp += 1
                if col == 'Learning License':
                    vf += 1
                if col == None:
                    un=un+1
        conn.close()

        # get data from table
        # prepare data
        data = {
              p:vp,
            d:vf,

        }
        Applicants = data.keys()
        License_type = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(Applicants, License_type)
        axes.set_title('RTO License Analysis')
        axes.set_ylabel('Applicants')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


class cityanalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Data Analysis')
        lu = 'LUCKNOW'
        math = 'MATHURA'
        kan = 'KANPUR'
        var='VARANASI'
        un='UNNAO'
        oth='OTHERS'

        l=0
        m=0
        k=0
        u=0
        v=0
        o=0

        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select City from license"
        cur = conn.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        for row in data:
            for col in row:
                if col=='LUCKNOW' or col=='VARANASI' or col=='KANPUR'or col=='UNNAO'or col=='MATHURA':
                    if col=='LUCKNOW':
                        l+=1
                    if  col=='VARANASI':
                        v+=1
                    if col=='KANPUR':
                        k+=1
                    if col=='UNNAO':
                        u+=1
                    if col=='MATHURA':
                        m=m+1
                else:
                    o+=1

        conn.close()
        # get data from table
        # prepare data
        data = {
              lu:l,
            math:m,
            var:v,
            kan:k,
            un:u,
            oth:o,
        }
        vehicleclass = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(vehicleclass, popularity)
        axes.set_title('City Based Analysis')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


class vehicleanalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Data Analysis')
        ld = 'Light Duty'
        mhd = 'Medium-Heavy Duty'
        hd = 'Heavy Duty'

        ldn = 0
        mhdn = 0
        hdn = 0
        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select Vehicle_class from rc"
        cur = conn.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        for row in data:
            for col in row:
                if col=='LIGHT DUTY':
                    ldn=ldn+1
                if  col=='MEDIUM HEAVY DUTY':
                    mhdn=mhdn+1
                if col=='HEAVY DUTY':
                    hdn=hdn+1
        conn.close()
        # get data from table
        # prepare data
        data = {
              ld:ldn,
            mhd:mhdn,
            hd:hdn,
        }
        vehicleclass = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(vehicleclass, popularity)
        axes.set_title('Vehicle Class Based Analysis')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



class fuelanalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Data Analysis')
        p='Petrol'
        d='Diesel'
        c='C.N.G'

        vp=0
        vd=0
        vcng=0

        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select Fuel_type from rc"
        cur = conn.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        print(data)
        for row in data:
            for col in row:
                if col == 'PETROL':
                    vp = vp + 1
                if col == 'DIESEL':
                    vd+=1
                if col == 'C.N.G':
                    vcng+=1
        conn.close()

        # get data from table
        # prepare data
        data = {
              p:vp,
            d:vd,
            c:vcng,
            #'Petrol': 5,
            #'Diesel':24,
            #'CNG': 10.46,
        }
        Fueltype = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(Fueltype, popularity)
        axes.set_title('Fuel Based Analysis')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


class testanalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Data Analysis')
        p='PASSED'
        d='FAILED'
        vp=0
        vf=0

        conn = sql.connect(host="localhost", user="root", password="", database="minor_project")
        qry = "select Test from license"
        cur = conn.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        for row in data:
            for col in row:
                if col == 'PASS':
                    vp += 1
                if col == 'FAIL':
                    vf += 1
                if col == None:
                    un=un+1
        conn.close()

        # get data from table
        # prepare data
        data = {
              p:vp,
            d:vf,

        }
        Result = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(Result, popularity)
        axes.set_title('RTO Test Analysis')
        axes.set_ylabel('Candidates')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == '__main__':
    appf = fuelanalysis()
    appv= vehicleanalysis()
    apptest= testanalysis()
    appcity= cityanalysis()

    appf.mainloop()
    appv.mainloop()
    apptest.mainloop()
    #appmanu.mainloop()
   # appcity.mainloop()
