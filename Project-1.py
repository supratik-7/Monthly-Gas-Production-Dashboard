from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk

# Load Data
data = pd.read_csv(r"Project-1\Monthly_Production_Volume_Students.csv")
data['PRODUCTION_DATE'] = pd.to_datetime(data['PRODUCTION_DATE'], format='%d-%b-%y')

data_years = ["All"] + sorted(data['PRODUCTION_DATE'].dt.year.unique(), reverse=True)
data_months = ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
fields = ["All"] + sorted(data['FIELD'].unique())
layer = ["All"] + sorted(data['LAYER_NAME'].unique())

root = Tk()
root.title("GAS PRODUCTION")
root.geometry("1200x900")


selection_var = StringVar(value="Field")

def toggle_combobox():
    if selection_var.get() == "Field":
        field.config(state="readonly")
        layer.config(state="disabled")
    else:
        field.config(state="disabled")
        layer.config(state="readonly")

def toggle_month():
    if year.get() == "All":
        month.config(state="disabled")
    else:
        month.config(state="readonly")

def plot():
    selected_year = year.get()
    selected_month = month.get()
    selected_selection = selection_var.get()
    selected_field = field.get()
    selected_layer = layer.get()
    

    filtered_data = data.copy()

    if selected_year != "All":
        selected_year = int(selected_year)
        filtered_data = filtered_data[filtered_data['PRODUCTION_DATE'].dt.year == selected_year]

    if selected_month != 'All' and month.cget("state") != "disabled":
        month_index = data_months.index(selected_month)
        filtered_data = filtered_data[filtered_data['PRODUCTION_DATE'].dt.month == month_index]

    if selected_selection == 'Field' and selected_field != 'All':
        filtered_data = filtered_data[filtered_data['FIELD'] == selected_field]
    elif selected_selection == 'Layer' and selected_layer != 'All':
        filtered_data = filtered_data[filtered_data['LAYER_NAME'] == selected_layer]

    for widget in f2.winfo_children():
        widget.destroy()

    toolbar_frame = Frame(f2)
    toolbar_frame.pack(side=TOP, fill=X)

    if filtered_data.empty:
        fig, ax = plt.subplots(figsize=(12, 7.5))
        ax.text(0.5, 0.5, 'No Records\nAvailable', 
                fontsize=45, 
                ha='center', 
                va='center', 
                color='gray', 
                fontname='Arial Rounded MT Bold')
        ax.axis('off')

    else:
        gas_volume_by_well = filtered_data.groupby('WELL_NAME')['GAS_VOLUME'].sum()
        fig, ax = plt.subplots(figsize=(12, 7.5))
        plt.subplots_adjust(left=0.069, right=0.97, top=0.926, bottom=0.17)
        x = gas_volume_by_well.index
        y = gas_volume_by_well.values
        bar_width = 0.7
        if len(x) < 4:
            bar_width = 0.2
            ax.set_xlim(-0.5, len(x) - 0.5)
        ax.bar(x, y,
               color='#1f77b4',
               edgecolor='black',
               linewidth=0.5,
               alpha=0.9, width=bar_width)
        ax.plot(x, y,
                color='maroon',
                marker='o',
                linewidth=1)
        if selected_selection == "Field":
            ax.set_title(f'Well-Wise Production (Cumulative) for Field: {selected_field}, Year: {selected_year}, Month: {selected_month}', fontsize=14)
        else:
            ax.set_title(f'Well-Wise Production (Cumulative) for Sand: {selected_layer}, Year: {selected_year}, Month: {selected_month}', fontsize=14)
        ax.set_xlabel('Well Name', fontsize=12, fontname='Arial Black')
        ax.set_ylabel('Total Gas Volume (In SCM)', fontsize=12, fontname='Arial Black')
        ax.tick_params(axis='x', rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=f2)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()
    canvas.get_tk_widget().pack()

    ax.grid(True, which='both', linestyle='--', linewidth=0.7, color='gray')
    ax.set_axisbelow(True)

    y_min, y_max = ax.get_ylim()
    y_range = y_max - y_min
    if y_range > 0:
        tick_interval = y_range / 10
        ticks = [round(y_min + tick_interval * i, 2) for i in range(11)] 
        ax.set_yticks(ticks)
