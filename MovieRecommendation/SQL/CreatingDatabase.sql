-- criando a tabela sobre os filmes 
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    directors TEXT,
    starring TEXT,
    release_year INT,
    mpaa_rating VARCHAR(50)
);

-- criando a tabela de avaliações dos filmes 
CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    avg_rating DECIMAL(3,1),
    num_ratings INT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- criando a tabela dos preços dos filmes 
CREATE TABLE movie_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    format VARCHAR(100),
    price_dollars DECIMAL(10,2),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

