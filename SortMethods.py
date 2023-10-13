import requests
import json
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker
from QuickSort import quick_sort as quick
from MergeSort import merge_sort
# Consumo de la API de datosgov
def obtener_datos():
    response = requests.get(url="https://www.datos.gov.co/resource/axk9-g2nh.json")
    datos = json.loads(response.text)
    return pd.DataFrame(datos), datos

def ordenamiento():
    metodo_ordenamiento = metodo_combobox.get()
    columna_ordenar = columna_combobox.get()

    #Metodos de ordenamiento elegidos por el usuario
    df_ordenado = None
    if metodo_ordenamiento == "QuickSort":
        lista_ordenada = quick(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    if metodo_ordenamiento == "MergeSort":
        lista_ordenada = merge_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)
    
    return df_ordenado
def mostrar_resultados():
    columna_ordenar = columna_combobox.get()
    df_ordenado = ordenamiento()
    
    # Crear un gráfico de barras
    figure = Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    ax.bar(df_ordenado.index, df_ordenado[columna_ordenar])
    ax.set_xlabel("Índice")
    ax.set_ylabel(columna_ordenar)

    # Configurar los intervalos en el eje Y
    intervals = [0, 2, 4, 6, 8, 10]  # Define los intervalos deseados en el eje Y
    ax.yaxis.set_major_locator(ticker.FixedLocator(intervals))  # Establece los intervalos personalizados

    # Actualizar las etiquetas en el eje Y (opcional)
    ax.set_yticklabels(intervals)

    canvas = FigureCanvasTkAgg(figure, master=frame_grafico)
    canvas.get_tk_widget().pack()
    
    # Crear una tabla
    treeview.delete(*treeview.get_children())
    for index, row in df_ordenado.iterrows():
        treeview.insert("", "end", values=[index] + list(row))

# Crear la ventana principal
window = tk.Tk()
window.title("Aplicación de Ordenamiento")

# Obtener los datos iniciales
datos, lista_datos = obtener_datos()

# Crear el marco principal
frame_principal = ttk.Frame(window)
frame_principal.pack()

# Crear los widgets
metodo_label = ttk.Label(frame_principal, text="Método de Ordenamiento:")
metodo_combobox = ttk.Combobox(frame_principal, values=["QuickSort","MergeSort"])  # Agrega otros métodos si es necesario
 
columna_label = ttk.Label(frame_principal, text="Columna a Ordenar:")
# Limpiar los nombres de las columnas
columnas_limpias = [col.strip("',") for col in datos.columns]
columna_combobox = ttk.Combobox(frame_principal, values=columnas_limpias)

ordenar_button = ttk.Button(frame_principal, text="Ordenar", command=mostrar_resultados)

frame_grafico = ttk.Frame(window)
frame_grafico.pack()


# Crear una tabla mejor formateada
treeview = ttk.Treeview(frame_principal, columns=["Index"] + list(datos.columns), show="headings")
for col in ["Index"] + list(datos.columns):
    treeview.heading(col, text=col)
    treeview.column(col, width=100)
    
# Colocar los widgets en la ventana
metodo_label.grid(row=0, column=0)
metodo_combobox.grid(row=0, column=1)
columna_label.grid(row=1, column=0)
columna_combobox.grid(row=1, column=1)
ordenar_button.grid(row=2, columnspan=2)
treeview.grid(row=3, columnspan=2)

window.mainloop()
