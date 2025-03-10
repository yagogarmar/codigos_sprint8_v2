import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# Cargar el archivo CSV con datos realistas
data = pd.read_csv("nivel_estres_relacionado.csv")

# Dividir el DataFrame en características y etiquetas
X = data[["horas_sueño", "carga_trabajo", "actividad_fisica"]]
y = data["nivel_estres"]

# Crear una lista de modelos
models = [
    ("decision_tree", DecisionTreeRegressor()),
    ("linear_regression", LinearRegression()),
    ("k_neighbors", KNeighborsRegressor(n_neighbors=5))
]

# Crear un modelo de ensamble con los modelos anteriores
model = VotingRegressor(models)

# Entrenar el modelo con los datos
model.fit(X, y)

# Hacer una predicción con el modelo
horas_sueño = 7  # Horas por noche
carga_trabajo = 7  # Escala de 1 a 10
actividad_fisica = 2  # Días por semana

# Crear un DataFrame con los valores de entrada
entrada = pd.DataFrame([[horas_sueño, carga_trabajo, actividad_fisica]], columns=["horas_sueño", "carga_trabajo", "actividad_fisica"])

nivel_estres_predicho = model.predict(entrada)

print(f"Para {horas_sueño} horas de sueño, una carga de trabajo de {carga_trabajo}/10 y {actividad_fisica} días de actividad física por semana, ")
print(f"se predice un nivel de estrés de {nivel_estres_predicho[0]:.2f}/10")
