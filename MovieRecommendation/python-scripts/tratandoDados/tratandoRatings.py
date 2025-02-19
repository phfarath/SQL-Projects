import pandas as pd 

file = "MovieRecommendation/dataset/filtrado/ratings.csv"

df = pd.read_csv(file, encoding='utf-8', on_bad_lines='skip', low_memory=False)

print(df.info())
print(df.columns)