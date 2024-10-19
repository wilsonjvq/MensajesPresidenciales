import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Función para leer los resúmenes
def leer_resumenes(directorio):
    resumenes = {}
    for anio in range(2021, 2025):
        with open(os.path.join(directorio, f'Resumen_{anio}.txt'), 'r', encoding='utf-8') as file:
            resumenes[anio] = file.read()
    return resumenes

# Función para obtener el mensaje central de un resumen usando KMeans
def obtener_mensaje_central(resumen):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([resumen])

    # Aplicar KMeans
    kmeans = KMeans(n_clusters=1, random_state=0)
    kmeans.fit(X)

    # Obtener los términos y sus pesos
    centroide = kmeans.cluster_centers_[0]
    indices = centroide.argsort()[::-1]
    palabras_clave = vectorizer.get_feature_names_out()[indices][:10]

    return " ".join(palabras_clave)

# Función para obtener aspectos resaltantes de un resumen
def obtener_aspectos_resaltantes(resumen):
    palabras = {}
    for palabra in resumen.split():
        palabra = palabra.lower()
        if len(palabra) > 4:  # Filtrar palabras de más de 4 caracteres
            if palabra in palabras:
                palabras[palabra] += 1
            else:
                palabras[palabra] = 1

    # Ordenar las palabras por su frecuencia
    aspectos_resaltantes = sorted(palabras.items(), key=lambda x: x[1], reverse=True)[:10]
    return aspectos_resaltantes

def main():
    directorio = "C:\\Users\\ACER\\Documents\\0Topicos"  # Cambia esto si es necesario
    resumenes = leer_resumenes(directorio)

    for anio, resumen in resumenes.items():
        # Obtener el mensaje central
        mensaje_central = obtener_mensaje_central(resumen)
        print(f"El mensaje más relevante del año {anio} es: {mensaje_central}.")

        # Obtener aspectos resaltantes
        aspectos_resaltantes = obtener_aspectos_resaltantes(resumen)
        print("Aspectos que resalta frente a los demás mensajes:")
        for palabra, frecuencia in aspectos_resaltantes:
            print(f"{palabra}: {frecuencia}")
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
