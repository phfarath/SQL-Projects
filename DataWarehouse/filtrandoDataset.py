import pandas as pd

# Lê o arquivo CSV mestre que contém todas as colunas
df = pd.read_csv("amazon.csv")

# --------------------------------------------------
# 1. Criando o CSV para a Tabela [dim_produto]
# Colunas: product_id, product_name, category, discounted_price, 
#         actual_price, discount_percentage, rating, rating_count, 
#         about_product, img_link, product_link
# --------------------------------------------------
dim_produto_columns = [
    'product_id',
    'product_name',
    'category',
    'discounted_price',
    'actual_price',
    'discount_percentage',
    'rating',
    'rating_count',
    'about_product',
    'img_link',
    'product_link'
]

df_dim_produto = df[dim_produto_columns].drop_duplicates()
df_dim_produto.to_csv("dim_produto.csv", index=False)
print("dim_produto.csv gerado com sucesso!")

# --------------------------------------------------
# 2. Criando o CSV para a Tabela [dim_user]
# Colunas: user_id, user_name
# --------------------------------------------------
dim_user_columns = [
    'user_id',
    'user_name'
]

df_dim_user = df[dim_user_columns].drop_duplicates()
df_dim_user.to_csv("dim_user.csv", index=False)
print("dim_user.csv gerado com sucesso!")

# --------------------------------------------------
# 3. Criando o CSV para a Tabela [review]
# Colunas: review_id, review_title, review_content, product_id, user_id
# (Esses campos servirão de fato para referenciar as dimensões)
# --------------------------------------------------
fact_review_columns = [
    'review_id',
    'review_title',
    'review_content',
    'product_id',  # chave para DimProduct
    'user_id'      # chave para DimUser
]

df_fact_review = df[fact_review_columns].drop_duplicates()
df_fact_review.to_csv("review.csv", index=False)
print("review.csv gerado com sucesso!")
