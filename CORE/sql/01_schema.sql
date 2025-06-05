DROP TABLE IF EXISTS knitted_by;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS needles;
DROP TABLE IF EXISTS yarns;

CREATE TABLE yarns (
  id   SERIAL PRIMARY KEY,
  name TEXT   NOT NULL UNIQUE
);

CREATE TABLE needles (
  id   SERIAL PRIMARY KEY,
  size REAL   NOT NULL UNIQUE
);

CREATE TABLE recipes (
  id             SERIAL PRIMARY KEY,
  pattern_name   TEXT   NOT NULL,
  size           TEXT   NOT NULL,
  overvidde_cm   REAL,
  length_cm      REAL,
  strikkefasthed TEXT,
  diff           REAL
);

CREATE TABLE knitted_by (
  id         SERIAL PRIMARY KEY,
  recipe_id  INTEGER NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
  yarn_id    INTEGER NOT NULL REFERENCES yarns(id)   ON DELETE CASCADE,
  needle_id  INTEGER NOT NULL REFERENCES needles(id) ON DELETE CASCADE,
  material_g REAL    NOT NULL,
  UNIQUE(recipe_id, yarn_id, needle_id)
);
