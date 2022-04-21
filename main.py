import pandas as pd


# 1. Remover 0 da frente de numeros
df = pd.read_csv('titles.csv', sep=',', encoding='utf-8')
print(df)

# 2. Remover chaves e caracteres diversos do title

