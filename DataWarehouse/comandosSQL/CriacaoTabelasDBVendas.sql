CREATE TABLE dim_produto (
    ProductKey INT AUTO_INCREMENT PRIMARY KEY,  -- Chave substituta
    product_id INT NOT NULL,                      -- ID original do produto
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    discounted_price DECIMAL(10,2),
    actual_price DECIMAL(10,2),
    discount_percentage DECIMAL(5,2),
    rating DECIMAL(3,2),
    rating_count INT,
    about_product TEXT,
    img_link VARCHAR(500),
    product_link VARCHAR(500),
    DtInclusao DATE,
    UNIQUE KEY uq_product_id (product_id)         -- Garante que cada product_id seja único
);

CREATE TABLE dim_user (
    UserKey INT AUTO_INCREMENT PRIMARY KEY,  -- Chave substituta
    user_id INT NOT NULL,                     -- ID original do usuário
    user_name VARCHAR(255) NOT NULL,
    DtInclusao DATE,
    UNIQUE KEY uq_user_id (user_id)           -- Garante que cada user_id seja único
);

CREATE TABLE review (
    FactReviewID INT AUTO_INCREMENT PRIMARY KEY,
    review_id INT NOT NULL,         -- ID original do review
    ProductKey INT NOT NULL,        -- FK para DimProduct
    UserKey INT NOT NULL,           -- FK para DimUser
    review_title VARCHAR(255),
    review_content TEXT,
    DtInclusao DATE,
    
    CONSTRAINT fk_fact_review_product 
        FOREIGN KEY (ProductKey) REFERENCES dim_produto(ProductKey),
    CONSTRAINT fk_fact_review_user 
        FOREIGN KEY (UserKey) REFERENCES dim_user(UserKey)
);
