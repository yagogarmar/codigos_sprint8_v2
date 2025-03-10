# pip install numpy==1.23.5
# pip install --only-binary :all: pandasai
import pandas as pd
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI


df = pd.read_csv("coin.csv")
#Consigue la key aquí: https://platform.openai.com/account/api-keys
llm = OpenAI(api_token="***")
pandas_ai = PandasAI(llm, verbose=True)
#Pide que haga un gráfico, basándose solo en dos columnas del csv.
response = pandas_ai.run(df, "give me a plot chart only with date data and volume data")
print(response)
