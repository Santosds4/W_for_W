DROP TABLE IF EXISTS posts

CREATE TABLE tabela_exemplo(
    id INTEGER PRIMARY KEY AUTOINCREMET,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
);
