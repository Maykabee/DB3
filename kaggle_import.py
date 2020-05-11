import csv
import cx_Oracle

username = 'Maya'
password = 'Maya'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username,password,databaseName)
cursor = connection.cursor()

tables = ['Game', 'Genre', 'Publisher', 'Region','Sales']
for table in tables:
    cursor.execute("DELETE FROM " +table)

with open('PS4.csv', 'rt') as inp, open('PS4_edit.csv', 'wt',newline='') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if (row[0] != "N/A") and (row[1] != "N/A") and (row[2] !="N/A") and (row[3] != "N/A"):
            writer.writerow(row)

csv_file = open('PS4_edit.csv', encoding='utf-8', errors='ignore')
data = csv.reader(csv_file, delimiter=',')

genre_unique = []
publisher_unique = []

cursor.execute("INSERT INTO Region(region_name) VALUES ('North_America')")
cursor.execute("INSERT INTO Region(region_name) VALUES ('Europe')")
cursor.execute("INSERT INTO Region(region_name) VALUES ('Japan')")
cursor.execute("INSERT INTO Region(region_name) VALUES ('Rest_of_world')")


next(data)
for row in data:
    game = row[0].strip()
    year = row[1].strip()
    genre = row[2].strip()
    publisher = row[3].strip()
    value1 = row[4].strip()
    value2 = row[5].strip()
    value3 = row[6].strip()
    value4 = row[7].strip()


    if genre not in genre_unique:
        genre_unique.append(genre)
        cursor.execute("INSERT INTO Genre(genre_name) VALUES(:genre)", genre=genre)


    if publisher not in publisher_unique:
        publisher_unique.append(publisher)
        cursor.execute("INSERT INTO Publisher(publisher_name) VALUES(:publisher)", publisher=publisher)


    cursor.execute("""INSERT INTO Game(game_name,year,genre_name,publisher_name) 
                   VALUES(:game_name, :year, :genre_name, :publisher_name)""",
		game_name = game, year = year, genre_name = genre, publisher_name = publisher)

    cursor.execute("INSERT INTO Sales(game_name,region_name,sales) "
                   "VALUES(:game_name, :region_name, :sales)",
                   game_name=game, region_name='North_America', sales=value1)

    cursor.execute("INSERT INTO Sales(game_name,region_name,sales) "
                   "VALUES(:game_name, :region_name, :sales)",
                   game_name=game, region_name='Europe', sales=value2)

    cursor.execute("INSERT INTO Sales(game_name,region_name,sales) "
                   "VALUES(:game_name, :region_name, :sales)",
                   game_name=game, region_name='Japan', sales=value3)

    cursor.execute("INSERT INTO Sales(game_name,region_name,sales) "
                   "VALUES(:game_name, :region_name, :sales)",
                   game_name=game, region_name='Rest_of_world', sales=value4)

connection.commit()
cursor.close()
connection.close()
csv_file.close()