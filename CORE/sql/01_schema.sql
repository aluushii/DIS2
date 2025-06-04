-- sql/schema.sql

DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe TEXT NOT NULL,
    size TEXT NOT NULL,
    overvidde_cm REAL,
    length_cm REAL,
    material_g REAL NOT NULL,
    strikkefasthed TEXT,
    needle REAL NOT NULL,
    diff REAL,
    yarn TEXT NOT NULL
);

