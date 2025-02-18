import pandas as pd

df = pd.read_csv("dim_produto.csv")

# colunas = [
#     'discounted_price',
#     'actual_price'
# ]

# # removendo os simbolos de moeda
# df[colunas] = df[colunas].replace('[\₹,]', '', regex=True)
# df[colunas] = df[colunas].astype(float)

# df.to_csv("dim_produto.csv", index=False)

# # removendo o simbolo de %
# df['discount_percentage'] = df['discount_percentage'].str.replace('%', '')
# df['discount_percentage'] = df['discount_percentage'].astype(float)

# df.to_csv("dim_produto.csv", index=False)


# # substituindo nulos por 0 na coluna rating_count
# df['rating_count'] = df['rating_count'].fillna(0)
# df.to_csv("dim_produto.csv", index=False)
# # convertendo rating count para int 
# df['rating_count'] = df['rating_count'].str.replace(',', '')
# df['rating_count'] = df['rating_count'].astype(int)

# df.to_csv("dim_produto.csv", index=False)

# # checando a coluna rating
# print(df['rating'].unique())

# for index in df.index:
#     if df.loc[index, 'rating'] == '.':
#         df.loc[index, 'rating'] = 0

# df['rating'] = df['rating'].astype(float)

# df.to_csv("dim_produto.csv", index=False)