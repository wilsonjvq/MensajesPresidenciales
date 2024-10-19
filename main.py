import PyPDF2
from transformers import pipeline

def leer_pdf(archivo):
    """Lee el contenido de un archivo PDF."""
    texto = ""
    with open(archivo, "rb") as f:
        lector = PyPDF2.PdfReader(f)
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def analizar_mensaje(texto):
    """Analiza el texto y devuelve el resumen."""
    resumen_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
    max_chunk_length = 1000  # Ajusta el tamaño de cada parte
    partes = [texto[i:i + max_chunk_length] for i in range(0, len(texto), max_chunk_length)]
    
    resúmenes = []
    for i, parte in enumerate(partes):
        print(f"Resumiendo parte {i + 1} de {len(partes)} con {len(parte)} caracteres...")
        resumen = resumen_pipeline(parte, max_length=150, min_length=30, do_sample=False)
        resúmenes.append(resumen[0]['summary_text'])
    
    return " ".join(resúmenes)

def main():
    """Función principal para leer y analizar los mensajes presidenciales."""
    archivos = [
        "Mensaje_a_la_Nacion_2021.pdf",
        "Mensaje_a_la_Nacion_2022.pdf",
        "Mensaje_a_la_Nacion_2023.pdf",
        "Mensaje_a_la_Nacion_2024.pdf"
    ]
    
    resultados = {}
    
    for archivo in archivos:
        print(f"Leyendo archivo: {archivo}")
        contenido = leer_pdf(archivo)
        print(f"Analizando contenido de {archivo}...")
        resumen = analizar_mensaje(contenido)
        resultados[archivo] = resumen
        print(f"Resumen de {archivo}:\n{resumen}\n")
    
    # Guardar los resultados en un archivo de texto
    with open("resultados.txt", "w", encoding="utf-8") as f:
        for archivo, resumen in resultados.items():
            f.write(f"Resumen de {archivo}:\n{resumen}\n\n")
    
    print("Análisis completo. Resultados guardados en resultados.txt.")

if __name__ == "__main__":
    main()