def clear():
    field.current(0)
    layer.current(0)
    year.current(0)
    month.current(0)
    toggle_month()
    for widget in f2.winfo_children():
        widget.destroy()

f3 = Frame(root, bg="#004d40")
f3.pack(pady=10, fill=X)
Label(f3, text="---MONTHLY GAS PRODUCTION DASHBOARD---", bg="#004d40", fg="white", font=("Cooper BT", 27, "bold")).grid(row=0, column=0, padx=20, pady=20)
f3.grid_columnconfigure(0, weight=1)

f1 = Frame(root, bg="#00695c")
f1.pack(side=LEFT, pady=5, padx=10, fill=Y)
f1.grid_columnconfigure(0, weight=1)

Radiobutton(f1, text="Field-Wise", variable=selection_var, value="Field", command=toggle_combobox, bg="#b3c9b5", fg="black", font=("Verdana", 14, "bold"), indicatoron=0).grid(row=0, column=0, sticky=W, padx=10, pady=10)
Radiobutton(f1, text="Sand-Wise", variable=selection_var, value="Layer", command=toggle_combobox, bg="#b3c9b5", fg="black", font=("Verdana", 14, "bold"), indicatoron=0).grid(row=0, column=1, sticky=W, padx=10, pady=10)

Label(f1, text="Field:", bg="#700101", fg="white", font=("Verdana", 14, "bold"), relief=RIDGE, padx=5, pady=5).grid(row=1, column=0, padx=10, pady=10, sticky="e")
field = ttk.Combobox(f1, values=fields, font=("Verdana", 12), state="readonly")
field.grid(row=1, column=1, padx=10, pady=10, sticky="w")
field.current(0)

Label(f1, text="Sand:", bg="#700101", fg="white", font=("Verdana", 14, "bold"), relief=RIDGE, padx=5, pady=5).grid(row=2, column=0, padx=10, pady=10, sticky="e")
layer = ttk.Combobox(f1, values=layer, font=("Verdana", 12), state="disabled")
layer.grid(row=2, column=1, padx=10, pady=10, sticky="w")
layer.current(0)

Label(f1, text="Year:", bg="#700101", fg="white", font=("Verdana", 14, "bold"), relief=RIDGE, padx=5, pady=5).grid(row=3, column=0, padx=10, pady=10, sticky="e")
year = ttk.Combobox(f1, values=data_years, font=("Verdana", 12), state="readonly")
year.grid(row=3, column=1, padx=10, pady=10, sticky="w")
year.bind("<<ComboboxSelected>>", lambda event: toggle_month())
year.current(0)

Label(f1, text="Month:", bg="#700101", fg="white", font=("Verdana", 14, "bold"), relief=RIDGE, padx=5, pady=5).grid(row=4, column=0, padx=10, pady=10, sticky="e")
month = ttk.Combobox(f1, values=data_months, font=("Verdana", 12), state="disabled")
month.grid(row=4, column=1, padx=10, pady=10, sticky="w")
month.current(0)

Button(f1, text="SUBMIT", command=plot, font=("Verdana", 13, "bold"), bg="#0288d1", fg="white", relief=RAISED, bd=3, overrelief=SUNKEN).grid(row=5, column=1, pady=20, ipadx=10, sticky=W)

Button(f1, text="CLEAR", command=clear, font=("Verdana", 13, "bold"), bg="#c62828", fg="white", relief=RAISED, bd=3, overrelief=SUNKEN).grid(row=5, column=1, padx=10, pady=20, ipadx=10, sticky=E)

f2 = Frame(root)
f2.pack(side=RIGHT, pady=20, fill=BOTH, expand=True)
f2.grid_columnconfigure(0, weight=1)

root.bind('<Return>', lambda event: plot())

root.mainloop()
