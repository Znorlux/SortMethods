import requests
import json
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker

from QuickSort import quick_sort
from MergeSort import merge_sort
from BucketSort import bucket_sort
from HeapSort import heap_sort 
from CountingSort import counting_sort
from RadixSort import radix_sort

# Consumo de la API de datosgov
def obtener_datos():

    params = {
        "$limit": 100 #Limite de filas que queremos tener de la API
    }
    response = requests.get(url="https://www.datos.gov.co/resource/dyy8-9s4r.json", params=params)
    datos = json.loads(response.text)
    return pd.DataFrame(datos), datos

def ordenamiento():
    metodo_ordenamiento = metodo_combobox.get()
    columna_ordenar = columna_combobox.get()

    #Metodos de ordenamiento elegidos por el usuario
    if metodo_ordenamiento == "QuickSort":
        lista_ordenada = quick_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    elif metodo_ordenamiento == "MergeSort":
        lista_ordenada = merge_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    elif metodo_ordenamiento == "HeapSort":
        lista_ordenada = heap_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    elif metodo_ordenamiento == "CountingSort":
        lista_ordenada = counting_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    elif metodo_ordenamiento == "RadixSort":
        lista_ordenada = radix_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    elif metodo_ordenamiento == "BucketSort":
        lista_ordenada = bucket_sort(lista_datos, columna_ordenar)
        df_ordenado = pd.DataFrame(lista_ordenada)

    return df_ordenado

def mostrar_resultados():
    columna_ordenar = columna_combobox.get() #Obtenemos la columna que decidió ordenar el usuario

    # En caso de que la API tenga valores numericos que realmente están guardados como string, los volvemos int
    for item in lista_datos:
        for key, value in item.items():
            if isinstance(value, str) and value.isdigit():
                item[key] = int(value)


    df_ordenado = ordenamiento()

    # Grafico de barras para visualizar los datos y sus valores
    figure = Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    ax.bar(df_ordenado.index, df_ordenado[columna_ordenar])
    ax.set_xlabel("Índice")
    ax.set_ylabel(columna_ordenar)

    #En caso de que haya un grafico ya hecho, lo borraremos (ocurre despues del primer uso)
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(figure, master=frame_grafico)
    canvas.get_tk_widget().pack()
    
    # Creamos una tabla la cual simplemente será una vista de nuestro dataframe con nuestros datos
    treeview.delete(*treeview.get_children())
    for index, row in df_ordenado.iterrows():
        treeview.insert("", "end", values=[index] + list(row))


'''
███████╗ ██████╗ ██████╗ ████████╗    ███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝    ████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗██╔════╝
███████╗██║   ██║██████╔╝   ██║       ██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║███████╗
╚════██║██║   ██║██╔══██╗   ██║       ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║╚════██║
███████║╚██████╔╝██║  ██║   ██║       ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝███████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝                                                                                                                                                                                                                    
'''
#Codigo principal
if __name__ == '__main__':
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
    metodo_combobox = ttk.Combobox(frame_principal, values=["QuickSort","MergeSort","HeapSort","CountingSort","RadixSort","BucketSort"])
    
    columna_label = ttk.Label(frame_principal, text="Columna a Ordenar:")

    # Limpiar los nombres de las columnas
    columnas_limpias = [col.strip("',") for col in datos.columns]
    columna_combobox = ttk.Combobox(frame_principal, values=columnas_limpias)

    ordenar_button = ttk.Button(frame_principal, text="Ordenar", command=mostrar_resultados)

    frame_grafico = ttk.Frame(window)
    frame_grafico.pack()


    # Creacion de la tabla que muestra los datos
    treeview = ttk.Treeview(frame_principal, columns=["Indice"] + list(datos.columns), show="headings")
    for col in ["Indice"] + list(datos.columns):
        treeview.heading(col, text=col)
        treeview.column(col, width=100)
        
    # Widgets de la ventana
    metodo_label.grid(row=0, column=0)
    metodo_combobox.grid(row=0, column=1)
    columna_label.grid(row=1, column=0)
    columna_combobox.grid(row=1, column=1)
    ordenar_button.grid(row=2, columnspan=2)
    treeview.grid(row=3, columnspan=2)

    window.mainloop()
