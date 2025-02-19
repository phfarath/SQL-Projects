import mysql.connector
import csv

def inserir_dados_em_prices():
    try:
        # Conectar ao MySQL
        conn = mysql.connector.connect(
            host="localhost",
            database="recomendacao_filmes",
            user="root",
            password="sql2005",
            allow_local_infile=True
        )
        cursor = conn.cursor()

        # Abrir o arquivo CSV tratado
        with open("MovieRecommendation/dataset/filtrado/movie_prices.csv", "r", encoding="utf-8") as csvfile:
            leitor = csv.reader(csvfile)
            next(leitor)  # Pular cabeçalho

            dados = []
            for linha in leitor:
                movie_id = int(linha[0]) if linha[0].isdigit() else None  # Garantir que `movie_id` seja inteiro
                format_type = linha[1] if linha[1] else "Desconhecido"  # Garantir que `format` não seja vazio
                price_dollars = float(linha[2]) if linha[2] else 0.0  # Garantir que `price_dollars` seja numérico (0 se vazio)

                dados.append((movie_id, format_type, price_dollars))

            # Query de inserção
            sql = """
            INSERT INTO movie_prices (movie_id, format, price_dollars)
            VALUES (%s, %s, %s);
            """

            # Inserir em lotes para melhor performance
            tamanho_lote = 2108  # Ajuste conforme necessário
            for i in range(0, len(dados), tamanho_lote):
                cursor.executemany(sql, dados[i:i+tamanho_lote])
                conn.commit()
                print(f"✅ Inseridos {i + tamanho_lote} registros...")

        print("✅ Todos os dados foram inseridos com sucesso!")

    except Exception as e:
        print("❌ Erro ao inserir dados:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    inserir_dados_em_prices()
