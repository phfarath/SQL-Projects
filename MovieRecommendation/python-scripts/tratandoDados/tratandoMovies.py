import pandas as pd 

file = "MovieRecommendation/dataset/filtrado/movies.csv"

df = pd.read_csv(file, encoding='utf-8', on_bad_lines='skip', low_memory=False)

# print(df.info())
# print(df.columns)

# preencher valores nulos ou ausentes
df['directors'] = df['directors'].fillna('Desconhecido')
df['starring'] = df['starring'].fillna('Desconhecido')
df['mpaa_rating'] = df['mpaa_rating'].fillna('Não classificado')

# converter release_year para int
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')  # Converte não numéricos para NaN
df['release_year'] = df['release_year'].astype('Int64')  # Usa Int64 do Pandas para suportar valores nulos
# removendo possiveis duplicatas
df.drop_duplicates(inplace=True)

print(df.info())

df.to_csv('MovieRecommendation/dataset/filtrado/movies.csv', index=False, encoding='utf-8')
print("✅ Dados tratados e exportados para 'movies_clean.csv'")