CREATE TABLE person(
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  age INTEGER
);

CREATE TABLE pet(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);

# Answering 2.2 - The reason for the preson_pet table is to assign the pet_id to the proper person
CREATE TABLE person_pet(
    person_id INTEGER,
    pet_id INTEGER
);
