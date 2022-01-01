CREATE TABLE users(
    user_id BIGSERIAL PRIMARY KEY NOT NULL,
    firstname VARCHAR (20) NOT NULL,
    lastname VARCHAR (20) NOT NULL,
    username VARCHAR(40) NOT NULL,
    master_pwd VARCHAR (50) NOT NULL
);

CREATE TABLE site_creds(
    sitename VARCHAR (100) NOT NULL,
    site_email VARCHAR (319) NOT NULL,
    password VARCHAR (50) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);