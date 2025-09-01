PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categories (
  id   INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS technologies (
  id          INTEGER PRIMARY KEY,
  slug        TEXT NOT NULL UNIQUE,
  name        TEXT NOT NULL UNIQUE,
  first_use   TEXT,            -- text to allow ranges/BCE
  region      TEXT,
  category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
  description TEXT,
  notes       TEXT
);

CREATE TABLE IF NOT EXISTS battles (    -- optional: filled from WarChest
  id        INTEGER PRIMARY KEY,
  name      TEXT NOT NULL,
  year      TEXT,
  war       TEXT,
  location  TEXT
);

CREATE TABLE IF NOT EXISTS tech_battles (
  tech_id    INTEGER NOT NULL REFERENCES technologies(id) ON DELETE CASCADE,
  battle_id  INTEGER NOT NULL REFERENCES battles(id) ON DELETE CASCADE,
  PRIMARY KEY (tech_id, battle_id)
);

-- handy view
CREATE VIEW IF NOT EXISTS tech_overview AS
SELECT t.slug, t.name, t.first_use, t.region, c.name AS category
FROM technologies t LEFT JOIN categories c ON c.id = t.category_id;
