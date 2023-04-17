CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist (id)
);


CREATE TABLE track (
    id INTEGER PRIMARY KEY,
    album_id INTEGER NOT NULL,
    track_name TEXT NOT NULL,
    track_number INTEGER NOT NULL,
    track_len INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album (id)
);






