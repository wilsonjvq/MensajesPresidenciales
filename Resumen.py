import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Función para contar las palabras en un archivo
def contar_palabras(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Lee el texto y convierte a minúsculas
    words = text.split()
    
    # Filtra palabras con menos de 4 caracteres
    words = [word for word in words if len(word) > 4]
    
    # Cuenta las palabras
    word_counts = Counter(words)
    
    # Obtiene las 20 palabras más comunes
    return word_counts.most_common(20)

# Función para graficar las palabras
def graficar_palabras(word_counts, year):
    words, counts = zip(*word_counts)  # Desempaqueta palabras y conteos

    plt.figure(figsize=(12, 8))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title(f'20 Palabras más comunes en Resumen {year}')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajusta la gráfica para que no se corte
    plt.savefig(f'grafica_{year}.png')  # Guarda la gráfica como imagen
    plt.close()  # Cierra la figura para liberar memoria

# Lista de archivos y años
resumenes = {
    'Resumen_2021.txt': '2021',
    'Resumen_2022.txt': '2022',
    'Resumen_2023.txt': '2023',
    'Resumen_2024.txt': '2024',
}

# Procesar cada resumen
for file_name, year in resumenes.items():
    if os.path.exists(file_name):  # Verifica si el archivo existe
        word_counts = contar_palabras(file_name)  # Cuenta las palabras
        graficar_palabras(word_counts, year)  # Genera y guarda la gráfica
    else:
        print(f'El archivo {file_name} no existe.')
