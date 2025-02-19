import pandas as pd

# Carregar o dataset original
file_path = "MovieRecommendation/dataset/Amazon- Movies and Films.csv"

# Carregar o dataset novamente
df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', low_memory=False)

# Renomear colunas para melhor compatibilidade
df.rename(columns={
    "Title": "title",
    "Movie_Rating": "avg_rating",
    "No_of_Ratings": "num_ratings",
    "Directed_By": "directors",
    "Starring": "starring",
    "ReleaseYear": "release_year",
    "MPAA_Rating": "mpaa_rating",
    "Format": "format",
    "Price": "price_dollars"
}, inplace=True)

# Criar um identificador único para os filmes
df["movie_id"] = range(1, len(df) + 1)

# Criar os três dataframes para exportação

# Tabela movies
movies_df = df[["movie_id", "title", "directors", "starring", "release_year", "mpaa_rating"]]

# Tabela ratings_summary
ratings_df = df[["movie_id", "avg_rating", "num_ratings"]]

# Tabela movie_prices
prices_df = df[["movie_id", "format", "price_dollars"]]

# Salvar os arquivos CSV
movies_csv_path = "MovieRecommendation/dataset/filtrado/movies.csv"
ratings_csv_path = "MovieRecommendation/dataset/filtrado/ratings.csv"
prices_csv_path = "MovieRecommendation/dataset/filtrado/movie_prices.csv"

movies_df.to_csv(movies_csv_path, index=False)
ratings_df.to_csv(ratings_csv_path, index=False)
prices_df.to_csv(prices_csv_path, index=False)
print("Arquivos CSV gerados com sucesso!")
