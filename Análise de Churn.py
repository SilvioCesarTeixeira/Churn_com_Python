import pandas as pd
from IPython.display import display
import plotly.express as px


# Dataframe extraído do arquivo .csv
df = pd.read_csv("telecom_users.csv")
display(df)


# Tratamento de dados:
# 1-Eliminar coluna sem rótulo
df = df.drop(["Unnamed: 0"], axis=1)
display(df)

# 2-Alterar o tipo de dado da coluna "TotalGasto" de object para numérico
print(df.info())
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
print(df.info())

# 3-Eliminar coluna "Codigo", que possui somente valores nulos
df = df.dropna(how='all', axis=1)
print(df.info())

# 4-Remover linhas com valores vazios
df = df.dropna()
print(df.info())


# Análise de Dados:
# 1-Contar quantos contratos foram cancelados (coluna Churn), total e percentual
display(df["Churn"].value_counts())
display(df["Churn"].value_counts(normalize=True).map('{:.1%}'.format))

# 2-Apresentar gráficos para 'insights'
for coluna in df:
    if coluna != "IDCliente":
        grafico = px.histogram(df, x=coluna, color="Churn")
        grafico.show()
        display(df.pivot_table(index="Churn", columns=coluna, aggfunc='count')["IDCliente"])

