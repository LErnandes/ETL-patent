import pandas as pd


# 1. Remover 0 da frente de numeros
df = pd.read_csv('titles.csv', sep=',', encoding='utf-8')

# 2. Remover chaves e caracteres diversos do title
for char in ['[', ']', '/', '{', '}', ';', ':', '(', ')', '...']:
    df['title'] = df['title'].str.replace(char, '', regex=False)


# 3. Converter numeros float para int em colunas de numeros inteiros


print(df)
