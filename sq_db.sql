CREATE TABLE IF NOT EXISTS mainmenu (
    id INTEGER PRIMARY KEY autoincrement,
    title text NOT NULL,
    url text NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY autoincrement,
    title text NOT NULL, 
    text text NOT NULL,
    time integer NOT NULL
);

