import pandas as pd
import sqlite3

# Conectando ao banco Sqlite
conn = sqlite3.connect('patent.db')


# 1. Remover 0 da frente de numeros
df = pd.read_csv('titles.csv', sep=',', encoding='utf-8')

# 2. Remover chaves e caracteres diversos do title
for char in ['[', ']', '/', '{', '}', ';', ':', '(', ')', '...']:
    df['title'] = df['title'].str.replace(char, '', regex=False)


# 3. Converter numeros float para int em colunas de numeros inteiros
int_columns = ['class', 'group', 'main_group']
df = df.fillna({column: 0 for column in int_columns}).astype({column: 'int32' for column in int_columns})

df.to_sql('patents', con=conn)
