import sqlite3
connection = sqlite3.connect("pets.db")

cursor = connection.cursor()
# cursor.execute()

person_id = input("Please enter your id(-1:stop)")
cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id, ))
row = cursor.fetchone()

if row == None:
    print("Person does not exists")
else:
    first_name = row[0]
    last_name = row[1]
    age = row[2]
    print(f"{first_name} {last_name}, {age} years old")
    cursor.execute("SELECT pet_id FROM person_pet WHERE person_id = ?", (person_id,))
    pet_id = []
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        pet_id.append(id)
    for id in pet_id:
        cursor.execute("SELECT name, breed, age, dead FROM pet WHERE id = ?", (id,))
        pet_data = cursor.fetchone()
        name = pet_data[0]
        breed = pet_data[1]
        age = pet_data[2]
        dead = pet_data[3]
        print(f"{first_name} {last_name} owned {name} a {breed}that was {age} years old")
connection.close()