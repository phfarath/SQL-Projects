import mysql.connector
import csv

# Configurações da conexão
config = {
    'user': 'root',
    'password': 'sql2005',
    'host': 'localhost',
    'database': 'db_vendas'
}

def insert_data_from_csv(file_path, table_name, columns):
    # Conecta ao banco de dados
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Cria uma lista de valores de acordo com a ordem das colunas
            values = [row[col] for col in columns]
            
            # Cria os placeholders para cada coluna
            placeholders = ', '.join(['%s'] * len(columns))
            
            # Cria a query; DtInclusao usará CURDATE() definido na query
            query = f"INSERT INTO {table_name} ({', '.join(columns)}, DtInclusao) VALUES ({placeholders}, CURDATE())"
            
            cursor.execute(query, values)
    
    # Confirma a transação e fecha a conexão
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Inserção a partir do CSV concluída.")

if __name__ == "__main__":
    file_path = "dim_user.csv"
    table_name = 'dim_user'
    # As colunas do CSV devem corresponder aos nomes na tabela (exceto DtInclusao, que é gerado automaticamente)
    columns = [
        'user_id', 
        'user_name'
    ]
    
    insert_data_from_csv(file_path, table_name, columns)
