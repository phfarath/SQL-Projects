import mysql.connector
import csv

def inserir_dados_em_movies():
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
        with open("MovieRecommendation/dataset/filtrado/movies.csv", "r", encoding="utf-8") as csvfile:
            leitor = csv.reader(csvfile)
            next(leitor)  # Pular cabeçalho

            dados = []
            for linha in leitor:
                movie_id = linha[0] if linha[0].isdigit() else None  # Garante que o ID seja numérico
                title = linha[1]
                directors = linha[2]
                starring = linha[3]
                release_year = linha[4] if linha[4] and linha[4] != 'nan' else None  # Corrige valores vazios
                mpaa_rating = linha[5]

                dados.append((movie_id, title, directors, starring, release_year, mpaa_rating))

            # Query de inserção **incluindo movie_id**
            sql = """
            INSERT INTO movies (movie_id, title, directors, starring, release_year, mpaa_rating)
            VALUES (%s, %s, %s, %s, %s, %s);
            """

            # Inserir dados
            tamanho_lote = 2108
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
    inserir_dados_em_movies()
