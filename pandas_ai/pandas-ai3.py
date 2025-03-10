import openai
import pandas as pd
import backoff  # Importamos la librería para el backoff

# Configura tu API key de OpenAI
openai.api_key = "***"

# Carga el archivo CSV
df = pd.read_csv("datos.csv")

# Extrae una muestra de los datos para enviar en el prompt (por ejemplo, las primeras 5 filas)
data_sample = df.head(5).to_csv(index=False)

# Función que envuelve la llamada a la API y aplica backoff en caso de RateLimitError
@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_time=60, max_tries=6)
def completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

def consulta_pregunta(pregunta):
    # Prepara el prompt combinando la muestra de datos y la consulta
    prompt = f"""
    Tengo los siguientes datos en un archivo CSV:
    {data_sample}
    
    Basándote en estos datos, responde a la siguiente pregunta:
    {pregunta}
    """
    # Llama a la función con backoff para gestionar posibles RateLimitError
    respuesta = completions_with_backoff(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1,
    )
    return respuesta.choices[0].message["content"].strip()

# Ejemplo de consulta: Salario máximo
print("Salario máximo:")
print(consulta_pregunta("¿Cuál es el salario máximo?"))
