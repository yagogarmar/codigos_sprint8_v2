import openai
import pandas as pd

# Configura tu API key de OpenAI
openai.api_key = "***"

# Carga el archivo CSV
# Asegúrate de que el CSV contenga las columnas 'salario' y 'categoria'
df = pd.read_csv("datos.csv")

# Extrae una muestra de los datos para enviar en el prompt (por ejemplo, las primeras 5 filas)
data_sample = df.head(5).to_csv(index=False)

def consulta_pregunta(pregunta):
    # Prepara el prompt combinando la muestra de datos y la consulta
    prompt = f"""
    Tengo los siguientes datos en un archivo CSV:
    {data_sample}
    
    Basándote en estos datos, responde a la siguiente pregunta:
    {pregunta}
    """
    # Llama a la API de OpenAI usando el modelo gpt-3.5-turbo
    respuesta = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "Eres un experto en análisis de datos."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return respuesta.choices[0].message["content"].strip()

# Ejemplo de consulta: Salario máximo
print("Salario máximo:")
print(consulta_pregunta("¿Cuál es el salario máximo?"))

# Ejemplo de consulta: Media del salario por categoría
print("\nMedia del salario por categoría:")
print(consulta_pregunta("¿Cuál es la media del salario por categoría?"))
