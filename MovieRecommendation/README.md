# 📌 Sistema de Recomendação e Consultas SQL

Este projeto implementa um sistema de recomendação de filmes utilizando SQL, além de consultas complementares para análise dos dados.

---

## 📂 Estrutura das Tabelas

### 1. `movies` 🎬
Armazena informações sobre os filmes.

```sql
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    directors TEXT,
    starring TEXT,
    release_year INT,
    mpaa_rating VARCHAR(50)
);
```

### 2. `ratings` ⭐
Registra as avaliações dos filmes.

```sql
CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    avg_rating DECIMAL(3,1),
    num_ratings INT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);
```

### 3. `movie_prices` 💰
Armazena os preços dos filmes em diferentes formatos.

```sql
CREATE TABLE movie_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    format VARCHAR(100),
    price_dollars DECIMAL(10,2),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);
```

---

## 🔍 Consultas SQL

### 📢 1. Sistema de Recomendação de Filmes Similares
Recomenda filmes semelhantes a um determinado filme com base na média de avaliação.

```sql
SELECT DISTINCT
    m2.movie_id,
    m2.title,
    r2.avg_rating,
    r2.num_ratings,
    ABS(r2.avg_rating - r1.avg_rating) AS diff_rating
FROM movies m1
JOIN ratings r1 ON m1.movie_id = r1.movie_id
JOIN ratings r2 ON m1.movie_id <> r2.movie_id
JOIN movies m2 ON r2.movie_id = m2.movie_id
WHERE m1.movie_id = 123  -- Substitua 123 pelo ID do filme de interesse
  AND ABS(r2.avg_rating - r1.avg_rating) <= 0.5
ORDER BY diff_rating ASC, r2.num_ratings DESC
LIMIT 10;
```

📌 **Parâmetro:** Substitua `123` pelo ID do filme que deseja obter recomendações.

---

### 🎬 2. Contagem de Filmes Gratuitos
Retorna o número total de filmes que possuem pelo menos um formato gratuito.

```sql
SELECT COUNT(DISTINCT movie_id) AS free_movies_count
FROM movie_prices
WHERE price_dollars = 0.00;
```

---

### 🆓 3. Listagem de Filmes Gratuitos
Lista os filmes disponíveis gratuitamente, incluindo formato e avaliações.

```sql
SELECT DISTINCT
    m.movie_id,
    m.title,
    r.avg_rating,
    r.num_ratings,
    mp.format
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
JOIN movie_prices mp ON m.movie_id = mp.movie_id
WHERE mp.price_dollars = 0.00;
```

---

### 🏆 4. Ranking dos Filmes por Avaliação
Gera um ranking dos filmes baseado na média de avaliações.

```sql
SELECT DISTINCT
    m.movie_id,
    m.title,
    r.avg_rating,
    r.num_ratings,
    RANK() OVER (ORDER BY r.avg_rating DESC, r.num_ratings DESC) AS ranking
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id;
```

---

### 🎥 5. Pares de Filmes do Mesmo Diretor com Avaliações Similares
Encontra pares de filmes do mesmo diretor que possuem avaliações semelhantes.

```sql
SELECT DISTINCT
    m1.movie_id AS movie1_id,
    m1.title AS movie1_title,
    m2.movie_id AS movie2_id,
    m2.title AS movie2_title,
    ABS(r1.avg_rating - r2.avg_rating) AS rating_diff
FROM movies m1
JOIN movies m2 ON m1.directors = m2.directors AND m1.movie_id < m2.movie_id
JOIN ratings r1 ON m1.movie_id = r1.movie_id
JOIN ratings r2 ON m2.movie_id = r2.movie_id
WHERE ABS(r1.avg_rating - r2.avg_rating) < 0.5;
```

---
Desenvolvido por Pedro Farath, apenas para fins exploratórios e acadêmicos.