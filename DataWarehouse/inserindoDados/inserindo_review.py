import mysql.connector
import csv

# Configurações da conexão com o banco de dados
config = {
    'user': 'root',
    'password': 'sql2005',
    'host': 'localhost',
    'database': 'db_vendas'
}

def insert_reviews_from_csv(file_path):
    # Cria um cursor buffered para evitar o erro "Unread result found"
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extraindo os valores do CSV conforme a ordem das colunas
            review_id = row['review_id']
            review_title = row['review_title']
            review_content = row['review_content']
            product_id = row['product_id']
            user_id = row['user_id']

            # Busca o ProductKey na tabela dim_produto usando product_id
            query_product = "SELECT ProductKey FROM dim_produto WHERE product_id = %s"
            cursor.execute(query_product, (product_id,))
            result_product = cursor.fetchone()
            if result_product:
                product_key = result_product[0]
            else:
                print(f"Produto com product_id '{product_id}' não encontrado. Registro ignorado.")
                continue

            # Busca o UserKey na tabela dim_user usando user_id
            query_user = "SELECT UserKey FROM dim_user WHERE user_id = %s"
            cursor.execute(query_user, (user_id,))
            result_user = cursor.fetchone()
            if result_user:
                user_key = result_user[0]
            else:
                print(f"Usuário com user_id '{user_id}' não encontrado. Registro ignorado.")
                continue

            # Insere o registro na tabela review; DtInclusao é definido via CURDATE()
            query_insert = """
                INSERT INTO review (review_id, ProductKey, UserKey, review_title, review_content, DtInclusao)
                VALUES (%s, %s, %s, %s, %s, CURDATE())
            """
            cursor.execute(query_insert, (review_id, product_key, user_key, review_title, review_content))
    
    # Confirma a transação e fecha a conexão
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Inserção dos reviews a partir do CSV concluída.")

if __name__ == "__main__":
    file_path = "review.csv"  # Certifique-se de que o arquivo contenha as colunas: review_id, review_title, review_content, product_id, user_id
    insert_reviews_from_csv(file_path)
