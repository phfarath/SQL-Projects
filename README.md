# Data Warehouse - Projeto de Análise de Vendas

## Descrição do Projeto
Este projeto implementa um **Data Warehouse** para armazenar, processar e analisar dados de vendas, produtos, usuários e avaliações. O objetivo é centralizar e otimizar consultas analíticas sobre reviews de produtos, permitindo insights sobre tendências de mercado, categorias mais bem avaliadas e participação dos usuários.

## Estrutura do Banco de Dados
O modelo segue a estrutura **Star Schema**, composta por tabelas dimensionais e uma tabela para os reviews.

### Tabelas e Estrutura:
#### **dim_produto** (Dimensão dos Produtos)
Armazena informações sobre os produtos, incluindo preço, categoria e avaliações.
```sql
CREATE TABLE dim_produto (
    ProductKey INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(100) NOT NULL,
    product_name TEXT NOT NULL,
    category TEXT,
    discounted_price DECIMAL(10,2),
    actual_price DECIMAL(10,2),
    discount_percentage DECIMAL(5,2),
    rating DECIMAL(3,2),
    rating_count INT,
    about_product TEXT,
    img_link VARCHAR(500),
    product_link VARCHAR(500),
    DtInclusao DATE
);
```

#### **dim_user** (Dimensão dos Usuários)
Armazena os dados dos usuários que postaram reviews.
```sql
CREATE TABLE dim_user (
    UserKey INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    DtInclusao DATE
);
```

#### **review** (Tabela Fato - Avaliações)
Armazena as reviews de produtos feitas pelos usuários, conectando-se às tabelas dimensionais.
```sql
CREATE TABLE review (
    FactReviewID INT AUTO_INCREMENT PRIMARY KEY,
    review_id VARCHAR(255) NOT NULL,
    ProductKey INT NOT NULL,
    UserKey INT NOT NULL,
    review_title TEXT,
    review_content TEXT,
    DtInclusao DATE,
    FOREIGN KEY (ProductKey) REFERENCES dim_produto(ProductKey),
    FOREIGN KEY (UserKey) REFERENCES dim_user(UserKey)
);
```

## Importação de Dados
Os dados das tabelas **dim_produto** e **dim_user** são inseridos via script Python utilizando arquivos CSV.

### **Script para Inserção em Tabelas Dimensionais**
```python
import mysql.connector
import csv

# Configuração do banco
config = {
    'user': 'root',
    'password': 'sql2005',
    'host': 'localhost',
    'database': 'db_vendas'
}

def insert_data_from_csv(file_path, table_name, columns):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            values = [row[col] for col in columns]
            placeholders = ', '.join(['%s'] * len(columns))
            query = f"INSERT INTO {table_name} ({', '.join(columns)}, DtInclusao) VALUES ({placeholders}, CURDATE())"
            cursor.execute(query, values)
    
    cnx.commit()
    cursor.close()
    cnx.close()
    print(f"Inserção concluída para {table_name}.")
```

### **Script para Inserção da Tabela de Reviews**
```python
import mysql.connector
import csv

def insert_reviews_from_csv(file_path):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            review_id = row['review_id']
            review_title = row['review_title']
            review_content = row['review_content']
            product_id = row['product_id']
            user_id = row['user_id']
            
            cursor.execute("SELECT ProductKey FROM dim_produto WHERE product_id = %s", (product_id,))
            product_key = cursor.fetchone()
            if not product_key: continue
            
            cursor.execute("SELECT UserKey FROM dim_user WHERE user_id = %s", (user_id,))
            user_key = cursor.fetchone()
            if not user_key: continue

            query = """
                INSERT INTO review (review_id, ProductKey, UserKey, review_title, review_content, DtInclusao)
                VALUES (%s, %s, %s, %s, %s, CURDATE())
            """
            cursor.execute(query, (review_id, product_key[0], user_key[0], review_title, review_content))
    
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Reviews inseridos com sucesso.")
```

## Exemplos de Consultas SQL para Análise

### 1. **Listando reviews com informações sobre o Produto e o Usuários, ordenando por nome do produto**
```sql
SELECT r.review_title, r.review_content, p.product_name, u.user_name
FROM review r
JOIN dim_produto p ON r.ProductKey = p.ProductKey
JOIN dim_user u ON r.UserKey = u.UserKey
ORDER BY p.product_name;
```

### 2. **Total de Reviews por categoria de produto, as 20 categorias com mais reviews**
```sql
SELECT p.category, COUNT(r.review_id) AS reviews_totais
FROM dim_produto p
JOIN review r ON p.ProductKey = r.ProductKey
GROUP BY p.category
ORDER BY reviews_totais DESC
LIMIT 20;
```

### 3. **5 Categorias com mais avaliações (rating_count)**
```sql
SELECT category, SUM(rating_count) AS avaliação_total
FROM dim_produto
GROUP BY category
ORDER BY avaliação_total DESC
LIMIT 5;
```

## Conclusão
Este projeto de Data Warehouse permite o armazenamento e análise de reviews de produtos, oferecendo insights valiosos sobre produtos mais avaliados, categorias mais populares e comportamento dos usuários. As consultas otimizadas permitem extrair informações rápidas e precisas para tomada de decisões.

---
### Autor
Desenvolvido por Pedro Farath como parte de um projeto de aprendizado e implementação de Data Warehouse.

