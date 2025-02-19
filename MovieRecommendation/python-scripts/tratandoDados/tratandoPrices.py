import pandas as pd 

file = "MovieRecommendation/dataset/filtrado/movie_prices.csv"

# Carregar o CSV
df = pd.read_csv(file, encoding="utf-8", on_bad_lines="skip", low_memory=False)

# Substituir valores nulos por 0 em `price_dollars`
df["price_dollars"] = df["price_dollars"].fillna(0)

# Verificar resultado
print(df.info())
print(df.head())

# Salvar o arquivo tratado
df.to_csv("MovieRecommendation/dataset/filtrado/movie_prices.csv", index=False, encoding="utf-8")

print("✅ Dados tratados e exportados para 'movie_prices.csv'")
